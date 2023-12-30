from asyncio.windows_events import NULL
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
import pandas as pd
import numpy as np
import os
import joblib
from tensorflow.keras.models import load_model
from bitcoin.views import BtcDataFrame, BtcValues
from binance.views import BnbDataFrame, BnbValues
from ethereum.views import EthDataFrame,EthValues
from xrp.views import XrpDataFrame,XrpValues
from aave.views import AaveDataFrame, AaveValues
from ada.views import AdaDataFrame, AdaValues
from bch.views import BchDataFrame, BchValues
from doge.views import DogeDataFrame, DogeValues
from dot.views import DotDataFrame, DotValues
from trx.views import TrxDataFrame, TrxValues
from bitcoin.serializers import *
from bitcoin.models import Bitcoin
from bitcoin.search import search,search2,search3
from rest_framework import routers, serializers, viewsets
from django.http import HttpResponse
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
# Create your views here.

class AllcoinsVal(viewsets.ViewSet) :
    btcValues = BtcValues()
    bnbValues = BnbValues()
    ethValues = EthValues()
    xrpValues = XrpValues()
    aaveValues = AaveValues()
    adaValues = AdaValues()
    bchValues = BchValues()
    dogeValues = DogeValues()
    dotValues = DotValues()
    trxValues = TrxValues() 


    obj = Geeks2(btcValues[0],bnbValues[0],ethValues[0],xrpValues[0],aaveValues[0],adaValues[0],bchValues[0],dogeValues[0],dotValues[0],trxValues[0],
                 btcValues[1],bnbValues[1],ethValues[1],xrpValues[1],aaveValues[1],adaValues[1],bchValues[1],dogeValues[1],dotValues[1],trxValues[1])

    queryset = Bitcoin.objects.all()
    
    def list(self,request):
        serializer = mySerializer(self.obj)
        #print(self.btcValues)
        return Response(serializer.data)

# Visualisation Part
class CoinReturns2(viewsets.ViewSet) : 

    queryset = Bitcoin.objects.all()

    btc_df = BtcDataFrame()
    bnb_df = BnbDataFrame()
    eth_df = EthDataFrame()
    xrp_df = XrpDataFrame()
    aave_df = AaveDataFrame()
    ada_df = AdaDataFrame()
    bch_df = BchDataFrame()
    doge_df = DogeDataFrame()
    dot_df  = DotDataFrame()
    trx_df = TrxDataFrame()

    returns_list = list()
    cumreturns_list = list()

    return_btc  = btc_df["Close"].pct_change().dropna(axis=0)
    return_bnb  = bnb_df["Close"].pct_change().dropna(axis=0)
    return_eth  = eth_df["Close"].pct_change().dropna(axis=0)
    return_xrp  = xrp_df["Close"].pct_change().dropna(axis=0)
    return_aave = aave_df["Close"][1:].pct_change().dropna(axis=0)
    return_ada  = ada_df["Close"][1:].pct_change().dropna(axis=0)
    return_bch  = bch_df["Close"][1:].pct_change().dropna(axis=0)
    return_doge = doge_df["Close"][1:].pct_change().dropna(axis=0)
    return_dot  = dot_df["Close"][1:].pct_change().dropna(axis=0)
    return_trx  = trx_df["Close"][1:].pct_change().dropna(axis=0)

    returns_list.append(return_btc.values)
    returns_list.append(return_bnb.values)
    returns_list.append(return_eth.values)
    returns_list.append(return_xrp.values)
    returns_list.append(return_aave.values)
    returns_list.append(return_ada.values)
    returns_list.append(return_bch.values)
    returns_list.append(return_doge.values)
    returns_list.append(return_dot.values)
    returns_list.append(return_trx.values)
    #cumreturns_list.append((((1 + return_btc).cumprod() - 1) * 100).values)
    #cumreturns_list.append((((1 + return_bnb).cumprod() - 1) * 100).values)
    #cumreturns_list.append((((1 + return_eth).cumprod() - 1) * 100).values)
    #cumreturns_list.append((((1 + return_xrp).cumprod() - 1) * 100).values)
    '''
    merged_df = btc_df[["Close"]].merge(bnb_df[["Close"]], on="Date") \
                                    .merge(eth_df[["Close"]], on="Date") \
                                    .merge(xrp_df[["Close"]], on="Date") \
                                    .merge(aave_df[["Close"]], on="Date")
    merged_df.columns = ["BTC", "BNB", "ETH", "XRP", "AAVE"]
    
    returns = merged_df.pct_change().dropna(axis=0)
    cum_returns = ((1 + returns).cumprod() - 1) *100
    for item in list(returns.columns) : 
        cumreturns_list.append(list(cum_returns[item]))'''

    obj  = ReturnObj(returns_list,cumreturns_list)
    def list(self,request):
        serializer = ReturnsSerializer(self.obj)
        return Response(serializer.data)
    
'''
class CoinReturns(viewsets.ViewSet) :
    merged_df = MultiIndexDataFrame()
    adj_close = merged_df['Close']
    returns_list = list()
    cumreturns_list = list()

    returns = adj_close.pct_change().dropna(axis=0)
    cum_returns = ((1 + returns).cumprod() - 1) *100

    for item in list(returns.columns) : 
        returns_list.append(list(returns[item]))
        cumreturns_list.append(list(cum_returns[item]))

    obj  = ReturnObj(returns_list,cumreturns_list)
    queryset = Bitcoin.objects.all()
    def list(self,request):
        serializer = ReturnsSerializer(self.obj)
        return Response(serializer.data)
'''
class CoinCorrelations(viewsets.ViewSet) : 

    queryset = Bitcoin.objects.filter(id=1)

    btc_df = BtcDataFrame()
    bnb_df = BnbDataFrame()
    eth_df = EthDataFrame()
    xrp_df = XrpDataFrame()
    aave_df = AaveDataFrame()
    ada_df = AdaDataFrame()
    bch_df = BchDataFrame()
    doge_df = DogeDataFrame()
    dot_df  = DotDataFrame()
    trx_df = TrxDataFrame()
    corr_list = list()

    merged_df = btc_df[["Close"]].merge(bnb_df[["Close"]], on="Date") \
                                    .merge(eth_df[["Close"]], on="Date") \
                                    .merge(xrp_df[["Close"]], on="Date") \
                                    .merge(aave_df[["Close"]][1:], on="Date") \
                                    .merge(ada_df[["Close"]], on="Date") \
                                    .merge(bch_df[["Close"]], on="Date") \
                                    .merge(doge_df[["Close"]], on="Date") \
                                    .merge(dot_df[["Close"]], on="Date") \
                                    .merge(trx_df[["Close"]], on="Date") \
                                        
    merged_df.columns = ["BTC", "BNB", "ETH", "XRP", "AAVE","ADA","BCH","DOGE","DOT","TRX"]
    corr = merged_df.pct_change().dropna(axis=0).corr()

    for item in list(merged_df.columns) : 
        corr_list.append(list(corr[item]))

    obj  = CorrObj(corr_list)

    def list(self,request):
        serializer = CorrSerializer(self.obj)
        # print(self.corr_list)
        return Response(serializer.data)

class Volatilty(viewsets.ViewSet) :     
    queryset = Bitcoin.objects.all()

    btc_df = BtcDataFrame()
    bnb_df = BnbDataFrame()
    eth_df = EthDataFrame()
    xrp_df = XrpDataFrame()
    aave_df = AaveDataFrame()
    ada_df = AdaDataFrame()
    bch_df = BchDataFrame()
    doge_df = DogeDataFrame()
    dot_df  = DotDataFrame()
    trx_df = TrxDataFrame()
    vl_list = list()

    vl_btc  = btc_df["Close"].pct_change().dropna(axis=0).std()
    vl_bnb  = bnb_df["Close"].pct_change().dropna(axis=0).std()
    vl_eth  = eth_df["Close"].pct_change().dropna(axis=0).std()
    vl_xrp  = xrp_df["Close"].pct_change().dropna(axis=0).std()
    vl_aave = aave_df["Close"][1:].pct_change().dropna(axis=0).std()
    vl_ada  = ada_df["Close"].pct_change().dropna(axis=0).std()
    vl_bch  = bch_df["Close"].pct_change().dropna(axis=0).std()
    vl_doge = doge_df["Close"].pct_change().dropna(axis=0).std()
    vl_dot  = dot_df["Close"].pct_change().dropna(axis=0).std()
    vl_trx  = trx_df["Close"].pct_change().dropna(axis=0).std()

    vl_list.append(vl_btc)
    vl_list.append(vl_bnb)
    vl_list.append(vl_eth)
    vl_list.append(vl_xrp)
    vl_list.append(vl_aave)
    vl_list.append(vl_ada)
    vl_list.append(vl_bch)
    vl_list.append(vl_doge)
    vl_list.append(vl_dot)
    vl_list.append(vl_trx)

    obj = VolatiltyObj(vl_list)

    def list(self,request):
        serializer = VolatiltySerializer(self.obj)
        print(self.vl_list)
        return Response(serializer.data)
