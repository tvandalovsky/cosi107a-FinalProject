import mysql.connector
import json

# Connect to MySQL server requires that user does not have password for mysql. 
# IF YOU HAVE A PASSWORD YOU NEED TO ADD IT INTO THE CODE FOR IT TO WORK

PASSWORD = ""

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=PASSWORD
)

# Create database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS unsafe_database")

# Switch to unsafe_database
mycursor.execute("USE unsafe_database")

# Create users table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        admin BOOLEAN,
        name VARCHAR(255),
        email VARCHAR(255),
        salary INT
    )
""")

default_users = [

]

# Close MySQL connection
mydb.close()