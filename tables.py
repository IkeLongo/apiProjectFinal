import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy import text
from roster import roster
from user import user
import pymysql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Long9136!",
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE roster (roster_id VARCHAR(2), owner_id VARCHAR(18), points VARCHAR(4))")

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host="localhost", db="mydatabase", user="root", pw="Long9136!"))

# Convert dataframes to sql table
roster.to_sql(name='rosters', con=engine, index=False)
user.to_sql(name='user', con=engine, index=False)

# with engine.connect() as conn:
#    conn.execute(text("SELECT * FROM rosters")).fetchall()
