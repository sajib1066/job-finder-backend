FROM python:3.8-slim
MAINTAINER sajib1066.github.io

ENTRYPOINT ["/entrypoint.sh"]

ENV PYTHONBUFFERED 1

RUN apt update
RUN apt clean

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /job-finder-backend
WORKDIR /job-finder-backend
COPY . /job-finder-backend
EXPOSE 8000

COPY ./entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh
