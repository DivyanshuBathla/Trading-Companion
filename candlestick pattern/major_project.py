
import pandas as pd
import numpy as np
import pandas_datareader as pdr

import yfinance as yfin
from pandas_datareader import data as pdr



symbol=pd.read_csv('EQUITY_L (3).csv')

symbol.head()

symbol=np.array(symbol)

type(symbol[0][0])

string=symbol[0][0]

string

import datetime as dt
x=dt.date.today()
x=x-dt.timedelta(1)
y=x-dt.timedelta(120)



# len(df)

x

(symbol.shape)[0]

def reverse_hammer(data,i):

    open_close=(data[i][3]-data[i][4])/data[i][3]*100
    open_close=abs(open_close)

    low=(data[i][2]-data[i][3])/data[i][2]*100
    low=abs(low)
    high=(data[i][1]-data[i][4])/data[i][1]*100
    high=abs(high)
    # print(open_close," ",high," ",low)
    if(open_close*3<high and low*3<high):
        #print(data[i][0])
        return(1)
    return(-1)

def hammer(data,i):

    open_close=(data[i][3]-data[i][4])/data[i][3]*100
    open_close=abs(open_close)

    low=(data[i][2]-data[i][3])/data[i][2]*100
    low=abs(low)
    high=(data[i][1]-data[i][4])/data[i][1]*100
    high=abs(high)
    # print(open_close," ",high," ",low)
    if(open_close*3<low and high*3<low):
        #print(data[i][0])
        return(1)
    return(-1)

def harebozo(data,i):

    open_close=(data[i][3]-data[i][4])/data[i][3]*100
    open_close=abs(open_close)

    low=(data[i][2]-data[i][3])/data[i][2]*100
    low=abs(low)
    high=(data[i][1]-data[i][4])/data[i][1]*100
    high=abs(high)
    # print(open_close," ",high," ",low)
    high_low=(data[i][1]-data[i][2])/data[i][1]*100
    high_low=abs(high_low)
    if((open_close>high*4 and open_close>low*4) or (open_close>high*5 and data[i][3]>data[i][1]) or(open_close>low*5 and data[i][4]>data[i][2]) ):

        #print(data[i][0])
        return(1)
    return(-1)

def spin_top(data,i):

    open_close=(data[i][3]-data[i][4])/data[i][3]*100
    open_close=abs(open_close)

    low=(data[i][2]-data[i][3])/data[i][2]*100
    low=abs(low)
    high=(data[i][1]-data[i][4])/data[i][1]*100
    high=abs(high)
    # print(open_close," ",high," ",low)

    if(low>5*open_close and high>5*open_close and abs(high-low)<0.5):
        #print(data[i][0])
        return(1)
    return(-1)

def twezzer_bottom(data,i):
    diff_low=(data[i-1][3]-data[i][3])
    per_chan=diff_low/data[i-1][3]*100
    per_chan=abs(per_chan)
    if(per_chan<1 and func(data,i)<0):
      return(1)
    else:
      return(-1)

def func(data,curr):
    temp=curr
    dec=0
    inc=0
    while(curr>temp-5):
        if(data[curr][4]<data[curr-1][4]):
            dec=dec+1
        else:
            inc=inc+1
        curr=curr-1
    return(dec-inc)

def check_pattern(data,i):

      if(hammer(data,i)==1 or reverse_hammer(data,i)==1 or spin_top(data,i)==1 or harebozo(data,i)==1):
      # if(twezzer_bottom(data,i)==1):
         if(func(data,i)>0):
             return(1)
         else:
             return(-1)
      return(0)

# def get_symbol(string,x,y):
#     try:
#         df=pdr.get_data_yahoo(string,start=x,end=y)
#         return df
#     except:
#         try:
#             df=pdr.get_data_yahoo(string+'.BO',start=x,end=y)
#             return df
#         except:
#             try:
#                 df=pdr.get_data_yahoo(string+'.NS',start=x,end=y)
#                 return df
#             except:
#                 df=pdr.get_data_yahoo('RELIANCE.NS',start=x,end=y)

def get_symbol(string,x,y):
    yfin.pdr_override()
    df1=pdr.get_data_yahoo(string,start=x,end=y)
    yfin.pdr_override()
    df2=pdr.get_data_yahoo(string+'.NS',start=x,end=y)
    yfin.pdr_override()
    df3=pdr.get_data_yahoo(string+'.BO',start=x,end=y)
    if(len(df1)!=0):
      df=df1
    elif len(df2)!=0:
      df=df2
    elif len(df3)!=0:
      df=df3
    return df

def piv_high(data,temp):
    count=0
    sum=0
    for i in range(temp-1,temp):
        sum=sum+data[i][1]
        count=count+1
    avg=sum/count
    return avg

