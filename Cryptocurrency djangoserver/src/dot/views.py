from django.shortcuts import render
from .search import search,search2,search3
import pandas as pd

# Create your views here.

def DotValues() :
    response = search2()
    dot_date = list()
    dot_open = list()
    dot_close = list()
    dot_high = list()
    dot_low = list()
    my_list = list()

    for r in response :
        dot_date.append(r.Date)
        dot_open.append(r.Open)
        dot_high.append(r.High)
        dot_low.append(r.Low)
        dot_close.append(r.Close)

    # Sort all lists based on dates
    sorted_indices = sorted(range(len(dot_date)), key=lambda i: dot_date[i])
    dot_date = [dot_date[i] for i in sorted_indices]
    dot_open = [dot_open[i] for i in sorted_indices]
    dot_close = [dot_close[i] for i in sorted_indices]
    dot_high = [dot_high[i] for i in sorted_indices]
    dot_low = [dot_low[i] for i in sorted_indices]
    
    my_list.append(dot_open)
    my_list.append(dot_high)
    my_list.append(dot_low)
    my_list.append(dot_close)

    return my_list,dot_date


def DotDataFrame() : 
    result = search2()
    df = pd.DataFrame([{'id':r.meta.id, **r.to_dict()} for r in result])
    df.set_index(['Date'],inplace = True)

    # Select only the specified columns
    features = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df = df.loc[:, features]  # Select only the specified columns
    df = df.sort_index(level='Date')
    return df

