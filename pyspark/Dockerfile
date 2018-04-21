FROM bde2020/spark-submit:2.3.0-hadoop2.7 
 
WORKDIR /opt 

RUN apt-get update && apt-get install gcc -y && \ 
    apt-get install make  -y && \ 
    apt-get install zlib1g-dev -y && \
    apt-get -y install build-essential python-dev python-setuptools python-pip python-smbus libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev openssl libffi-dev

RUN wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz && \
    tar -xvf Python-3.6.3.tgz && \
    cd Python-3.6.3 && \
    ./configure && \
    make && \
    make install

RUN python3.6 -m pip install findspark pyspark ipython

COPY init.py . 