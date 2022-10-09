import randominfo
import uuid
import random
import randomtimestamp
import datetime
import json
import pandas as pd
from supabase import create_client
import numpy as np

API_URL = 'https://dquglwcmtervdexzzyma.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRxdWdsd2NtdGVydmRleHp6eW1hIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY1NjMwMjc0MCwiZXhwIjoxOTcxODc4NzQwfQ.HnD8TCzYHQLEu3WRs-2tCH-1etD0WdO8MKkRQU77MW4'
supabase = create_client(API_URL, API_KEY)
print(supabase)

from collections import Counter


def random_email(first_name):
    domains = ["gmail", "yahoo", "hotmail", "express", "yandex", "nexus", "online", "omega", "institute", "finance",
               "company", "corporation", "community"]
    extentions = ['com', 'in', 'jp', 'us', 'uk', 'org', 'edu', 'au', 'de', 'co', 'me', 'biz', 'dev', 'ngo', 'site',
                  'xyz', 'zero', 'tech']

    random_Numeber = random.randint(0, 1000)

    return f"{first_name.lower()}{random_Numeber}@{random.choice(domains)}.{random.choice(extentions)}"


def random_date_generator():
    now = datetime.datetime.now()
    generated = randomtimestamp.randomtimestamp(start_year=2021, end_year=2022)

    # IF generated timestamp is in the future, then generate a new one
    while generated > now:
        generated = randomtimestamp.randomtimestamp(start_year=2021, end_year=2022)

    return generated.strftime("%m/%d/%Y, %H:%M:%S")


def generate_product():
    first_name = randominfo.get_first_name(gender=None)

    # name
    # discrption
    # price
    # discount
    # joinedat
    # imgurl
    # SKU
    # stock
    # rating
    # buyCount
    # offer
    # properties
    # orders

    userid = uuid.uuid4()
    username = first_name + " " + randominfo.get_last_name()
    password = randominfo.random_password(length=8)
    gender = randominfo.get_gender(first_name=first_name)
    dob = randominfo.get_birthdate()
    email = random_email(first_name)
    phone = randominfo.get_phone_number()
    joined_date = random_date_generator()
    url = "https://robohash.org/c0eb5cc8f036ec7ecd9d1f5b1f2ccb69?set=set4&bgset=&size=400x400"

    # to json
    person = {
        "id": str(userid),
        "username": username,
        "password": password,
        "gender": gender,
        "email": email,
        "phone": phone,
        "joinedat": joined_date
    }

    return person


def generate_people(count):
    people = [generate_person() for i in range(count)]
    return people


