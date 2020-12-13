FROM python:3.8-slim
MAINTAINER sajib1066.github.io

ENV PYTHONBUFFERED 1

RUN apt update
RUN apt clean

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /job-finder-backend
WORKDIR /job-finder-backend
COPY . /job-finder-backend
EXPOSE 8000
CMD python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
