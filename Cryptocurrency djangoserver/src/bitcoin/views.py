from asyncio.windows_events import NULL
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
import pandas as pd
import numpy as np
import itertools
from binance.views import BnbDataFrame, BnbValues
from ethereum.views import EthDataFrame,EthValues
from xrp.views import XrpDataFrame,XrpValues
from aave.views import AaveDataFrame, AaveValues
from ada.views import AdaDataFrame, AdaValues
from bch.views import BchDataFrame, BchValues
from doge.views import DogeDataFrame, DogeValues
from dot.views import DotDataFrame, DotValues
from trx.views import TrxDataFrame, TrxValues
from .serializers import *
from .models import Bitcoin
from .search import search,search2,search3
from rest_framework import routers, serializers, viewsets
# Create your views here.

def BtcValues() :
    response    = search2()
    btc_date    = list()
    btc_open    = list()
    btc_close   = list()
    btc_high    = list()
    btc_low     = list()
    my_list     = list()

    for r in response :
        btc_date.append(r.Date)
        btc_open.append(r.Open)
        btc_high.append(r.High)
        btc_low.append(r.Low)
        btc_close.append(r.Close)
    
    # Sort all lists based on dates
    sorted_indices = sorted(range(len(btc_date)), key=lambda i: btc_date[i])
    btc_date = [btc_date[i] for i in sorted_indices]
    btc_open = [btc_open[i] for i in sorted_indices]
    btc_close = [btc_close[i] for i in sorted_indices]
    btc_high = [btc_high[i] for i in sorted_indices]
    btc_low = [btc_low[i] for i in sorted_indices]
    
    my_list.append(btc_open)
    my_list.append(btc_high)
    my_list.append(btc_low)
    my_list.append(btc_close)

    return my_list,btc_date

def BtcDataFrame() : 
    result = search2()
    df = pd.DataFrame([{'id':r.meta.id, **r.to_dict()} for r in result])
    df.set_index(['Date'],inplace = True)

    # Select only the specified columns
    features = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df = df.loc[:, features]  # Select only the specified columns
    df = df.sort_index(level='Date')
    return df
