from django.shortcuts import render
from .search import search2,search3
import pandas as pd
# Create your views here.


def EthValues() :
    response = search2()
    eth_date = list()
    eth_open = list()
    eth_close = list()
    eth_high = list()
    eth_low = list()
    my_list = list()

    for r in response :
        eth_date.append(r.Date)
        eth_open.append(r.Open)
        eth_high.append(r.High)
        eth_low.append(r.Low)
        eth_close.append(r.Close)

    # Sort all lists based on dates
    sorted_indices = sorted(range(len(eth_date)), key=lambda i: eth_date[i])
    eth_date = [eth_date[i] for i in sorted_indices]
    eth_open = [eth_open[i] for i in sorted_indices]
    eth_close = [eth_close[i] for i in sorted_indices]
    eth_high = [eth_high[i] for i in sorted_indices]
    eth_low = [eth_low[i] for i in sorted_indices]
    
    my_list.append(eth_open)
    my_list.append(eth_high)
    my_list.append(eth_low)
    my_list.append(eth_close)

    return my_list,eth_date

def EthDataFrame() : 
    result = search2()
    df = pd.DataFrame([{'id':r.meta.id, **r.to_dict()} for r in result])
    df.set_index(['Date'],inplace = True)

    # Select only the specified columns
    features = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df = df.loc[:, features]  # Select only the specified columns
    df = df.sort_index(level='Date')
    return df