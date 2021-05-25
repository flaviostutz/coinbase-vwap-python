FROM python:3.9.5-buster

RUN pip install websocket-client
RUN pip install kafka-python

ENV LOG_LEVEL 'info'
ENV COINBASE_WS_URL 'wss://ws-feed-public.sandbox.pro.coinbase.com'
ENV KAFKA_BROKERS ''

ADD /startup.sh /
ADD / /app
ENTRYPOINT /startup.sh

EXPOSE 4000
