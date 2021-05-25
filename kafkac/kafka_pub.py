from kafka import KafkaProducer
import logging
from kafka.errors import KafkaError
import sys

producer = [None]

def SetupKafkaProducer(brokers):
    try:
        producer[0] = KafkaProducer(bootstrap_servers=brokers, client_id='vwap')
    except KafkaError:
        logging.exception("Error connecting to Kafka")
        sys.exit(1)

def PublishVWAPToKafka(product_id, vwap):
    if producer[0] is None:
        logging.error("Call SetupKafkaProducer before calling publish...")
        return
    
    producer[0].send("vwap-" + product_id, str(vwap).encode('utf-8'))
