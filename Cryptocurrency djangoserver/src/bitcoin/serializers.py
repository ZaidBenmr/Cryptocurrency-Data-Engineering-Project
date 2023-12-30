from .models import Bitcoin
import decimal
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class BitcoinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bitcoin
        fields = (
            'id',
            'date',
            'open',
            'high',
            'low',
            'close',
            'volume'
        )

class Geeks(object):
    def __init__(self, integers):
        self.integers = integers

class Geeks2(object):
    def __init__(self, btc,bnb,eth,xrp,aave,ada,bch,doge,dot,trx,
                 btc_dates,bnb_dates,eth_dates,xrp_dates,aave_dates,ada_dates,bch_dates,doge_dates,dot_dates,trx_dates):
        self.btc = btc
        self.bnb = bnb
        self.eth = eth
        self.xrp = xrp
        self.aave = aave
        self.ada = ada
        self.bch = bch
        self.doge = doge
        self.dot = dot
        self.trx = trx
        self.btc_dates = btc_dates
        self.bnb_dates = bnb_dates
        self.eth_dates = eth_dates
        self.xrp_dates = xrp_dates
        self.aave_dates = aave_dates
        self.ada_dates = ada_dates
        self.bch_dates = bch_dates
        self.doge_dates = doge_dates
        self.dot_dates = dot_dates
        self.trx_dates = trx_dates


class GeeksSerializer(serializers.Serializer):
    integers = serializers.ListField(
    child = serializers.IntegerField(min_value = 0, max_value = 400)
    )


class mySerializer(serializers.Serializer):
    btc = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=10, decimal_places=2)
    )
    )
    bnb = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=10, decimal_places=2)
    )
    )
    eth = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=10, decimal_places=2)
    )
    )
    xrp = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=10, decimal_places=2)
    )
    )

    aave = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=10, decimal_places=2)
    )
    )

    ada = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=10, decimal_places=2)
    )
    )

    bch = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=10, decimal_places=2)
    )
    )

    doge = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=10, decimal_places=2)
    )
    )

    dot = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=10, decimal_places=2)
    )
    )

    trx = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=10, decimal_places=2)
    )
    )

    btc_dates = serializers.ListField(
        child = serializers.DateTimeField()
    )

    bnb_dates = serializers.ListField(
        child = serializers.DateTimeField()
    )

    eth_dates = serializers.ListField(
        child = serializers.DateTimeField()
    )

    xrp_dates = serializers.ListField(
        child = serializers.DateTimeField()
    )

    aave_dates = serializers.ListField(
        child = serializers.DateTimeField()
    )

    ada_dates = serializers.ListField(
        child = serializers.DateTimeField()
    )

    bch_dates = serializers.ListField(
        child = serializers.DateTimeField()
    )

    doge_dates = serializers.ListField(
        child = serializers.DateTimeField()
    )

    dot_dates = serializers.ListField(
        child = serializers.DateTimeField()
    )

    trx_dates = serializers.ListField(
        child = serializers.DateTimeField()
    )


class ReturnObj(object):
    def __init__(self, doubles,cumreturns_list):
        self.doubles = doubles
        self.cumreturns = cumreturns_list


class ReturnsSerializer(serializers.Serializer) : 
    doubles = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=10, decimal_places=6)
    )
    )
    cumreturns = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=20, decimal_places=6)
    )
    )

class VolatiltyObj(object):
    def __init__(self, std):
        self.std = std

class VolatiltySerializer(serializers.Serializer):
    std = serializers.ListField(
    child = serializers.DecimalField(max_digits=10, decimal_places=6)
    )

class CorrObj(object) : 
    def __init__(self, corr):
        self.corr = corr


class CorrSerializer(serializers.Serializer) : 
    corr = serializers.ListField(
    child = serializers.ListField(
        child = serializers.DecimalField(max_digits=20, decimal_places=16)
    )
    )

class MLPredObj(object):
    def __init__(self, values,dates):
        self.values = values
        self.dates = dates

class DLPredSerializer(serializers.Serializer) : 
    values = serializers.ListField(
        child = serializers.DecimalField(max_digits=20, decimal_places=6)
    )
    dates = serializers.ListField(
        child = serializers.DateTimeField()
    )

class InputDataSerializer(serializers.Serializer):
    input_string = serializers.CharField(max_length=100)