if __name__ == "__main__":
    print("Generating Data...")

    pd.set_option('display.max_columns', None)

    """
    # ProductID,ProductName,ProductBrand,Gender,Price (INR),NumImages,Description,PrimaryColor
    # read csv
    df = pd.read_csv('myntra_products_catalog.csv')

    # head with all columns
    pd.set_option('display.max_columns', None)

    #  remove column 'ProductBrand' and 'PrimaryColor'
    df = df.drop(['NumImages'], axis=1)

    print(df.head())

    # Brand Name to list
    brand_list = df['ProductName'].tolist()

    # list to string
    data_set = ' '.join(brand_list)

    # split() returns list of all the words in the string
    split_it = data_set.split()

    # Pass the split_it list to instance of Counter class.
    Counters_found = Counter(split_it)
    # print(Counters)

    # most_common() produces k frequently encountered
    # input values and their respective counts.
    most_occur = Counters_found.most_common(100)
    print(most_occur)

    # fashion wordset
    fashion_wordset = ['Socks', 'Shapewear', 'Blouse', 'Shorts', 'Glove', 'Espadrille', 'Saree', 'Clogs', 'Mule',
                       'Flip-Flops', 'Sweatshirt', 'Jean', 'Legging', 'Heels', 'Flat', 'Loafer', 'Trousers', 'T-shirt',
                       'Sandal', 'Belt', 'Flip-Flop', 'Espadrilles', 'Shirt', 'Sock', 'Flip Flop', 'Sneaker', 'Heel',
                       'Sandals', 'Blazer', 'Thongs', 'Pant', 'Coat', 'Tops', 'Kurti', 'Gloves', 'Thong', 'Boot',
                       'Mules', 'Salwar', 'Dress', 'Sliders', 'Leggings', 'Shoe', 'Suits', 'Wedges', 'Watch', 'Slider',
                       'Trainer', 'Skirt', 'Trainers', 'Activewear', 'Shoes', 'Flip Flops', 'Slipper', 'T-shirts',
                       'Bag',
                       'Bodysuit', 'Flats', 'Perfume', 'Underwear', 'Dresse', 'Jumpsuit', 'Jacket', 'Top',
                       'Sunglasses', 'Trouser', 'Watches', 'Sneakers', 'Bra', 'Nightwear', 'Jodhpuri', 'Loafers',
                       'Tuxedo', 'Wallets', 'Swimwear', 'Boots', 'Hat', 'Churidar', 'Sweater', 'Suit', 'Tie', 'Dresses',
                       'Kurta', 'Pants', 'Scarf', 'Wedge', 'Panties', 'Sherwani', 'Dupatta', 'Bags', 'Clog', 'Pantie',
                       'Jeans', 'Jackets', 'Slippers', 'Mask', 'Short', 'T-Shirt', 'Belts', 'Cream', 'Hats',
                       'Denim', 'Wallet']

    duplicate_wordset = ['Belt', 'Wallet', 'Suit', 'Jean', 'Shirt', 'T-Shirt' 'Bag', 'Watch', 'Top', 'Dress', 'Jacket',
                         'Hat']
    duplicate_wordset_duplicate = ['Belts', 'Wallets', 'Suits', 'Jeans', 'Shirts', 'T-Shirts', 'Bags', 'Watches',
                                   'Tops',
                                   'Dresses', 'Jackets', 'Hats']

    # for each row in the dataframe 'ProductName' column, check if the word is in the fashion_wordset and if it is, then
    # add that word to the 'Product Category' column, else add 'Other'
    for index, row in df.iterrows():
        for word in fashion_wordset:
            if word.lower() in row['ProductName'].lower():
                df.at[index, 'Product Category'] = word
                break
            else:
                df.at[index, 'Product Category'] = 'Other'

    for index, row in df.iterrows():
        for word in fashion_wordset:
            if word.lower() in row['Description'].lower():
                df.at[index, 'Product Category Description'] = word
                break
            else:
                df.at[index, 'Product Category Description'] = 'Other'

    # if the 'Product Category' column is 'Other' then add the 'Product Category Description' column value to the
    # 'Product Category' column and print the row if both the columns are not 'Other'
    for index, row in df.iterrows():
        if row['Product Category'] == 'Other':
            # df.at[index, 'Product Category'] = row['Product Category Description']
            if row['Product Category Description'] != 'Other':
                # print(row)
                pass

    # If 'Product Category' column has word in duplicate_wordset_duplicate, then replace it with the word in duplicate_wordset
    for index, row in df.iterrows():
        for word in duplicate_wordset_duplicate:
            if word.lower() in row['Product Category'].lower():
                df.at[index, 'Product Category'] = duplicate_wordset[duplicate_wordset_duplicate.index(word)]
                break

    # If 'Product Category Description' column has word in duplicate_wordset_duplicate, then replace it with the word in duplicate_wordset
    for index, row in df.iterrows():
        for word in duplicate_wordset_duplicate:
            if word.lower() in row['Product Category Description'].lower():
                df.at[index, 'Product Category Description'] = duplicate_wordset[
                    duplicate_wordset_duplicate.index(word)]
                break

    print(df.head())

    # save to csv
    df.to_csv('WithCategory.csv', index=False)

    """

    """
        # read csv
        df = pd.read_csv('WithCategory.csv')
    
        # count number of rows
        print("Number of rows: ", len(df.index))
    
        # remove 1000 rows which has 'Other' in 'Product Category' column
        for i in range(1000):
            df = df[df['Product Category'] != 'Other']
    
        # count number of rows
        print("Number of rows: ", len(df.index))
    
        # Remove 7000 random rows
        df = df.sample(frac=0.05, random_state=1)
    
        # count number of rows
        print("Number of rows: ", len(df.index))
    
        # count fashion wordset words frequency in the 'Product Category' column
        fashion_wordset_count = df['Product Category'].value_counts()
        print(fashion_wordset_count)
    
    
        # for each row
        for index, row in df.iterrows():
            # generate random number between 1.0 and 5.0 for 'rating'
            df['rating'] = np.random.uniform(1.0, 5.0, size=(len(df), 1)).round(1)
    
            # Generate stock
            df['stock'] = np.random.randint(1, 100, size=(len(df), 1))
    
            # Generate SKU with 'Category' and 3 digit incrementing number
            df['SKU'] = df['Product Category'].str[:3] + df.groupby('Product Category').cumcount().add(1).astype(
                str).str.zfill(3)
            #df['SKU'] = df['Product Category'].str[0:3] + np.random.randint(100, 999, size=(len(df), 1)).astype(str)
    
            # joinedat with random timestamp between 2020-10-01 and 2022-10-01
            df['joinedat'] = random_date_generator()
    
        print(df.head())
        print()
        print()
        print()
        print()
    
        # Generate random discount between 0 and 50 smaller than respective 'price'
        # get 'price' in of the considering row
        for index, row in df.iterrows():
            price = row['Price (INR)']
            # generate random discount between 0 and 50 giving more weightage to 0
            discount = np.random.randint(0, 50)
            # if discount is less than price then add it to the 'discount' column
            if discount < price * 40 / 100:
                df.at[index, 'discount'] = discount
            else:
                df.at[index, 'discount'] = 0
    
        properties = {
            "size": {
                "value": [
                    "SM",
                    "L"
                ]
            },
            "color": {
                "value": [
                    "white",
                    "blue"
                ]
            },
            "material": {
                "value": "cotton"
            }
        }
    
        # for each row in the dataframe add the properties
        for index, row in df.iterrows():
            df.at[index, 'properties'] = str(properties)
    
        print("Final")
        print(df.head())
    
        # save to csv
        df.to_csv('Final.csv', index=False)
    
    """

    # read csv
    df = pd.read_csv('Final.csv')

    # count number of rows
    print("Number of rows: ", len(df.index))
    print(df.head())

    # change column names
    df.rename(columns={'Product Category': 'category', 'ProductName': 'name', 'Description': 'description',
                       'Price (INR)': 'price', 'SKU': 'SKU', 'joinedat': 'joinedat', 'rating': 'rating',
                       'stock': 'stock', 'discount': 'discount', 'properties': 'properties', 'ProductID': 'id',
                       "ProductBrand": "brand", "Gender":"gender"}, inplace=True)

    # remove 'id' from df
    df.drop('id', axis=1, inplace=True)

    print(df.head())

    df.to_json("products.json", indent=4, orient="records")

    # get data from json file
    with open("products.json", "r") as f:
        people = json.load(f)

    # insert data to supabase
    for person in people:
        res = supabase.from_("products").insert(person).execute()
        print(res)


