from django.shortcuts import render
from .search import search,search2,search3
import pandas as pd

# Create your views here.


def DogeValues() :
    response = search2()
    doge_date = list()
    doge_open = list()
    doge_close = list()
    doge_high = list()
    doge_low = list()
    my_list = list()

    for r in response :
        doge_date.append(r.Date)
        doge_open.append(r.Open)
        doge_high.append(r.High)
        doge_low.append(r.Low)
        doge_close.append(r.Close)

    # Sort all lists based on dates
    sorted_indices = sorted(range(len(doge_date)), key=lambda i: doge_date[i])
    doge_date = [doge_date[i] for i in sorted_indices]
    doge_open = [doge_open[i] for i in sorted_indices]
    doge_close = [doge_close[i] for i in sorted_indices]
    doge_high = [doge_high[i] for i in sorted_indices]
    doge_low = [doge_low[i] for i in sorted_indices]
    
    my_list.append(doge_open)
    my_list.append(doge_high)
    my_list.append(doge_low)
    my_list.append(doge_close)

    return my_list,doge_date


def DogeDataFrame() : 
    result = search2()
    df = pd.DataFrame([{'id':r.meta.id, **r.to_dict()} for r in result])
    df.set_index(['Date'],inplace = True)

    # Select only the specified columns
    features = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df = df.loc[:, features]  # Select only the specified columns
    df = df.sort_index(level='Date')
    return df

