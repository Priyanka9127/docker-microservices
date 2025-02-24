FROM python:3.9-slim-buster

WORKDIR /worker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["celery", "-A", "worker", "worker", "--loglevel=INFO"]