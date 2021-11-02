FROM python:3.8.12-slim-bullseye

COPY requirements.txt /app/requirements.txt

WORKDIR /app

ADD . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py collectstatic --noinput

ENTRYPOINT ["./gunicorn_starter.sh"]