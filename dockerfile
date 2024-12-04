FROM  nvidia/cuda:12.2.2-devel-ubuntu22.04

RUN apt update \
    && apt install -y \
    git\
    python3\
    python3-pip

RUN apt-get autoremove -y && apt-get clean && \
    rm -rf /usr/local/src/*

COPY requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /tmp/
