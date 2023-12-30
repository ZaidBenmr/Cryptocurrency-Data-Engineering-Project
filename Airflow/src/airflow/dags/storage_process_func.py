from confluent_kafka import Consumer, KafkaError
from pymongo import MongoClient
import json
import re
import datetime

def consume_kafka_data() :
    consumer_config = {
    'bootstrap.servers': '192.168.11.108:9092',  # Kafka broker(s)
    'group.id': 'my-consumer'                # Consumer group ID
    #'auto.offset.reset': 'earliest'         # Read messages from the beginning of the topic
    }

    consumer = Consumer(consumer_config)
    consumer.subscribe(['cryptobalance'])

    # Making a Connection with MongoClient
    client = MongoClient("mongodb://192.168.11.108:27017/")
    # database
    db = client["cryptocurrencies"]
    # collection
    company= db["Crypto_balance"]

    return consumer, company

def clean_data(data):
    # Replace "$" and commas with an empty string for numeric fields
    data["onehour"]     = float(re.sub(r'[^\d.]', '', data["onehour"]))
    data["oneday"]      = float(re.sub(r'[^\d.]', '', data["oneday"]))
    data["sevendays"]   = float(re.sub(r'[^\d.]', '', data["sevendays"]))
    data["marketcap"]   = float(re.sub(r'[^\d.]', '', data["marketcap"]))
    data["Volume"]      = float(re.sub(r'[^\d.]', '', data["Volume"]))

    # Handle the case where 'price' contains ellipsis ("...")
    if '...' in data["price"]:
        data["price"] =  float(re.sub(r'[^\d.]', '', data["price"].replace('...', '0000')))
    else:
        data["price"] = float(re.sub(r'[^\d.]', '', data["price"]))
    
    data["datetime"] = datetime.datetime.strptime(data["datetime"], "%Y-%m-%d %H:%M:%S")
    
    return data


def read_clean_scraped_data() : 

    consumer ,company = consume_kafka_data()

    while True:
        msg = consumer.poll(1.0)  # Poll for messages, with a timeout

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('Reached end of partition')
            else:
                print('Error while polling for messages: {}'.format(msg.error()))
        else:
            # Process the received message
            print('Received message: {}'.format(msg.value()))
            
            # Deserialize the message value (assuming it's in bytes)
            message_data = msg.value()

            # Convert the deserialized data to JSON format
            try:
                json_data = json.loads(message_data)
            except json.JSONDecodeError as e:
                print('Error decoding JSON: {}'.format(e))
                continue

            # Clean the data
            cleaned_json = clean_data(json_data)

            # Store the JSON document in MongoDB
            company.insert_one(cleaned_json)


if __name__ == "__main__":
    read_clean_scraped_data()

