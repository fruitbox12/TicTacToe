FROM python:3.8-alpine
COPY ./. .

RUN apk add --update --no-cache py3-numpy
ENV PYTHONPATH=/usr/lib/python3.8/site-packages
CMD python main.py
