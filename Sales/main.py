from datetime import datetime, timedelta
from supabase import create_client
import uuid
import json
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import math
import numpy as np
from numpy.linalg import norm
from fastapi.responses import FileResponse
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import cloudinary

cloudinary.config(
    cloud_name="dxbi9m7sv",
    api_key="651348724447779",
    api_secret="Z5LP84k7pwSFv1yDPf604sjyVjE"
)

import cloudinary.uploader
import cloudinary.api

API_URL = 'https://dquglwcmtervdexzzyma.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRxdWdsd2NtdGVydmRleHp6eW1hIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY1NjMwMjc0MCwiZXhwIjoxOTcxODc4NzQwfQ.HnD8TCzYHQLEu3WRs-2tCH-1etD0WdO8MKkRQU77MW4'
supabase = create_client(API_URL, API_KEY)
print(supabase)


# # Get order data from supabase
# OrderData = supabase.table('orders').select('*').execute()
#
# # save to json file
# with open('orders.json', 'w') as f:
#     json.dump(OrderData.data, f)

# load json file
with open('orders.json', 'r') as f:
    OrderData = json.load(f)

# convert to dataframe
OrderData = pd.DataFrame(OrderData)

# df head show all columns
pd.set_option('display.max_columns', None)

print(OrderData)


def NumofDaysSalesReport(numofdays=30):
    global date, OrderData

    # get datetime of 30 days ago
    today = datetime.today()
    thirty_days_ago = today - timedelta(days=numofdays)

    # filter orders by date
    for i in range(len(OrderData)):
        dateTable = datetime.strptime(OrderData['datetime'][i], "%Y-%m-%dT%H:%M:%S")
        if dateTable < thirty_days_ago:
            OrderData.drop(i, inplace=True)
    print()
    print(OrderData)
    # count orderData rows
    print(OrderData.shape[0])
    # calculate each day sales in last 30 days
    # datetime timestamp to date
    OrderData['datetime'] = pd.to_datetime(OrderData['datetime']).dt.date
    # group by date
    OrderData = OrderData.groupby(['datetime']).size().reset_index(name='counts')
    # sort by date
    OrderData = OrderData.sort_values(by=['datetime'])
    # reset index
    OrderData = OrderData.reset_index(drop=True)
    print(OrderData)

    # fill missing dates
    date = pd.date_range(start=thirty_days_ago, end=today)
    date = pd.DataFrame(date)
    date.columns = ['datetime']
    date['datetime'] = pd.to_datetime(date['datetime']).dt.date
    print(date)
    OrderData = pd.merge(date, OrderData, on='datetime', how='left')
    OrderData = OrderData.fillna(0)
    print(OrderData)

    return OrderData


def plotData(plottype='bar', numofdays=30):
    OrderData = NumofDaysSalesReport(numofdays)

    # plot sales in last 30 days
    plt.figure(figsize=(10, 5))
    if plottype == 'bar':
        sns.barplot(data=OrderData, x='datetime', y='counts')
    elif plottype == 'line':
        sns.lineplot(data=OrderData, x='datetime', y='counts')
    elif plottype == 'scatter':
        sns.scatterplot(data=OrderData, x='datetime', y='counts')
    elif plottype == 'point':
        sns.pointplot(data=OrderData, x='datetime', y='counts')
    elif plottype == 'strip':
        sns.stripplot(data=OrderData, x='datetime', y='counts')
    elif plottype == 'swarm':
        sns.swarmplot(data=OrderData, x='datetime', y='counts')
    elif plottype == 'box':
        sns.boxplot(data=OrderData, x='datetime', y='counts')
    elif plottype == 'violin':
        sns.violinplot(data=OrderData, x='datetime', y='counts')
    elif plottype == 'count':
        sns.countplot(data=OrderData, x='datetime', y='counts')
    elif plottype == 'cat':
        sns.catplot(data=OrderData, x='datetime', y='counts')
    else:
        # default plot type is bar
        sns.barplot(data=OrderData, x='datetime', y='counts')
    plt.title('Sales in last 30 days')
    # 5 days for each x label
    plt.xticks(rotation=45)
    # only integer on y axis
    plt.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.savefig('sales.png')

    # upload image to cloudinary
    cloudinary.uploader.upload("sales.png", public_id="sales", overwrite=True, invalidate=True)

    # get image url
    image_url = cloudinary.CloudinaryImage("sales").build_url()
    print(image_url)

    return str(image_url)


