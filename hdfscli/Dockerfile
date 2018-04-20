FROM python:3.6-slim

WORKDIR /opt

ENV HDFSCLI_CONFIG=/opt/.hdfscli.cfg

COPY .hdfscli.cfg /opt/

RUN mkdir /opt/data

RUN pip install ipython

RUN pip install hdfs

ENTRYPOINT sleep 5 && /usr/local/bin/hdfscli upload /opt/data/dataset.csv /user/dataset.csv