'''
class BuyAndHold(viewsets.ViewSet) : 

    merged_df = MultiIndexDataFrame()
    adj_close = merged_df['Close']
    bh_list = list()

    buyhold = adj_close.apply(lambda x: x / x[0])

    for item in list(adj_close.columns) : 
        bh_list.append(list(buyhold[item]))

    obj  = CorrObj(bh_list)
    queryset = Bitcoin.objects.filter(id=1)

    def list(self,request):
        serializer = CorrSerializer(self.obj)
        print(self.bh_list)
        return Response(serializer.data)
'''


class Predictions(viewsets.ViewSet) :
    #authentication_classes = [SessionAuthentication, BasicAuthentication]  # Add this line
    #permission_classes = [AllowAny]  # Add this line
    queryset = Bitcoin.objects.all()
    coin_df = BtcDataFrame()
    coin_name = "btc"

    
    def crypto_dataframe(self, input_string):
        #serializer = InputDataSerializer(data=request.data)
        #if serializer.is_valid():
            #input_string = serializer.validated_data['input_string']
            if input_string.lower() in ["btc", "bnb", "eth", "xrp", "bch", "dot", "doge", "aave", "ada", "trx"]:
                if input_string.lower() == "btc":
                    self.coin_df = BtcDataFrame()
                elif input_string.lower() == "bnb":
                    self.coin_df = BnbDataFrame()
                elif input_string.lower() == "eth":
                    self.coin_df = EthDataFrame()
                elif input_string.lower() == "xrp":
                    self.coin_df = XrpDataFrame()
                elif input_string.lower() == "bch":
                    self.coin_df = BchDataFrame()
                elif input_string.lower() == "aave":
                    self.coin_df = AaveDataFrame()
                elif input_string.lower() == "ada":
                    self.coin_df = AdaDataFrame()
                elif input_string.lower() == "dot":
                    self.coin_df = DotDataFrame()
                elif input_string.lower() == "doge":
                    self.coin_df = DogeDataFrame()
                elif input_string.lower() == "trx":
                    self.coin_df = TrxDataFrame()

                self.coin_name = input_string.lower()
            else:
                return Response("Crypto doesn't exist", status=status.HTTP_200_OK)

        #else:
        #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def dataset_generator_lstm2(data):
        dataset, coinname = data
        # multiple feature from data provided to the model
        backcandles=15
        X = []
        dataset = np.array(dataset)
        for i in range(backcandles, dataset.shape[0]):
            X.append(dataset[i-backcandles:i, 4])

        X = np.reshape(np.array(X), (np.array(X).shape[0], np.array(X).shape[1], 1 ))
        print(X[-1].reshape(-1, 1))
        return X[-1], coinname
    
    def scaler_X(data) : 
        array, coinname = data
        BASE_DIR     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DL_DIR  = os.path.join(BASE_DIR, 'Deep_learning_models')
        print(coinname)
        # Importing Min-Max Scaler
        path_scaler_x = os.path.join(DL_DIR, f"scaler_x_{coinname}.joblib")
        print(path_scaler_x)
        scaler_x = joblib.load(path_scaler_x)
        scaled_array = scaler_x.transform(array.reshape(-1, 1))
        print(scaled_array)
        return scaled_array, coinname

    def forecasting_model(data) :
        scaled_array, coinname = data
        BASE_DIR     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DL_DIR  = os.path.join(BASE_DIR, 'Deep_learning_models')

        # Importing LSTM Model
        path_model = os.path.join(DL_DIR, f"model_{coinname}.h5")
        model   = load_model(path_model)
        print(path_model)

        # Make predictions for future values
        predictions = []
        current_sequence = scaled_array
        for i in range(120):
            predicted_value = model.predict(current_sequence.reshape(1, 15, 1))
            predictions.append(predicted_value[0, 0])
            current_sequence = np.concatenate((current_sequence[1:], predicted_value), axis=None)
        print(np.array(predictions).reshape(-1, 1))
        return np.array(predictions).reshape(-1, 1), coinname
    
    def scaler_Y(data) : 
        predictions, coinname = data
        BASE_DIR     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DL_DIR  = os.path.join(BASE_DIR, 'Deep_learning_models')

        # Importing Min-Max Scaler
        path_scaler_y = os.path.join(DL_DIR, f"scaler_y_{coinname}.joblib")
        scaler_y = joblib.load(path_scaler_y)
    
        predicted_values = scaler_y.inverse_transform(predictions)
        print(predicted_values)
        return predicted_values

    
    pipeline = Pipeline(steps=[
    ('Data generation for LSTM Model', FunctionTransformer(dataset_generator_lstm2)),
    ('Normlisation of input data', FunctionTransformer(scaler_X)),
    ('Closing price forecasting', FunctionTransformer(forecasting_model)),
    ('Denormalization of future predictions', FunctionTransformer(scaler_Y))
    ])

    #predicted_values = pipeline.transform(coin_df).flatten().tolist()

    #obj = MLPredObj(predicted_values, dates)

    def retrieve(self, request, pk=None):
        self.crypto_dataframe(pk)

        # Prepare dates for the future predictions
        dates = pd.date_range(start=self.coin_df.index[-1], periods=120+1, freq='D')[1:]

        predicted_values = self.pipeline.transform((self.coin_df, self.coin_name)).flatten().tolist()

        obj = MLPredObj(predicted_values, dates)
        serializer = DLPredSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)



