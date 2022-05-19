FROM python:3.8

WORKDIR /traine

EXPOSE 8000

COPY . .

RUN pipenv install