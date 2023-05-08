import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
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
        name VARCHAR(255),
        email VARCHAR(255)
    )
""")

# Close MySQL connection
mydb.close()