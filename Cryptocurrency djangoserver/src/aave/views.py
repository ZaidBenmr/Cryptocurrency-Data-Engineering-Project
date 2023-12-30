from django.shortcuts import render
from .search import search,search2,search3
import pandas as pd

# Create your views here.


def AaveValues() :
    response = search2()
    aave_date = list()
    aave_open = list()
    aave_close = list()
    aave_high = list()
    aave_low = list()
    my_list = list()
    
    for r in response :
        aave_date.append(r.Date)
        aave_open.append(r.Open)
        aave_high.append(r.High)
        aave_low.append(r.Low)
        aave_close.append(r.Close)

    # Sort all lists based on dates
    sorted_indices = sorted(range(len(aave_date)), key=lambda i: aave_date[i])
    aave_date = [aave_date[i] for i in sorted_indices]
    aave_open = [aave_open[i] for i in sorted_indices]
    aave_close = [aave_close[i] for i in sorted_indices]
    aave_high = [aave_high[i] for i in sorted_indices]
    aave_low = [aave_low[i] for i in sorted_indices]
    
    my_list.append(aave_open)
    my_list.append(aave_high)
    my_list.append(aave_low)
    my_list.append(aave_close)

    return my_list,aave_date


def AaveDataFrame() : 
    result = search2()
    df = pd.DataFrame([{'id':r.meta.id, **r.to_dict()} for r in result])
    df.set_index(['Date'],inplace = True)

    # Select only the specified columns
    features = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df = df.loc[:, features]  # Select only the specified columns
    df = df.sort_index(level='Date')
    return df

