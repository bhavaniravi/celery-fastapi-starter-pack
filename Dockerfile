FROM python:3.11.0-bullseye

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

CMD celery -A app worker --loglevel=info