from supabase import create_client
import uuid
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import math
import numpy as np
from numpy.linalg import norm
from fastapi.responses import FileResponse

import cloudinary

cloudinary.config(
    cloud_name="dxbi9m7sv",
    api_key="651348724447779",
    api_secret="Z5LP84k7pwSFv1yDPf604sjyVjE"
)

import cloudinary.uploader
import cloudinary.api

config = cloudinary.config(secure=True)
API_URL = 'https://dquglwcmtervdexzzyma.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRxdWdsd2NtdGVydmRleHp6eW1hIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY1NjMwMjc0MCwiZXhwIjoxOTcxODc4NzQwfQ.HnD8TCzYHQLEu3WRs-2tCH-1etD0WdO8MKkRQU77MW4'
supabase = create_client(API_URL, API_KEY)
print(supabase)


def productInteraction(personID):
    InteractionData = supabase.table('Interactions').select('*').execute()

    for item in InteractionData.data:
        print(item)

    InteractionData = pd.DataFrame(InteractionData.data)

    print(InteractionData)

    ## Summarization of the data
    # https://www.kaggle.com/roshansharma/customer-segmentation-using-rfm-analysis

    # interaction = InteractionData.groupby('product')['type'].sum()
    interaction = InteractionData.groupby(['product', 'type']).size()
    interaction = interaction.reset_index()
    interaction.columns = ['ProductID', 'interaction Type', 'count']
    print("interaction")
    print(interaction)
    print(type(interaction))
    print(type(interaction))
    print(type(interaction))
    print(type(interaction))
    print(type(interaction))

    # For all item in interaction['interaction Type']:
    for item in interaction['interaction Type']:
        # if item == 1: replace with 'click'
        if item == 1:
            interaction['interaction Type'] = interaction['interaction Type'].replace(item, 'click')
        # if item == 2: replace with 'like'
        elif item == 2:
            interaction['interaction Type'] = interaction['interaction Type'].replace(item, 'like')
        # if item == 3: replace with 'purchase'
        elif item == 3:
            interaction['interaction Type'] = interaction['interaction Type'].replace(item, 'purchase')
        # if item == 4: replace with 'wishlist'
        elif item == 4:
            interaction['interaction Type'] = interaction['interaction Type'].replace(item, 'wishlist')
        # if item == 5: replace with 'add to cart'
        elif item == 5:
            interaction['interaction Type'] = interaction['interaction Type'].replace(item, 'add to cart')

    # Click - 1 Like - 2 Wishlist - 4 Add to Cart - 5 Proceed to Purchase - 3   6- share   7- comment   8- review
    # 9- view   10- search   11- view cart   12- checkout   13- return   14- cancel   15- refund   16- exchange
    # 17- subscribe   18- unsubscribe   19- download

    print(interaction)
    print(interaction)

    list1 = interaction.to_json(orient='records')
    print("list1")
    print(list1)
    print(type(list1))
    print(type(list1))

    # conver string to json
    list2 = json.loads(list1)

    # interaction.to_json('temp.json', orient='records', lines=True)

    # cloudinary.uploader.upload('plot.png', public_id='plot-customer', overwrite=True, invalidate=True)
    # srcURL = cloudinary.CloudinaryImage("plot-customer").build_url()

    # return interaction
    return list2


#  uvicorn main:app --reload


