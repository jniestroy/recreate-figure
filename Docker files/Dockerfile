FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-pip build-essential
COPY requirements.txt .
COPY data_cleaning.py /usr/local/bin
RUN chmod +x /usr/local/bin/data_cleaning.py
COPY create_fig.py /usr/local/bin
RUN chmod +x /usr/local/bin/create_fig.py
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
