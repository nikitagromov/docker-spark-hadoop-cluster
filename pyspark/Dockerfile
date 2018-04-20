FROM bde2020/spark-submit:2.3.0-hadoop2.7


WORKDIR /opt
RUN pip3 install -U pip
RUN pip3 install findspark
RUN pip3 install pyspark
RUN pip3 install ipython
COPY init.py .
