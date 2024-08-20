FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./.env /app/.env

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./applications /app/applications
COPY ./components /app/components

EXPOSE 80 443
