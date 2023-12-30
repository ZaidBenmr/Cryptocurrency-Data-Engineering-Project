from django.shortcuts import render
from .search import search2,search3
import pandas as pd
# Create your views here.


def XrpValues() :
    response = search2()
    xrp_date = list()
    xrp_open = list()
    xrp_close = list()
    xrp_high = list()
    xrp_low = list()
    my_list = list()

    for r in response :
        xrp_date.append(r.Date)
        xrp_open.append(r.Open)
        xrp_high.append(r.High)
        xrp_low.append(r.Low)
        xrp_close.append(r.Close)

    # Sort all lists based on dates
    sorted_indices = sorted(range(len(xrp_date)), key=lambda i: xrp_date[i])
    xrp_date = [xrp_date[i] for i in sorted_indices]
    xrp_open = [xrp_open[i] for i in sorted_indices]
    xrp_close = [xrp_close[i] for i in sorted_indices]
    xrp_high = [xrp_high[i] for i in sorted_indices]
    xrp_low = [xrp_low[i] for i in sorted_indices]
    
    
    my_list.append(xrp_open)
    my_list.append(xrp_high)
    my_list.append(xrp_low)
    my_list.append(xrp_close)

    return my_list,xrp_date

def XrpDataFrame() : 
    result = search2()
    df = pd.DataFrame([{'id':r.meta.id, **r.to_dict()} for r in result])
    df.set_index(['Date'],inplace = True)

    # Select only the specified columns
    features = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df = df.loc[:, features]  # Select only the specified columns
    df = df.sort_index(level='Date')
    return df