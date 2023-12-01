import pandas as pd
from sqlalchemy import create_engine, MetaData
from roster import roster
from user import user

# create engine
engine = create_engine('mysql+mysqlconnector://root:Long9136!@localhost/mydatabase')

# Replace 'table_name' with the desired table name
rosters = 'rosters'
roster.to_sql(rosters, con=engine, if_exists='replace', index=False)

users = 'users'
user.to_sql(users, con=engine, if_exists='replace', index=False)

# Replace 'your_table_name' with the actual table name
# table_name = 'users'

# Create a Metadata object
metadata = MetaData()

# Bind the engine to the metadata
metadata.reflect(bind=engine)

# Check if the table exists in the metadata
# if table_name in metadata.tables:
#     print(f"The table '{table_name}' exists.")
# else:
#     print(f"The table '{table_name}' does not exist.")

# Query to select all rows from the table
query = f"SELECT * FROM rosters"
query2 = f"SELECT * FROM users"

# Execute the query and fetch results into a Pandas DataFrame
rosters = pd.read_sql(query, con=engine)
users = pd.read_sql(query2, con=engine)

# Save the DataFrame to a CSV file
csv_rosters = 'rosters_api_data.csv'
rosters.to_csv(csv_rosters, index=False)

csv_users = 'users_api_data.csv'
users.to_csv(csv_users, index=False)

# Display the DataFrame
# print(rosters)
# print(users)

# Read the data from the CSV file into a new DataFrame
roster_df = pd.read_csv(csv_rosters)
user_df = pd.read_csv(csv_users)

# Display the loaded DataFrame
print(roster_df)
print(user_df)

