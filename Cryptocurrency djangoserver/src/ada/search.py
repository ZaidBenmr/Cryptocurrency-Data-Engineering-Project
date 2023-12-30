from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Date, Search, Double
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

# Create a connection to ElasticSearch
connections.create_connection()

class AdaIndex(Document):
    date       = Date()
    open       = Double()
    high       = Double()
    low        = Double()
    close      = Double()
    volume     = Double()
    market_cap = Double()
    class Index:
      name = 'ada_cleaned'

# Bulk indexing function, run in shell
def bulk_indexing():
    AdaIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Ada.objects.all().iterator()))

# Simple search function
def search(id):
    s = Search(index='ada_cleaned').filter('term', id=id)
    response = s.execute()
    return response

def search2():
    s = Search(index='ada_cleaned')
    response = s.scan()
    return response

def search3():
    s = Search(index='ada_cleaned').extra(size=1000)
    #s = s[0:s.count()]
    response = s.execute()
    return response