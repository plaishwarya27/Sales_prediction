from socket import fromfd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt1
import seaborn as sns
import datetime
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.ensemble import RandomForestRegressor

def randomForestRegressor(file,name,fromDate,toDate):
    def bar():
        #print("Working")
        N = len(new_date)
        act =df_preds['actual_sale']
        pre = df_preds['pred_sale']
        ind = np.arange(N)
        plt1.figure(figsize=(10,5))
        width = 0.3
        plt1.bar(ind, act , width, label='Actual Values')
        plt1.bar(ind + width, pre, width, label='Predicted Values')
        plt1.xlabel('Date')
        plt1.ylabel('Sales')
        plt1.title('Bar-Predicted Image')
        plt1.xticks(ind + width / 2, df_preds['date'],rotation=90)
        plt1.legend(loc='best')
        plt1.savefig('barForest.png')
    def pie():
        r2=int(r2_score(new_date['sales'],rfr_preds)*100)
        val=np.array([r2,100-r2])
        plt1.pie(val,labels=['R2_score','Error'])
        plt1.savefig('pieForest.png')

    df=pd.read_csv(file)
    #print(fromDate," ",toDate)
    df['date']=pd.to_datetime(df['date'])
    df['ordinal']=df['date'].map(datetime.datetime.toordinal)
    X=df['ordinal'].values.reshape(-1,1)
    y=df['sales']
    start=pd.to_datetime(fromDate)
    end=pd.to_datetime(toDate)
    new_date=df[(df['date']>=start) & (df['date']<=end)]
    rfr=RandomForestRegressor()
    rfr.fit(X,y)
    rfr_preds=rfr.predict(new_date['ordinal'].values.reshape(-1,1))
    df_preds=pd.DataFrame(np.array([rfr_preds,np.array(new_date['sales'])]).transpose(),columns=['pred_sale','actual_sale'])
    df_preds['date']=np.array(new_date['date'])
    df_preds['date']=df['date'].dt.strftime('%m/%Y')
    plt1.scatter(x=df_preds['date'], y=df_preds['actual_sale'],label='Actual Sales')
    plt1.plot(df_preds['date'],df_preds['actual_sale'])
    plt1.text(1,850,"Actual Values")
    plt1.savefig('out1.png')
    plt1.scatter(x=df_preds['date'],y=df_preds['pred_sale'],label='Predicted Sales')
    plt1.plot(df_preds['date'],df_preds['pred_sale'])
    plt1.ylabel("Sales")
    plt1.xticks(rotation=90)
    plt1.legend(bbox_to_anchor=(1,1))
    df_preds.to_csv('raw_data.csv',index=False)
    plt1.text(1,850,"Accuracy Score: "+str(r2_score(new_date['sales'],rfr_preds)),fontsize=12)
    plt1.savefig(name)
    pie()
    bar()
    #r2_score(new_date['sales'],rfr_preds)#r2_score or Accuracy
    #mean_squared_error(new_date['sales'],rfr_preds)**0.5
    #mean_absolute_error(new_date['sales'],rfr_preds)

#randomForestRegressor("raw_data.csv","sales.png","01-1966","01-1968")