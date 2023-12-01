import mysql.connector
import pandas as pd
from pandas.io import sql
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Long9136!",
  database="mydatabase"
)

usdf = pd.read_json('https://api.sleeper.app/v1/league/918551365406797824/users')

usdf2 = usdf[['user_id', 'display_name']].copy()

user = usdf2.copy()

# print(user)