import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Long9136!",
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

mycursor.execute("SHOW TABLES")