def test () : 
    btc_df = BtcDataFrame()
    BASE_DIR     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DL_DIR  = os.path.join(BASE_DIR, 'Deep_learning_models')

    # Importing Min-Max Scalers
    path_scaler_x = os.path.join(DL_DIR, "scaler_x_btc.joblib")
    scaler_x = joblib.load(path_scaler_x)

    path_scaler_y = path = os.path.join(DL_DIR, "scaler_y_btc.joblib")
    scaler_y = joblib.load(path_scaler_y)

    # Importing LSTM Model
    path_model = os.path.join(DL_DIR, "model_btc.h5")
    model   = load_model(path_model)

    def dataset_generator_lstm2(dataset):
        # multiple feature from data provided to the model
        backcandles=15
        X = []
        dataset = np.array(dataset)
        for i in range(backcandles, dataset.shape[0]):
            X.append(dataset[i-backcandles:i, 4])
        
        X = np.reshape(np.array(X), (np.array(X).shape[0], np.array(X).shape[1], 1))
        return X[-1].reshape(-1, 1)
    
    def scaler_X(array) : 

        scaled_array = scaler_x.transform(array)

        return scaled_array

    def forecasting_model(scaled_array) : 
        # Make predictions for future values
        predictions = []
        current_sequence = scaled_array
        for i in range(120):
            predicted_value = model.predict(current_sequence.reshape(1, 15, 1))
            predictions.append(predicted_value[0, 0])
            current_sequence = np.concatenate((current_sequence[1:], predicted_value), axis=None)

        return np.array(predictions).reshape(-1, 1)
    
    def scaler_Y(predictions) : 

        predicted_values = scaler_y.inverse_transform(predictions)

        return predicted_values

    # Prepare dates for the future predictions
    dates = pd.date_range(start=btc_df.index[-1], periods=120+1, freq='D')[1:]

    pipeline = Pipeline(steps=[
    ('Data generation for LSTM Model', FunctionTransformer(dataset_generator_lstm2)),
    ('Normlisation of input data', FunctionTransformer(scaler_X)),
    ('Closing price forecasting', FunctionTransformer(forecasting_model)),
    ('Denormalization of future predictions', FunctionTransformer(scaler_Y))
    ])

    predicted_values = pipeline.transform(btc_df)

    return predicted_values, dates