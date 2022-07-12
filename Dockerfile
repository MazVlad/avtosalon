FROM python:3.8

WORKDIR .

EXPOSE 8000

COPY . .

RUN pip install pipenv && pipenv install --deploy --system