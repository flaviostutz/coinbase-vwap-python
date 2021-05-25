#!/usr/bin/env python3

import argparse
import logging
import sys
import asyncio
import coinbase.stream_client as stream_client
import coinbase.vwap_calculator as vwap_calculator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--loglevel', default='info', help='debug, info, warning, error')
    parser.add_argument('--coinbase-ws-url', default='wss://ws-feed-public.sandbox.pro.coinbase.com', help='Coinbase Websockets API endpoint URL. Defaults to sandbox URL')
    parser.add_argument('--kafka-brokers', default='', help='Kafka broker addresses separated by comma. ex.: kafka1:9092,kafka2:9092')
    args = parser.parse_args()

    #configure log level
    numeric_level = getattr(logging, args.loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.loglevel)
    logging.basicConfig(level=numeric_level)

    if args.coinbase_ws_url == '':
        logging.error("'--coinbase-ws-url' cannot be empty")
        sys.exit(1)

    logging.info("====Starting coinbase-vwap-python====")

    stream_client.SubscribeMatchesChannel(args.coinbase_ws_url, onMatch)

def onMatch(info):
    vwap_calculator.CalculateVWAP(info, 200, onVWAPInfo)

def onVWAPInfo(vwap, product_id):
    logging.info(product_id + "=" + str(vwap)[:15])

if __name__ == '__main__':
    main()
    
