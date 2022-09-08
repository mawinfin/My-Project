# # Final Project - Analyzing Sales Data
# 
# **Date**: 1 March 2022
# 
# **Author**: Juladet Asunee Na Ayuttaya
# 
# **Course**: `Pandas Foundation`
# 
# You can see full code and some of visualization on this link
#
# https://datalore.jetbrains.com/notebook/EHPn07vg8F0Yf8S5GRJBSF/ZP2KHkAdvP64THutkD4tTG/


# import data
import pandas as pd
df = pd.read_csv("sample-store.csv")

# preview top 5 rows
df.head()

# shape of dataframe
df.shape

# see data frame information using .info()
df.info()

# We can use `pd.to_datetime()` function to convert columns 'Order Date' and 'Ship Date' to datetime.


# TODO - convert order date and ship date to datetime in the original dataframe
df['Order Date']=pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date']=pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')
df.head(10)

df.info()

# TODO - count nan in postal code column
df['Postal Code'].isna().sum()

# TODO - filter rows with missing values
df[df['Postal Code'].isna()]

# TODO - Explore this dataset on your owns, ask your own questions
#fill na
df['Postal Code']=df['Postal Code'].fillna(value='Not specified')
df.isna().sum()

#What is the most profit category in each region
own=df.groupby(['Region','Category'])['Profit'].sum().reset_index()
maxV=own.sort_values(['Region','Profit'],ascending=False)
maxV.iloc[[0,3,6,9]]

# ## Data Analysis Part
# 
# Answer 10 below questions to get credit from this course. Write `pandas` code to find answers.


# TODO 01 - how many columns, rows in this dataset
s=df.shape
print(s[0],'rows','and',s[1],'columns')

# TODO 02 - is there any missing values?, if there is, which colunm? how many nan values?
print('Yes,there is')
na=df['Postal Code'].isna().sum()
print('there are',na,'nan in Postal Code culumn')
df.isna().sum()



# TODO 03 - your friend ask for `California` data, filter it and export csv for him
Cali = df[df['State'] == 'California']
Cali.to_csv('California_data')

# TODO 04 - your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file
Cali_Tex_2017=df[((df['State'] == 'California')|(df['State'] == 'Texas'))\
    &((df['Order Date'] >= '2017-01-01') & (df['Order Date'] < '2018-01-01'))]
Cali_Tex_2017.to_csv('Cali_Texas_2017')

# TODO 05 - how much total sales, average sales, and standard deviation of sales your company make in 2017
df_2017=df[(df['Order Date'] >= '2017-01-01') & (df['Order Date'] < '2018-01-01')]
df_2017['Sales'].agg(['sum','mean','std'])

# TODO 06 - which Segment has the highest profit in 2018
df_2018=df[(df['Order Date'] >= '2018-01-01') & (df['Order Date'] < '2019-01-01')]
mp=df_2018.groupby('Segment')['Profit'].sum().reset_index()
mp.sort_values('Profit',ascending=False)
print('Highest profit in 2018 is')
print(mp.head(1))

# TODO 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019
df_new=df[(df['Order Date'] >= '2019-04-15') & (df['Order Date'] < '2019-12-31')]
Top5=df_new.groupby('State')['Sales'].sum().reset_index().sort_values('Sales')
print(Top5.head())

# TODO 08 - what is the proportion of total sales (%) in West + Central in 2019 e.g. 25% 
df_2019=df[(df['Order Date'] >= '2019-01-01') & (df['Order Date'] < '2020-01-01')]
Tsale=df_2019['Sales'].sum()
WC_2019=df_2019.query('Region == "West"|Region == "Central"')
WCsale=WC_2019['Sales'].sum()
print(int((WCsale/Tsale)*100),"%",'from 2019 total sales')


# TODO 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020
df_19_20=df[(df['Order Date'] >= '2019-01-01')]
#df_19_20['Product Name'].value_counts().nlargest(5)
top_pro=df_19_20.groupby('Product Name')['Order ID'].count().nlargest(10).reset_index()
top_sale=df_19_20.groupby('Product Name')['Sales'].sum().nlargest(10).reset_index()
top10 = pd.merge(top_pro, top_sale , left_index=True, right_index=True)
top10



# TODO 10 - plot at least 2 plots, any plot you think interesting :)
df['Region'].value_counts().plot(kind='bar',color=['Red','Salmon','Pink','Purple'])
#Order in each Region

#sales & profit in each region
sa=df.groupby('Region')['Sales'].sum()
pf=df.groupby('Region')['Profit'].sum()
data=pd.merge(sa,pf,left_index=True,right_index=True)
data.plot(kind='bar')

# TODO Bonus - use np.where() to create new column in dataframe to help you answer your own questions
# if Order have sales more than 500$ and don't have any discount,there will give free shipping.
# How many order are free shipping?
import numpy as np
df['Free shipping'] = np.where((df['Sales']>500)&(df['Discount']==0),True,False)
df['Free shipping'].value_counts()
#there are 512 order that have free shipping.

