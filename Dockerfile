FROM python:3.12-slim
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app
RUN pip install setuptools
RUN pip install allure-pytest
RUN pip install pytest-xdist
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ARG HOST="http://image-manager.pre.spb.play.dc/images/v4/"
ARG STATIC_URL="http://static.okko.tv/images/v4/"
ARG WORKERS=6
ENV WORKERS=$WORKERS
ENV HOST=$HOST
ENV STATIC_URL=$STATIC_URL


RUN mkdir "allure-results"
VOLUME /app/allure-results

ENTRYPOINT /bin/bash run_docker.sh lf ${WORKERS}