from confluent_kafka import Consumer, KafkaError
from pymongo import MongoClient
import json
import re
import datetime
import argparse

def consume_kafka_data(topicName, collectionName) :
    consumer_config = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker(s)
    'group.id': 'btc-consumer',              # Consumer group ID
    #'auto.offset.reset': 'earliest'         # Read messages from the beginning of the topic
    }

    consumer = Consumer(consumer_config)
    consumer.subscribe([topicName])

    # Making a Connection with MongoClient
    client = MongoClient("mongodb://localhost:27017/")

    # database
    db = client["cryptocurrencies"]
    company= db[collectionName]

    # collection
    #if (string == "snapshots") :
    #    company= db["XRP_snapshots"]
    #
    #elif (string == "all") : 
    #    company= db["XRP_cleaned"]

    return consumer, company

def clean_data(data):
    # Replace "$" and commas with an empty string for numeric fields
    data["Open"]        = float(re.sub(r'[^\d.]', '', data["Open"]))
    data["High"]        = float(re.sub(r'[^\d.]', '', data["High"]))
    data["Low"]         = float(re.sub(r'[^\d.]', '', data["Low"]))
    data["Close"]       = float(re.sub(r'[^\d.]', '', data["Close"]))
    data["Adj Close"]   = float(re.sub(r'[^\d.]', '', data["Adj Close"]))
    data["Volume"]      = float(re.sub(r'[^\d.]', '', data["Volume"]))
    
    # Parse the "Date" field
    date_val = datetime.datetime.strptime(data["Date"], "%b %d, %Y")

    # If the "Time" field is present, parse it and add it to the "Date"
    if "Time" in data:
        time_val = datetime.datetime.strptime(data["Time"], "%H:%M:%S").time()
        date_val = datetime.datetime.combine(date_val, time_val)

    # Update the "Date" field in the data dictionary
    data["Date"] = date_val

    return data


def read_clean_scraped_data(topicName, collectionName) : 

    consumer ,company = consume_kafka_data(topicName, collectionName)

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
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Read and clean scraped data from Kafka.')

    # Add a command line argument for 'string'
    parser.add_argument('--topicName', help='Specify the topic name')
    parser.add_argument('--collectionName', help='Specify the collection name')

    # Parse the command line arguments
    args = parser.parse_args()

    # Call your function with the 'string' argument from the command line
    read_clean_scraped_data(args.topicName, args.collectionName)

