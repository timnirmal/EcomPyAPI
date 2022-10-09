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

if __name__ == "__main__":
    print("Generating Data...")




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