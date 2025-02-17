FROM python:3.10.11-alpine

WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .

CMD ["python", "cinema-seek.py"]