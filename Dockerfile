FROM ubuntu:20.04


RUN mkdir ./app
RUN chmod 777 ./app
WORKDIR /app

RUN apt -qq update

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata


RUN apt -qq install -y git python3 python3-pip
COPY requirements.txt .

COPY deploy.sh .
RUN bash deploy.sh
COPY . .
CMD ["python3", "-m", "Toxic"]
