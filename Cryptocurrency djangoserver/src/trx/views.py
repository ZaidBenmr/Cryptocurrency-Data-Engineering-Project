from django.shortcuts import render
from .search import search,search2,search3
import pandas as pd

# Create your views here.


def TrxValues() :
    response = search2()
    trx_date = list()
    trx_open = list()
    trx_close = list()
    trx_high = list()
    trx_low = list()
    my_list = list()
    
    for r in response :
        trx_date.append(r.Date)
        trx_open.append(r.Open)
        trx_high.append(r.High)
        trx_low.append(r.Low)
        trx_close.append(r.Close)

    # Sort all lists based on dates
    sorted_indices = sorted(range(len(trx_date)), key=lambda i: trx_date[i])
    trx_date = [trx_date[i] for i in sorted_indices]
    trx_open = [trx_open[i] for i in sorted_indices]
    trx_close = [trx_close[i] for i in sorted_indices]
    trx_high = [trx_high[i] for i in sorted_indices]
    trx_low = [trx_low[i] for i in sorted_indices]
    
    my_list.append(trx_open)
    my_list.append(trx_high)
    my_list.append(trx_low)
    my_list.append(trx_close)

    return my_list,trx_date


def TrxDataFrame() : 
    result = search2()
    df = pd.DataFrame([{'id':r.meta.id, **r.to_dict()} for r in result])
    df.set_index(['Date'],inplace = True)

    # Select only the specified columns
    features = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df = df.loc[:, features]  # Select only the specified columns
    df = df.sort_index(level='Date')
    return df

