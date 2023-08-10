from fileinput import filename
from unicodedata import name
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import autocorrelation_plot
from pandas.tseries.offsets import DateOffset
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import r2_score

def worker_code(file,name,fromDate,toDate):
    def adfuller_test(sales):
        result=adfuller(sales)
        labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
        for value,label in zip(result,labels):
            print(label+' : '+str(value) )
        if result[1] <= 0.05:
            print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary")
        else:
            print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")

    df=pd.read_csv(file)
    df.columns=["Month","Sales"]
    df.dropna(how='any', inplace=True)
    df['Month']=pd.to_datetime(df['Month'])
    df.set_index('Month',inplace=True)
    df.plot()
    #adfuller_test(df['Sales'])
    df['Seasonal_First_Difference']=df['Sales']-df['Sales'].shift(12)
    #adfuller_test(df['Seasonal_First_Difference'].dropna())
    df['Seasonal_First_Difference'].dropna()
    df['Seasonal_First_Difference'].plot()
    model=sm.tsa.statespace.SARIMAX(df['Sales'],order=(1, 1, 1),seasonal_order=(1,1,1,12))
    results=model.fit()
    df['forecast']=results.predict(start=fromDate,end=toDate,dynamic=True)
    df[['Sales','forecast']].plot(figsize=(12,8))
    df.to_csv('ss_data.csv')
    plt.savefig(name)
    x=list(df['Sales'].dropna())
    y=list(df['forecast'].dropna());z=[]
    for i in list(df.index):
        z.append(str(i).split()[0])
    temp=fromDate[3:]+'-'+fromDate[:2]+'-01'
    print(z.index(temp))
    return [x,y,z,z.index(temp)]


