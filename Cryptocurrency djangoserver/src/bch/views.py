from django.shortcuts import render
from .search import search,search2,search3
import pandas as pd

# Create your views here.


def BchValues() :
    response = search2()
    bch_date = list()
    bch_open = list()
    bch_close = list()
    bch_high = list()
    bch_low = list()
    my_list = list()

    for r in response :
        bch_date.append(r.Date)
        bch_open.append(r.Open)
        bch_high.append(r.High)
        bch_low.append(r.Low)
        bch_close.append(r.Close)

    # Sort all lists based on dates
    sorted_indices = sorted(range(len(bch_date)), key=lambda i: bch_date[i])
    bch_date = [bch_date[i] for i in sorted_indices]
    bch_open = [bch_open[i] for i in sorted_indices]
    bch_close = [bch_close[i] for i in sorted_indices]
    bch_high = [bch_high[i] for i in sorted_indices]
    bch_low = [bch_low[i] for i in sorted_indices]
    
    my_list.append(bch_open)
    my_list.append(bch_high)
    my_list.append(bch_low)
    my_list.append(bch_close)

    return my_list,bch_date


def BchDataFrame() : 
    result = search2()
    df = pd.DataFrame([{'id':r.meta.id, **r.to_dict()} for r in result])
    df.set_index(['Date'],inplace = True)

    # Select only the specified columns
    features = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df = df.loc[:, features]  # Select only the specified columns
    df = df.sort_index(level='Date')
    return df

