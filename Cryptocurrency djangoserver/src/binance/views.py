from django.shortcuts import render
from .search import search,search2,search3
import pandas as pd
from rest_framework import routers, serializers, viewsets
# Create your views here.


def BnbValues() :
    response = search2()
    bnb_date = list()
    bnb_open = list()
    bnb_close = list()
    bnb_high = list()
    bnb_low = list()
    my_list = list()

    for r in response :
        bnb_date.append(r.Date)
        bnb_open.append(r.Open)
        bnb_high.append(r.High)
        bnb_low.append(r.Low)
        bnb_close.append(r.Close)

    # Sort all lists based on dates
    sorted_indices = sorted(range(len(bnb_date)), key=lambda i: bnb_date[i])
    bnb_date = [bnb_date[i] for i in sorted_indices]
    bnb_open = [bnb_open[i] for i in sorted_indices]
    bnb_close = [bnb_close[i] for i in sorted_indices]
    bnb_high = [bnb_high[i] for i in sorted_indices]
    bnb_low = [bnb_low[i] for i in sorted_indices]
    
    my_list.append(bnb_open)
    my_list.append(bnb_high)
    my_list.append(bnb_low)
    my_list.append(bnb_close)

    return my_list,bnb_date

def BnbDataFrame() : 
    result = search2()
    df = pd.DataFrame([{'id':r.meta.id, **r.to_dict()} for r in result])
    df.set_index(['Date'],inplace = True)

    # Select only the specified columns
    features = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df = df.loc[:, features]  # Select only the specified columns
    df = df.sort_index(level='Date')
    return df