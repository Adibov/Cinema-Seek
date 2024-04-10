import os

from flask import Flask, request, jsonify
import redis
from elasticsearch import Elasticsearch
import requests

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, db=0)
es = Elasticsearch(['http://elastic:9200'],
                   basic_auth=(os.environ.get('ELASTIC_USER'), os.environ.get('ELASTIC_PASS')))
api_url = "https://imdb146.p.rapidapi.com/v1/find/"
api_headers = {
    "X-RapidAPI-Key": os.environ.get('RAPIDAPI_KEY'),
    "X-RapidAPI-Host": "imdb146.p.rapidapi.com"
}


@app.route('/search-movie', methods=['GET'])
def search_movie():
    query = request.args.get('query')

    # Search in Redis
    movie_data = redis_client.get(query)
    if movie_data:
        return jsonify({"source": "Redis", "data": movie_data.decode()})

    # Search in Elasticsearch
    search_body = {
        "query": {
            "match": {
                "Series_Title": query
            }
        }
    }
    search_result = es.search(index='movies_index', body=search_body)
    if search_result['hits']['total']['value'] > 0:
        movie_data = search_result['hits']['hits'][0]['_source']['Series_Title']
        redis_client.set(query, str(movie_data))  # Cache the result in Redis
        return jsonify({"source": "Elasticsearch", "data": movie_data})

    # Search using the external API
    querystring = {"query": query}
    response = requests.get(api_url, headers=api_headers, params=querystring)
    if response.status_code == 200:
        matched_movies = response.json()['titleResults']['results']
        if len(matched_movies) == 0:
            return jsonify({"message": "Movie not found"}), 404
        movie_data = matched_movies[0]['titleNameText']
        redis_client.set(query, str(movie_data))  # Cache the result in Redis
        return jsonify({"source": "External API", "data": movie_data})

    return jsonify({"message": "Movie not found"}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0")
