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
        
        if result:
            admin_value = result[0]
            print("admin_value", admin_value)

            # get data from db
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
