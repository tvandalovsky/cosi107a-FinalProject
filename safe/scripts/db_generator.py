import mysql.connector

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
mycursor.execute("CREATE DATABASE IF NOT EXISTS safe_database")

# Switch to safe_database
mycursor.execute("USE safe_database")

# Create users table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        admin BOOLEAN NOT NULL DEFAULT 0,
        name VARCHAR(255),
        email VARCHAR(255),
        salary INT
    )
""")


users = [
    (True, 'Professor Treese', 'treese@fake.com', 5000000),
    (True, 'Jeff Forristal', 'ihearthacking@sql.com', 33434343),
    (True, 'Tim Hickey', 'code@cs.com', 45454334),
    (False, 'Jack Garbus', 'ta@cs.com', 300000),
    (True, 'Marco Qin', 'cs107a@cs.com', 455555),
    (False, 'Pito Salas', 'pivot@table.com', 1234566),
    (False, 'Louis D. Brandeis', 'brandeis@fake.com', 34000),
    (False, 'Ron Leb', 'ron@fake.com', 160),
]
for user in users:
    sql = "INSERT INTO users (admin, name, email, salary) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, user)

mydb.commit()

# Close MySQL connection and cursor connection
mycursor.close()
mydb.close()