def getSalesData(numofdayas=30):
    OrderData = NumofDaysSalesReport(numofdayas)

    print("Converting ....")
    # convert to json
    OrderDataJson = OrderData.to_json(orient='records', indent=4)

    # save to json file
    with open('NumofDaysSalesReport.json', 'w') as f:
        f.write(OrderDataJson)

    # Read json file
    with open('NumofDaysSalesReport.json', 'r') as f:
        OrderDataJson = json.load(f)

    return OrderDataJson



def lastOrdersReport(numoforders=10):
    global OrderData

    # order by datetime
    OrderData = OrderData.sort_values(by=['datetime'], ascending=False)

    # reset index
    OrderData = OrderData.reset_index(drop=True)

    # get last 10 orders
    OrderData = OrderData.tail(numoforders)
    print(OrderData)

    # keep only username, totalPrice, id
    OrderData = OrderData[['username', 'totalprice', 'id']]
    print(OrderData)

    #convert to json
    OrderDataJson = OrderData.to_json(orient='records', indent=4)

    # save to json file
    with open('lastOrdersReport.json', 'w') as f:
        f.write(OrderDataJson)

    # Read json file
    with open('lastOrdersReport.json', 'r') as f:
        OrderDataJson = json.load(f)

    return OrderDataJson




#NumofDaysSalesReport(numofdays=30, plot=True)

#lastOrdersReport(numoforders=10)


#
# # get date of each order
# date = []
# for i in range(len(OrderData)):
#     date.append(OrderData['datetime'][i][:10])
#
# # convert to dataframe
# date = pd.DataFrame(date, columns=['date'])
#
# # count each date
# date = date.groupby('date').size().reset_index(name='count')
#
# # convert date to datetime
# date['date'] = pd.to_datetime(date['date'])
#
# # sort by date
# date = date.sort_values(by='date')
#
# # plot
# plt.figure(figsize=(15, 5))
# sns.lineplot(data=date, x='date', y='count')
# plt.title('Sales in last 30 days')
# plt.xlabel('Date')
# plt.ylabel('Sales')
# plt.savefig('sales.png')
#
# # show plot
# plt.show()









# # get unique customers
# customers = OrderData['customer_id'].unique()
#
# # create empty dataframe
# customers_df = pd.DataFrame()
#
# # loop through customers
# for customer in customers:
#     # get customer data
#     customer_data = OrderData[OrderData['customer_id'] == customer]
#
#     # get total spent
#     total_spent = customer_data['total'].sum()
#
#     # get total orders
#     total_orders = customer_data.shape[0]
#
#     # get first order date
#     first_order_date = customer_data['date'].min()
#
#     # get last order date
#     last_order_date = customer_data['date'].max()
#
#     # get customer id
#     customer_id = customer_data['customer_id'].iloc[0]
#
#     # create new row
#     new_row = {
#         'customer_id': customer_id,
#         'total_spent': total_spent,
#         'total_orders': total_orders,
#         'first_order_date': first_order_date,
#         'last_order_date': last_order_date
#     }
#
#     # append new row to customers_df
#     customers_df = customers_df.append(new_row, ignore_index=True)
#
# # convert first_order_date and last_order_date to datetime
# customers_df['first_order_date'] = pd.to_datetime(customers_df['first_order_date'])
# customers_df['last_order_date'] = pd.to_datetime(customers_df['last_order_date'])
#
# print(customers_df)
#

