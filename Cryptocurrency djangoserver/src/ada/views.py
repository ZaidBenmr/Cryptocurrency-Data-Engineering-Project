from django.shortcuts import render
from .search import search,search2,search3
import pandas as pd

# Create your views here.


def AdaValues() :
    response = search2()
    ada_date = list()
    ada_open = list()
    ada_close = list()
    ada_high = list()
    ada_low = list()
    my_list = list()

    for r in response :
        ada_date.append(r.Date)
        ada_open.append(r.Open)
        ada_high.append(r.High)
        ada_low.append(r.Low)
        ada_close.append(r.Close)

    # Sort all lists based on dates
    sorted_indices = sorted(range(len(ada_date)), key=lambda i: ada_date[i])
    ada_date = [ada_date[i] for i in sorted_indices]
    ada_open = [ada_open[i] for i in sorted_indices]
    ada_close = [ada_close[i] for i in sorted_indices]
    ada_high = [ada_high[i] for i in sorted_indices]
    ada_low = [ada_low[i] for i in sorted_indices]
    
    my_list.append(ada_open)
    my_list.append(ada_high)
    my_list.append(ada_low)
    my_list.append(ada_close)

    return my_list,ada_date


def AdaDataFrame() : 
    result = search2()
    df = pd.DataFrame([{'id':r.meta.id, **r.to_dict()} for r in result])
    df.set_index(['Date'],inplace = True)

    # Select only the specified columns
    features = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df = df.loc[:, features]  # Select only the specified columns
    df = df.sort_index(level='Date')
    return df

