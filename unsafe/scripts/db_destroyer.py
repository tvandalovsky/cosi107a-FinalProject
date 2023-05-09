'''
Created by Anya Lefkowitz, Hannah Whitmore, and Thomas Vandalovsky
COSI-107a - Cyber Security

Description: 
python script to delete mysql database and reset testing environment
called in make unsafe_clean
'''

import mysql.connector

PASSWORD = ""

# Connect to MySQL server
# IF YOU HAVE A PASSWORD YOU NEED TO ADD IT INTO THE CODE FOR IT TO WORK
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=PASSWORD
)

# Drop database so you can run a clean environment next time you run it
mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS unsafe_database;")

# Close MySQL connection
mydb.close()