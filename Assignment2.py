
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[1]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')


# In[11]:

import numpy as np
import pandas as pd
import matplotlib.dates as dates
get_ipython().magic('matplotlib notebook')

data=pd.read_csv("data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv")
data.head()


# In[12]:

data1=data[~data["Date"].str.endswith(r'02-29')]
data1['Date']=pd.to_datetime(data1['Date'])
data1['Day'],data1['Month'],data1['Year']=data1['Date'].dt.day, data1["Date"].dt.month,data1['Date'].dt.year
data1['Temp']=data1['Data_Value']//10
data1=data1.sort_values("Year")
data1.head()


# In[13]:

data_pre2015=data1[data1["Year"]!=2015].groupby(["Month","Day"])['Temp'].agg(['max','min']).reset_index()
data_pre2015.head()


# In[14]:

data_2015=data1[data1["Year"]==2015].groupby(["Month","Day"])['Temp'].agg(['max','min']).reset_index()
data_2015.head()


# In[29]:

import numpy as np
import pandas as pd

get_ipython().magic('matplotlib notebook')

data=pd.read_csv("data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv")

data1=data[~data["Date"].str.endswith(r'02-29')]
data1['Date']=pd.to_datetime(data1['Date'])
data1['Day'],data1['Month'],data1['Year']=data1['Date'].dt.day, data1["Date"].dt.month,data1['Date'].dt.year
data1['Temp']=data1['Data_Value']//10
data1=data1.sort_values("Year")

data_pre2015=data1[data1["Year"]!=2015].groupby(["Month","Day"])['Temp'].agg(['max','min']).reset_index()
data_2015=data1[data1["Year"]==2015].groupby(["Month","Day"])['Temp'].agg(['max','min']).reset_index()

maximum2015=[]
minimum2015=[]
max2015_axis=[]
min2015_axis=[]
for i in range(len(data_pre2015['max'])):
    if data_pre2015['min'][i]>data_2015['min'][i]:
        min2015_axis.append(i)
        minimum2015.append(data_2015['min'][i])
    if data_pre2015['max'][i]<data_2015['max'][i]:
        max2015_axis.append(i)
        maximum2015.append(data_2015['max'][i])

plt.plot(data_pre2015['min'],color='b', lw=0.5, label='record low 2005-2014')
plt.plot(data_pre2015['max'],color='r', lw=0.5, label='record high 2005-2014')

plt.xticks( np.linspace(0,365,num=12), [r'Jan', r'Feb', r'Mar', r'Apr', r'May', r'Jun', r'Jul', 
                                        r'Aug', r'Sep', r'Oct', r'Nov', r'Dec'] )

plt.scatter(min2015_axis, minimum2015,s=10,c='darkgreen',label='2015 break points (minimum)')
plt.scatter(max2015_axis, maximum2015,s=10,c='black',label='2015 break points (maximum)')

plt.gca().fill_between(range(len(data_pre2015['min'])), 
                       data_pre2015['min'], data_pre2015['max'], 
                       facecolor='grey', 
                       alpha=0.25)

plt.legend()
plt.xlabel('Month')
plt.ylabel('Temperature ($^0C$)')
plt.title("Ann Arbor, Michigan Temperature per day \n from 2005 to 2014, with 2015 outliers")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



