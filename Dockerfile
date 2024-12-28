FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN python --version && pip --version

# FIX
RUN pip install PyPDF2 --break-system-packages

WORKDIR /app
COPY . /app