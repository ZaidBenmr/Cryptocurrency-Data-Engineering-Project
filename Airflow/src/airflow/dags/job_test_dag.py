from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from confluent_kafka import Consumer, KafkaError
from pymongo import MongoClient
import json
import re


# Define your Job 2 function (listening to Kafka and performing ETL)
def job_2():
    def consume_kafka_data() :
        consumer_config = {
        'bootstrap.servers': 'localhost:9092',  # Kafka broker(s)
        'group.id': 'my-consumer',              # Consumer group ID
        'auto.offset.reset': 'earliest'         # Read messages from the beginning of the topic
        }

        consumer = Consumer(consumer_config)
        consumer.subscribe(['cryptobalance'])

        # Making a Connection with MongoClient
        client = MongoClient("mongodb://localhost:27017/")
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
        
        data["datetime"] = datetime.strptime(data["datetime"], "%Y-%m-%d %H:%M:%S")

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

    read_clean_scraped_data()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 3),  # Replace with your start date
    'retries': 1,
    'retry_delay': timedelta(minutes=5),  # Adjust as needed
}

dag_2 = DAG(
    'test_dag',
    default_args=default_args,
    description='DAG for Crypto ETL Job 2',
    schedule_interval=None,  # Job 1 will run every 5 seconds
    catchup=False,  # Prevent backfilling
)



job_2_task = PythonOperator(
    task_id='job_2',
    python_callable=job_2,
    dag=dag_2,
)

job_2_task