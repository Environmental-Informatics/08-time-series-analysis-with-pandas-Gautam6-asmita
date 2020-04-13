#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on 2020-03-22 by Asmita Gautam
Assignment 08: Time-Series-analysis-with-pandas
Use the date and time function with pandas dataframe 
To conduct timeseries data of a dataset
'WabashRiver Daily discharge from March 17 2015 to March 24 2016'

Modified for comments on 2020-04-13
"""

import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt


# open and read the file

#header=None, since the header of the dataset is not used
#skiprows=26, to skip the top 26 rows, which include comments
#usecols=[2,3,4], to read only the specified column

DataDF = pd.read_csv('WabashRiver_DailyDischarge_20150317-20160324.txt',
                     header=None, skiprows=26,usecols=[2,3,4],
                     names=['DateTime','TimeZone','Discharge'],  
                     delimiter="\t",parse_dates=[['DateTime','TimeZone']],
                     infer_datetime_format=True)
DataDF=DataDF.set_index('DateTime_TimeZone')    #To set the Datetime_Timezone as index
#print(DataDF.head())

#Daily discharge average, using resampling frequency of a day
plt.figure()
Discharge_D= DataDF.resample("D").mean()   #resampling daily and getting it's mean
Discharge_D.plot()
plt.xlabel('DateTime')
plt.ylabel('Discharge (cfs)')
plt.title('Average Daily Discharge')
plt.savefig('Average Daily Discharge.pdf')  #To save figure as pdf

#Highest 10 daily discharge
high10discharge=Discharge_D.nlargest(10,columns='Discharge')

#Ploting daily discharge showing highest 10 daily discharge
plt.figure()
Discharge_D.plot()
##Scatterplot of high 10 discharge with index so that it can we identified
plt.scatter(high10discharge.index,high10discharge.Discharge,
                        marker='*',c='r',label='Highest 10 Discharge')
plt.legend()  #To show legend
plt.xlabel('DateTime')
plt.ylabel('Discharge (cfs)')
plt.title('Highest 10 Daily Discharge')
plt.savefig('Highest 10 Daily Discharge.pdf')  #To save figure as pdf


#Monthly discharge average, using resampling frequency of a month
plt.figure()
Discharge_M= DataDF.resample("M").mean()    #Monthly resampling and getting it's mean
Discharge_M.plot()
plt.xlabel('DateTime')
plt.ylabel('Discharge (cfs)')
plt.title('Monthly Average Discharge')
plt.savefig('Monthly Average Discharge.pdf')  #To save figure as pdf

