import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Drop database
mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS unsafe_database")

# Close MySQL connection
mydb.close()