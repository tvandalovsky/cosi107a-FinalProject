from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

PASSWORD = ""

# Define route for home page
@app.route('/')
def home():
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database="unsafe_database"
    )
    mydb.close()
    return render_template('index.html')

# Define route for adding data to database
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Connect to MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=PASSWORD,
            database="unsafe_database"
        )
        # Get data from form
        name = request.form['name']
        email = request.form['email']

        # Check if user exists and retrieve admin value
        mycursor = mydb.cursor()
        mycursor.execute("SELECT admin FROM users WHERE name = %s AND email = %s", (name, email))
        result = mycursor.fetchone()

        if result:
            admin_value = result[0]

            # Fetch data from the database
            if admin_value:
                mycursor.execute("SELECT * FROM users")
            else:
                mycursor.execute("SELECT name, email FROM users WHERE admin = 0")

            data = mycursor.fetchall()
            columns = mycursor.description
            mydb.close()

            # Return success message
            return render_template("display.html", data=data, admin=admin_value)
        else:
            # User does not exist in the database, add them with admin value set to False
            mycursor.execute("INSERT INTO users (admin, name, email) VALUES (%s, %s, %s)", (False, name, email))
            mydb.commit()

            mycursor.execute("SELECT name, email FROM users WHERE admin = 0")
            data = mycursor.fetchall()
            mydb.close()
            return render_template("display.html", data=data, column=columns, admin=False)

    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
