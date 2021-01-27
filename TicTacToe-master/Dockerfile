FROM alpine:3.1
RUN apk add --update make cmake gcc g++ gfortran
RUN apk add --update python py-pip python-dev
RUN pip install cython
RUN pip install numpy

CMD python main.py