def piv_close(data,temp):
    count=0
    sum=0
    for i in range(temp-1,temp):
        sum=sum+data[i][4]
        count=count+1
    avg=sum/count
    return avg

def piv_low(data,temp):
    count=0
    sum=0
    for i in range(temp-1,temp):
        sum=sum+data[i][2]
        count=count+1
    avg=sum/count
    return avg

file=open('suggest.txt','w')
file.close()

len(symbol)

file=open('suggest.txt','w')
i=720
result=[]
while(i<1200):
    try:
        print("Index=",i)
        string=symbol[i][0]
        df=get_symbol(string,y,x)
        df=df.reset_index()
        print(df.head(2))
        print("\n")
        data=np.array(df)
        temp=(df.shape)[0]-1
        if(temp<4):
            i=i+1
            continue
        check=check_pattern(data,temp-1)
        print("check=",check)
        print("i=",i)
        print("check=",check)
        if(check>0):
            file.write("Company name=")
            file.write(symbol[i][1])
            file.write("\n")
            file.write("Suggestion=Buy stock\n")
            # file.write("Entry price=")
            # avg=data[temp-1][1]
            # avg=avg+(avg*0.005)
            # file.write(str(round(avg,2)))
            # high=piv_high(data,temp-1)
            # low=piv_low(data,temp-1)
            # close=piv_close(data,temp-1)

            # pp=(high+low+close)/3
            # rr1=(2*pp)-low
            # target1=rr1
            # rr2=pp+(high-low)
            # target2=rr2
            # file.write("\nTarget price 1=")
            # file.write(str(round(target1,2)))
            # file.write("\nTarget price 1=")
            # file.write(str(round(target2,2)))

            # file.write("\nStop loss=")
            # stop_loss=data[temp-1][2]
            # stop_loss=stop_loss-(stop_loss*0.002)
            # file.write(str(round(stop_loss,2)))
            file.write("\n\n")

            print("Company name=",symbol[i][1])
            print("Suggestion=Buy stock")
            # print("Entry price=",avg)
            # print("Target price1=",target1)
            # print("Target price2=",target2)
            # print("Stop loss",stop_loss)

            if(data[temp-1][4]<data[temp][4]):
                result.append([symbol[i][1],data[temp-1][0],'bullish','bullish'])
            else:
                result.append([symbol[i][1],data[temp-1][0],'bullish','bearish'])
            i=i+1
        elif check<0:
            file.write("Company name=")
            file.write(symbol[i][1])
            file.write("\n")
            file.write("Suggestion=Sell stock\n")
            # file.write("Entry price=")
            # avg=data[temp-1][1]
            # avg=avg+(avg*0.005)
            # file.write(str(round(avg,2)))
            # high=piv_high(data,temp-1)
            # low=piv_low(data,temp-1)
            # close=piv_close(data,temp-1)

            # pp=(high+low+close)/3
            # rr1=(2*pp)-low
            # target1=rr1
            # rr2=pp+(high-low)
            # target2=rr2
            # file.write("\nTarget price 1=")
            # file.write(str(round(target1,2)))
            # file.write("\nTarget price 2=")
            # file.write(str(round(target2,2)))

            # file.write("\nStop loss=")
            # stop_loss=data[temp-1][2]
            # stop_loss=stop_loss-(stop_loss*0.002)
            # file.write(str(round(stop_loss,2)))
            file.write("\n\n")

            print("Company name=",symbol[i][1])
            print("Suggestion=Sell stock")
            # print("Target price1=",target1)
            # print("Target price2=",target2)
            # print("Stop loss",stop_loss)

            if(data[temp-1][4]<data[temp][4]):
                result.append([symbol[i][1],data[temp-1][0],'bearish','bullish'])
            else:
                result.append([symbol[i][1],data[temp-1][0],'bearish','bearish'])
            i=i+1
        else:
            i=i+1
    except:



        i=i+1
file.close()

result

res_df=pd.DataFrame(result,columns=['Date','Company Name','Prediction','Actual'])

res_df.to_csv('prediction_res.csv')

count=0
b=0
for i in range(len(result)):
    if(result[i][2]==result[i][3] and result[i][2]=='bullish'):
        count=count+1
    elif(result[i][2]==result[i][3] and result[i][2]=='bearish'):
        b=b+1

acq=(count+b)/len(result)

print("The accuraccy is=",round(acq,2))

arr = res_df.to_numpy()

actual=[]
predicted=[]
for i in range (len(arr)):
  actual.append(arr[i][2])
  predicted.append(arr[i][3])

from sklearn import metrics
confusion_matrix = metrics.confusion_matrix(actual, predicted)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['Bearish', 'Bullsih'])
import matplotlib.pyplot as plt
cm_display.plot()
plt.show()