"""
    people = generate_people(10)
    # list to dataframe
    df = pd.DataFrame(people)
    # save df to txt with indent
    df.to_json("people.json", indent=4, orient="records")

    print(people)
    print(df)

    # get data from json file
    with open("people.json", "r") as f:
        people = json.load(f)

    # insert data to supabase
    for person in people:
        res = supabase.from_("profiles").insert(person).execute()
        print(res)

"""

## Categories
# Other         2440
# Shirt         1588
# T-shirt       1258
# Jean          1065
# Kurta          778
# Top            514
# Dress          451
# Trousers       407
# Sneaker        396
# Jacket         322
# Sweatshirt     310
# Watch          302
# Bag            292
# Bra            260
# Shoe           245
# Flat           215
# Sweater        158
# Sandal         150
# Saree          143
# Heels          122
# Shorts         107
# Suit            94
# Pant            89
# Blazer          82
# Sunglasses      69
# Wallet          64
# Skirt           53
# Legging         45
# Dupatta         45
# Churidar        41
# Belt            41
# Flip-Flops      40
# Jumpsuit        34
# Perfume         31
# Kurti           27
# Loafer          27
# Socks           24
# Wedges          20
# Mule            17
# Blouse          15
# Cream           14
# Coat            14
# Scarf           10
# Tie              9
# Hat              9
# Mask             9
# Sherwani         8
# Salwar           7
# Denim            4
# Tuxedo           4
# Bodysuit         4
# Heel             4
# Sliders          3
# Slipper          3
# Boot             2
# Clogs            2
# Underwear        1
# Jodhpuri         1
# Espadrille       1
# Short            1
