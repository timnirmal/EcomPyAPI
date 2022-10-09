# from supabase import create_client
# import uuid
# import json
# import pandas as pd
# import DataGenerator.Uploaded_Data as UD
#
# # load 'product.json'
# with open('products.json') as f:
#     products = json.load(f)
#
# # convert products to dataframe
# df = pd.DataFrame(products)
#
# # show all column in head
# pd.set_option('display.max_columns', None)
#
# print(df)
#
# # get all category to list
# category = df['category'].unique().tolist()
#
# print(category)
#
# cat = ['T-shirt', 'Dress', 'Heels', 'Sweatshirt', 'Sneaker', 'Watch', 'Jumpsuit', 'Wallet', 'Trousers', 'Shirt', 'Kurta', 'Top', 'Jean', 'Jacket', 'Bra', 'Shorts', 'Belt', 'Suit', 'Flat', 'Sweater', 'Churidar', 'Bag', 'Dupatta', 'Skirt', 'Pant', 'Sandal', 'Legging', 'Shoe', 'Saree', 'Blazer', 'Flip-Flops', 'Short', 'Cream', 'Sunglasses', 'Perfume', 'Loafer', 'Mask', 'Other']
#
# # get all brand to list
# brand = df['brand'].unique().tolist()
#
# print(brand)
#
# # get all color to list
# colors = df['PrimaryColor'].unique().tolist()
#
# print(colors)

number =  '1,999.00'

newNUmber = number.replace(',', '')

print (newNUmber)