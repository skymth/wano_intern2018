FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -yq make cmake gcc g++ unzip wget build-essential gcc zlib1g-dev 

# Python3のインストール
WORKDIR /root/
RUN wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz \
        && tar zxf Python-3.6.0.tgz \
        && cd Python-3.6.0 \
        && ./configure \
        && make altinstall
ENV PYTHONIOENCODING "utf-8"
RUN apt-get install -y python3-pip python-qt4

RUN apt-get install build-essential libssl-dev libffi-dev python-dev
RUN pip3 install flask peewee pandas datetime timedelta sqlalchemy pymysql

