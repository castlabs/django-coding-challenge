FROM python:3.6
MAINTAINER Andrew Young <andrew.young@castlabs.com>

RUN mkdir -p /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

WORKDIR /app
