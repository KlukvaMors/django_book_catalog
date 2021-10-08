FROM python:3.8

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
COPY . /usr/src/app/

EXPOSE 8000

# install psycopg2 dependencies
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

RUN pip install --no-cache-dir -r requirements.txt
