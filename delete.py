import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Long9136!",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE roster"

mycursor.execute(sql)