FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/
RUN pip install setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ARG HOST="http://image-manager.pre.spb.play.dc/images/v4/"
ARG STATIC_URL="http://static.okko.tv/images/v4/"
ENV HOST=$HOST
ENV STATIC_URL=$STATIC_URL
ARG WORKERS=4

EXPOSE 8000

RUN mkdir "./screenshots"
VOLUME /app/screenshots

#CMD pytest ./tests/*.py --image-snapshot-save-diff -v
ENTRYPOINT pytest ./tests/placeholder.py --image-snapshot-save-diff -v

#wget https://github.com/allure-framework/allure2/releases/download/2.32.2/allure-2.32.2.tgz
#allure serve allure-results --port 8000