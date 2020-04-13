#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/bin/env python
# add your header here
#

"""Created on 2020-03-21 by Asmita Gautam
Assignment 08: Time-Series-analysis-with-pandas; tutorial codes
Using pandas #Pandas data demo type
Modified for comments on 2020-04-13
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt

pd.set_option('display.max_rows',15) # this limit maximum numbers of rows

##%pylab inline
#To print pandas version
print(pd.__version__)

"""
#!curl http://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/monthly.ao.index.b50.current.ascii >> 'monthly.ao.index.b50.current.ascii'
wget http://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/monthly.ao.index.b50.current.ascii
downloaded at 4:41 pm  3/21/2020
ao = np.loadtxt('monthly.ao.index.b50.current.ascii')
"""
#Monthly 
ao = np.loadtxt('monthly.ao.index.b50.current.ascii')
print(ao[0:2])  #It consist of three elements year, month and day
print(ao.shape) #shape of array is (842,3)

dates = pd.date_range('1950-01', periods=ao.shape[0], freq='M')  #Dates to date time index
print(dates)

print(dates.shape)

AO = Series(ao[:,2], index=dates)
#print(AO)
"""
#Daily atlantic ossilation, Output 23, from tutorial
"""
plt.figure()
AO.plot()
plt.title('Daily Atlantic oscillation')
plt.savefig('Daily_AO.pdf')
#AO['1980':'1990'].plot()   #For ploting a part, 1980 to 1990
#AO['1980-05':'1981-03'].plot()  #For ploting a specific time frame

print(AO[120])

print(AO['1960-01'])

AO['1960']


AO[AO > 0]

#Downloaded at 8:51

nao = np.loadtxt('norm.nao.monthly.b5001.current.ascii')
dates_nao = pd.date_range('1950-01', periods=nao.shape[0], freq='M')
NAO = Series(nao[:,2], index=dates_nao)
NAO.index
aonao = DataFrame({'AO' : AO, 'NAO' : NAO})

aonao.plot(subplots=True)
aonao.head()
aonao['NAO']
aonao.NAO
#Creating a column using the data within dataframe
aonao['Diff'] = aonao['AO'] - aonao['NAO']
aonao.head()
#Removing the column from a dataframe
del aonao['Diff']
aonao.tail()

aonao['1981-01':'1981-03'] #Selecting a specific timeframe

import datetime
aonao.loc[(aonao.AO > 0) & (aonao.NAO < 0) 
        & (aonao.index > datetime.datetime(1980,1,1)) 
        & (aonao.index < datetime.datetime(1989,1,1)),
        'NAO'].plot(kind='barh')

aonao.mean()

aonao.max()
aonao.min()
aonao.mean(1)

#To get descriptive statistics of dataframe
aonao.describe()

#To resample annullay and getting mean
AO_mm = AO.resample("A").mean()
AO_mm.plot(style='g--')
"""
#Annual median ossilation, resampling annual and getting median 
"""
plt.figure()
AO_mm = AO.resample("A").median()  
AO_mm.plot()
plt.title('Annual Median Ossilation')
plt.savefig('Annual_median_osicilation_AO.pdf')

## Resampling frequency of 3 years and getting maximum osillation for plot generation
AO_mm = AO.resample("3A").apply(np.max)
AO_mm.plot()

#Resampling for 3 years, max, min and mean and makings as subplots
AO_mm = AO.resample("A").apply(['mean', np.min, np.max])
AO_mm['1900':'2020'].plot(subplots=True)
AO_mm['1900':'2020'].plot()

AO_mm

"""
# Rolling mean of both  AO AND NOA, OUTPUT 52
"""
plt.figure()
aonao.rolling(window=12, center=False).mean().plot(style=['-g','-b'])#Changing color  
plt.title('Moving mean of AO and NOA')
plt.savefig('Rolling_mean_AO_NOA.pdf')

aonao.AO.rolling(window=120).corr(other=aonao.NAO).plot(style='-g') #Rolling correlation of 120 points

aonao.corr()
