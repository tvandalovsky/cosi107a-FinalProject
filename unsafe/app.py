'''
Created by Anya Lefkowitz, Hannah Whitmore, and Thomas Vandalovsky
COSI-107a - Cyber Security

Description:
Unsafe app with unparameterized query
called in make unsafe_run
'''

from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

PASSWORD = ""

# home route
@app.route('/')
def home():
    # Connect to mysql db
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="unsafe_database"
    )
    mydb.close()
    return render_template('index.html')

# route for adding data to the db
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=PASSWORD,
            database="unsafe_database"
        )
        # get data from user form
        name = request.form['name']
        email = request.form['email']

        # check if user already exists in the db, and retrieve admin value
        ###
        # This is where the sql injection takes place since the query is not properly parameterized.
        # By concatenating the string to the query the attacker is able to add unwanted SQL commands leading them to gain admin access 
        ###
        mycursor = mydb.cursor()
        mycursor.execute("SELECT admin FROM users WHERE name = '%s' AND email = '%s'" % (name, email))
        result = mycursor.fetchall()

        mycursor.close()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=PASSWORD,
            database="unsafe_database"
        )

        mycursor = mydb.cursor()

        print("result", result)
        
        # if user entered has already been added to the SQL database
        if result:
            admin_value = result[0]
            print("admin_value", admin_value)

            # if user that has already been entered has been designated as an admin
            if admin_value:
                mycursor.execute("SELECT * FROM users")
            else:
                mycursor.execute("SELECT name, email FROM users WHERE admin = 0")

            data = mycursor.fetchall()
            columns = mycursor.description  # Get the column names
            
            mydb.close()
            
            # display relevant information
            return render_template("display.html", data=data, columns=columns, admin=admin_value)
        else:
            mycursor = mydb.cursor()
            # user not in the db, add them with admin value set to False
            mycursor.execute("INSERT INTO users (admin, name, email) VALUES (%s, %s, %s)", (False, name, email))
            mydb.commit()

            mycursor.execute("SELECT name, email FROM users WHERE admin = 0")
            data = mycursor.fetchall()
            columns = mycursor.description 
            
            mydb.close()
            return render_template("display.html", data=data, columns=columns, admin=False)

    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
