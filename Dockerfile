FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
COPY .env /app/tests

ARG HOST="http://image-manager.pre.spb.play.dc/images/v4/"
ARG STATIC_URL="http://static.okko.tv/images/v4/"
ENV HOST=$HOST
ENV STATIC_URL=$STATIC_URL
ARG WORKERS=4

EXPOSE 5050
EXPOSE 5252
EXPOSE 8000


RUN mkdir "./screenshots"
VOLUME /app/screenshots

#CMD pytest ./tests/*.py --image-snapshot-save-diff -v
ENTRYPOINT pytest ./tests/placeholder.py --image-snapshot-save-diff -v
#ENTRYPOINT /bin/bash run_pytest.sh lf 4
# --alluredir=allure-results
#wget https://github.com/allure-framework/allure2/releases/download/2.32.2/allure-2.32.2.tgz
#allure serve allure-results --port 8000