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

# from supabase import orders
orders = supabase.table('orders').select('*').execute()

print(orders)

sojd = [
    {'id': 1, 'username': 'timnirmal', 'payment': 2000.5, 'discount': 100, 'datetime': '2022-06-26T17:28:46+00:00',
         'orders': [{'id': 3, 'quantity': '4', 'created_at': '2022-07-05T17:58:29.178Z',
                     'properties': {'size': 'XL', 'color': 'red', 'material': 'silk'}},
                    {'id': 3, 'quantity': 1, 'created_at': '2022-07-05T17:58:58.751Z',
                     'properties': {'size': 'SM', 'color': 'white', 'material': 'cotton'}},
                    {'id': 3, 'quantity': '31', 'created_at': '2022-07-05T18:00:38.019Z',
                     'properties': {'size': 'SM', 'color': 'white', 'material': 'cotton'}},
                    {'id': 16, 'quantity': '6', 'created_at': '2022-07-05T18:05:42.752Z',
                     'properties': {'size': 'SM', 'color': 'white', 'material': 'cotton'}},
                    {'id': 17, 'quantity': '4', 'created_at': '2022-07-05T18:09:49.148Z', 'properties': {}}],
         'userid': '72abd6a1-9d84-432c-a114-ba27ed13bab7', 'totalprice': 1900.5},

        {'id': 2, 'username': 'Thimira', 'payment': 50, 'discount': 10, 'datetime': '2022-10-01T17:13:32.694+00:00',
         'orders': [{'id': 3, 'quantity': '4', 'created_at': '2022-07-05T17:58:29.178Z',
                     'properties': {'size': 'XL', 'color': 'Blue', 'material': 'cotton'}},
                    {'id': 3, 'quantity': 1, 'created_at': '2022-07-05T17:58:58.751Z',
                     'properties': {'size': 'SM', 'color': 'white', 'material': 'cotton'}},
                    {'id': 3, 'quantity': '31', 'created_at': '2022-07-05T18:00:38.019Z',
                     'properties': {'size': 'SM', 'color': 'white', 'material': 'cotton'}},
                    {'id': 16, 'quantity': '6', 'created_at': '2022-07-05T18:05:42.752Z',
                     'properties': {'size': 'SM', 'color': 'white', 'material': 'cotton'}},
                    {'id': 17, 'quantity': '4', 'created_at': '2022-07-05T18:09:49.148Z', 'properties': {}}],
         'userid': 'de1f515e-d6f5-4c08-a461-114183f2276c', 'totalprice': 40}]
