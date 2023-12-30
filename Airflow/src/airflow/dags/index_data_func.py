from pymongo import MongoClient
from elasticsearch import Elasticsearch
import json

def index_data(collectionName, indexName) :

    # MongoDB connection settings
    mongo_host = "192.168.11.108"
    mongo_port = 27017
    mongo_db_name = "cryptocurrencies"
    mongo_collection_name = collectionName

    # Elasticsearch connection settings
    es_host = "192.168.11.108"
    es_port = 9200
    es_index = indexName  # Choose your Elasticsearch index name

    # Connect to MongoDB
    mongo_client = MongoClient(f"mongodb://{mongo_host}:{mongo_port}")
    mongo_db = mongo_client[mongo_db_name]
    mongo_collection = mongo_db[mongo_collection_name]

    # Connect to Elasticsearch
    es = Elasticsearch([f"http://{es_host}:{es_port}"])

    # Query the data from MongoDB and index it in Elasticsearch
    for document in mongo_collection.find().sort("datetime", -1).limit(100):
        # Convert MongoDB document to a JSON-serializable format
        document_json = json.loads(json.dumps(document, default=str))

        # Remove the _id field from the document
        if '_id' in document_json:
            del document_json['_id']

        # Index the document in Elasticsearch
        es.index(index=es_index, document=document_json)
        #print(document)
    # Close the MongoDB and Elasticsearch connections
    mongo_client.close()

    print(f"Data from MongoDB has been indexed into Elasticsearch index '{es_index}'")
