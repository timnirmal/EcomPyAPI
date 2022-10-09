import randominfo
import uuid
import random
import randomtimestamp
import datetime
import json
import pandas as pd
from supabase import create_client
import numpy as np

pd.set_option('display.max_columns', None)


API_URL = 'https://dquglwcmtervdexzzyma.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRxdWdsd2NtdGVydmRleHp6eW1hIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY1NjMwMjc0MCwiZXhwIjoxOTcxODc4NzQwfQ.HnD8TCzYHQLEu3WRs-2tCH-1etD0WdO8MKkRQU77MW4'
supabase = create_client(API_URL, API_KEY)
print(supabase)

# Load data fromt the supabase now in products.json
#
#
# # read products.json
# with open('Uploaded_Data/products.json') as f:
#     products = json.load(f)
#
# # conver products to dataframe
# #df = pd.DataFrame(products)
# df = pd.read_json("Uploaded_Data/products.json")
#
# # get 4 items of "T-shirt" category
# df = df[df['category'] == 'T-shirt'].sample(4)
#
#
# #print(df.head())
#
#
# # Get product data from supabase
# data = supabase.from_("products").select("*").execute()
#
# print(data)
#
# # convert to dataframe
# df2 = pd.DataFrame(data.data)
#
# print(df2.head())
#
# # dataframe to json
# df2.to_json("products.json", indent=4, orient="records")
#

# Read products.json
with open('products.json') as f:
    products = json.load(f)

# conver products to dataframe
df = pd.DataFrame(products)

# get 4 items of "T-shirt" category
df = df[df['category'] == 'Trousers'].sample(4)

# convert df to json
df.to_json("products 3.json", indent=4, orient="records")



