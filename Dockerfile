
FROM python:3.9.5-slim-buster

#start

RUN mkdir ./app
RUN chmod 777 ./app
WORKDIR /app

RUN apt -qq update

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata


RUN apt -qq install -y git python3 python3-pip wget
COPY requirements.txt .
#try
RUN pip3 install --no-cache-dir -r requirements.txt
COPY deploy.sh .
RUN bash deploy.sh
COPY . .
CMD ["python3", "-m", "Phoenix"]
