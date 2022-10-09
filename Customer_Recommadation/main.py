from supabase import create_client
import uuid
import json
import pandas as pd
import DataGenerator.Uploaded_Data as UD

API_URL = 'https://dquglwcmtervdexzzyma.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRxdWdsd2NtdGVydmRleHp6eW1hIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY1NjMwMjc0MCwiZXhwIjoxOTcxODc4NzQwfQ.HnD8TCzYHQLEu3WRs-2tCH-1etD0WdO8MKkRQU77MW4'
supabase = create_client(API_URL, API_KEY)
print(supabase)


def func():
    hi = "message"
    return hi


def func2():
    return supabase

def products():
    ProductData = supabase.table('products').select('*').execute()
    productDataList = supabase.table('products').select('*').execute()

    print(productDataList)
    print(productDataList)
    print(productDataList)
    print(productDataList)
    print(productDataList)

    return productDataList



def recommendation(person_id):
    global category
    ProductData = supabase.table('products').select('*').execute()
    ProfileData = supabase.table('profiles').select('*').execute()

    def get_product_id(product_name):
        for i in range(len(ProfileData['data'])):
            if ProfileData['data'][i]['id'] == person_id:
                id = ProfileData['data'][i]
                break

    #id = ProfileData.data[0]['id']

    print()
    print()
    print(person_id)

    # get data from supabase
    data = supabase.from_("products").select("*").eq('id', person_id).execute()
    print(data)

    # load products.json
    with open('products.json') as f:
        products = json.load(f)

    # conver products to dataframe
    df = pd.DataFrame(products)

    # for each row in dataframe
    for index, row in df.iterrows():
        print(row['id'], row['category'])
        if row['id'] == person_id:
            category = row['category']
            # get the row
            break

    print(person_id)
    print("Category: ", category)
    print(category)

    # get 4 random data from products dataframe where category is same
    df = df[df['category'] == category].sample(4)
    #
    print(df)

    # get id from dataframe
    id_list = df['id'].tolist()
    #
    # # convert dataframe to json
    # json_data = df.to_json(orient='records',  indent=4)
    #
    # # save json to file
    # with open('recommendation.json', 'w') as f:
    #     f.write(json_data)
    #
    # # load json file and return
    # with open('recommendation.json') as f:
    #     data = json.load(f)




    # get category of id from

    # Do the recommendation

    # Output Recommendation
    # append to a list
    list1 = []
    list1.append(16)
    list1.append(17)
    list1.append(17)
    list1.append(16)
    Recommendation_output = id_list

    productDataList = []

    # for each item in list1
    for i in range(len(Recommendation_output)):
        productDataList.append(supabase.table('products').select('*').eq('id', Recommendation_output[i]).execute())


    # print(productDataList)
    # print(productDataList)
    # print(productDataList)
    # print(productDataList)
    # print(productDataList)

    return productDataList
    #return Recommendation_output



def CartItems(person_id):
    CartData = supabase.table('cart').select('*').execute()
    # convert string to uuid
    #uuid_object = uuid.UUID(CartData['data'][0]['id'])
    #CartData = supabase.table('cart').select('*').execute()
    ProfileData = supabase.table('profiles').select('*').execute()


    def get_product_id(person_id):
        for i in range(len(CartData.data)):
            if CartData.data[i]['id'] == person_id:
                data = CartData.data[i]
                return data

    #id = ProfileData.data[0]['id']

    data = get_product_id(person_id)['items']
    #data = CartData.data[0]

    print(data)
    print(data)
    print(data)

    return data
    #return Recommendation_output


def main():
    hi = func()
    print(hi)

