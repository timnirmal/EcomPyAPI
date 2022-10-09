import randominfo
import uuid
import random
import randomtimestamp
import datetime
import json
import pandas as pd
from supabase import create_client

API_URL = 'https://dquglwcmtervdexzzyma.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRxdWdsd2NtdGVydmRleHp6eW1hIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY1NjMwMjc0MCwiZXhwIjoxOTcxODc4NzQwfQ.HnD8TCzYHQLEu3WRs-2tCH-1etD0WdO8MKkRQU77MW4'
supabase = create_client(API_URL, API_KEY)
print(supabase)

with open("products.json", "r") as f:
    products = json.load(f)



def random_email(first_name):
    domains = ["gmail", "yahoo", "hotmail", "express", "yandex", "nexus", "online", "omega", "institute", "finance",
               "company", "corporation", "community"]
    extentions = ['com', 'in', 'jp', 'us', 'uk', 'org', 'edu', 'au', 'de', 'co', 'me', 'biz', 'dev', 'ngo', 'site',
                  'xyz', 'zero', 'tech']

    random_Numeber = random.randint(0, 1000)

    return f"{first_name.lower()}{random_Numeber}@{random.choice(domains)}.{random.choice(extentions)}"


def random_date_generator(end_date=datetime.datetime.now()):
    print("End")
    # convert end date string to datetime
    if type(end_date) == str:
        end_date = datetime.datetime.strptime(str(end_date), "%Y-%m-%d %H:%M:%S.%f")
        #end_date = datetime.datetime.strptime('2022-10-04 15:12:25.439052', "%Y-%m-%d %H:%M:%S.%f")

    print(end_date)
    print(type(end_date))
    now = datetime.datetime.now()
    generated = randomtimestamp.randomtimestamp(start_year=2021, end_year=2022)
    print("Generated")
    print(generated)
    print(type(generated))

    # IF generated timestamp is in the future, then generate a new one
    while generated > now:
        generated = randomtimestamp.randomtimestamp(start_year=2021, end_year=2022)

    return generated


def generate_person():
    first_name = randominfo.get_first_name(gender=None)

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


def random_product():
    return random.choice(products)



def random_orders(created=datetime.datetime.now()):
    # get random product from products.json
    product = random_product()

    id = product["id"]
    price = product["price"]

    sizeList = ['SM', 'M', 'L', 'XL', 'XXL']
    materialList = ['cotton', 'silk', 'Linen']
    color = product['PrimaryColor']
    size = random.choice(sizeList)
    material = random.choice(materialList)

    # "properties" : { "size": "XL", "color": "red", "material": "silk" }
    # create properties string
    properties = f'"properties" : {{"size": "{size}", "color": "{color}", "material": "{material}"}}'

    created_at = random_date_generator(created)

    quantity = random.randint(1, 10)

    # remove fist letter from price and replace(",","") then convert to float and multiply by quantity
    total = float(price[1:].replace(",", "")) * quantity

    # print(product)
    # print(id)
    # print(color)
    # print(size)
    # print(material)
    # print(properties)
    # print(created_at)
    # print(quantity)

    # order string
    #   {
    #     "id": 3,
    #     "quantity": "4",
    #     "created_at": "2022-07-05T17:58:29.178Z",
    #     "properties": {
    #       "size": "XL",
    #       "color": "red",
    #       "material": "silk"
    #     }

    # create order string
    order = f'{{"id": {id}, "quantity": "{quantity}", "created_at": "{created_at.strftime("%m/%d/%Y, %H:%M:%S")}", {properties}}}'

    return order, total


def random_order():
    total_price = 0

    # create random date
    created_at = random_date_generator()

    # create random number of orders
    numorders = random.randint(1, 10)

    # get random orders for numorders
    orders, price = zip(*[random_orders(created_at) for i in range(numorders)])

    print("Orders")
    # get data from set
    # orders tuple to list
    orders = list(orders)
    print(orders)
    print(type(orders))
    print("Price")
    print(price)
    print(type(price))
    # each item in price tuple remove first letter, replace(",","") and covert to float and add to total_price
    # for item in price:
    #     total_price += float(str(item)[1:].replace(",", ""))
    total_price = sum(price)
    print("Total Price")
    print(total_price)

    # calculate random discount compared to total price
    discount = random.randint(0, int(total_price))
    print("Discount")
    print(discount)

    # get random person from supabase
    personList = supabase.from_("profiles").select("*").execute()
    #person = random.choice(personList['data'])

    #print(personList)
    print()
    #print(personList.data)
    print()
    print()
    # pick random person from list
    person = random.choice(personList.data)
    #print(person)
    # get person id
    personId = person['id']
    personUserName = person['username']
    #print(personId)

    totalPrice = total_price + discount
    print("Total Price")
    print(totalPrice)

    # orders to string
    orders = str(orders).replace("'", '')
    print("Orders")
    print(orders)
    print(type(orders))
    print(str(orders))
    print(orders)

    created_at = created_at.strftime("%m/%d/%Y, %H:%M:%S")

    # create dataframe with username, payment, discount, totalprice, datetime, userid
    df = pd.DataFrame({'username': [personUserName], 'payment': [total_price], 'discount': [discount], 'totalprice': [totalPrice], 'datetime': [created_at], 'userid': [personId], 'orders': [orders]})

    # all columns in head
    pd.set_option('display.max_columns', None)
    print(df.head())

    # df to json
    #df = df.to_json("order.json" ,indent=4, orient="records")

    # get data from json file
    with open("order.json", "r") as f:
        people = json.load(f)

    print(people)




    # # create order
    # order = {
    #     "username": personUserName,
    #     "payement": total_price + discount,
    #     "discount": discount,
    #     "totalPrice": total_price,
    #     "datetime": created_at.strftime("%m/%d/%Y, %H:%M:%S"),
    #     "orders": orders,
    #     "userid": personId
    # }
    #
    # # create orders string
    # #orders = f'{{"username": "{personUserName}", "payement": {total_price + discount}, "discount": {discount}, "totalPrice": {total_price}, "datetime": "{created_at.strftime("%m/%d/%Y, %H:%M:%S")}", "orders": {orders}, "userid": "{personId}"}}'
    #
    # printData = json.dumps(order, indent=4)
    # print(printData)
    #
    # # order to json with json.dumps
    # with open('order.json', 'w') as outfile:
    #     json.dump(order, outfile, indent=4)
    #
    #
    # # open order.json and read
    # with open('order.json') as json_file:
    #     data = json.load(json_file)




    return df


if __name__ == "__main__":
    print("Generating Data...")

    product = random_order()

    # product is a dataframe
    print(product)

    # create dataframe to hold all orders
    orders = pd.DataFrame()

    # df head with all columns
    pd.set_option('display.max_columns', None)

    # create 1000 orders
    for i in range(488):
        product = random_order()
        # add product dataframe to orders dataframe
        orders = pd.concat([orders, product], ignore_index=True)


    print(orders)

    # orders to json
    orders = orders.to_json("orders.json" ,indent=4, orient="records")

    # get data from json file
    with open("orders.json", "r") as f:
        orders_list = json.load(f)

    print(orders_list)

    # insert orders into supabase
    for order in orders_list:
        print(order)
        # insert order into supabase
        response = supabase.from_("orders").insert(order).execute()
        print(response)



    #print(product)

"""
## Data added to 'profiles' using this code
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


# .strftime("%m/%d/%Y, %H:%M:%S")