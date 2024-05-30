# 🎬 Cinema Seek

Cinema Seek is a Python-based 🐍 application that allows users to search for movies 🎥. It uses Flask, Redis, Elasticsearch, and an external API to provide search results.

## 🌟 Features

- **Redis Caching**: The application uses Redis as a caching layer to store the results of movie searches. This significantly improves the performance of the application by reducing the need for repeated expensive operations, such as querying the Elasticsearch index or making external API calls.

- **Elasticsearch Support**: The application uses Elasticsearch for storing and searching movie data. Elasticsearch provides powerful full-text search capabilities and is highly scalable.

- **External API Calls**: In case a movie search result is not found in the Redis cache or Elasticsearch index, the application makes an external API call to fetch the movie data. This ensures that the application can always return the most up-to-date and comprehensive movie data.

- **Dockerized Application**: The application and its dependencies (Redis, Elasticsearch) are containerized using Docker. This makes it easy to set up the development environment and deploy the application.

- **Kubernetes Deployment**: The project includes a Kubernetes deployment script, making it ready for deployment in a Kubernetes cluster.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose
- Python
- Pip

### Installation

1. Clone the repository
```shell
git clone https://github.com/Adibov/cinema-seek.git
```

2. Navigate to the project directory
```shell
cd cinema-seek
```

3. Build and run the Docker containers
```shell
docker-compose up --build
```

## 📚 Usage

The application is accessible at `http://localhost:5000/search-movie?query=<movie_name>`

## 🚢 Deployment

The project includes a Kubernetes deployment script. To deploy, run the following commands:

```shell
./deployment/deploy.sh
```

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Redis](https://redis.io/)
- [Elasticsearch](https://www.elastic.co/)

## 👥 Authors

- Adibov

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details