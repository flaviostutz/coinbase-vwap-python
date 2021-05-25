#!/bin/bash

echo "Starting coinbase-vwap-python..."

/app/coinbase-vwap.py \
  --loglevel="$LOG_LEVEL" \
  --coinbase-ws-url="$COINBASE_WS_URL" \
  --kafka-brokers="$KAFKA_BROKERS"
  

