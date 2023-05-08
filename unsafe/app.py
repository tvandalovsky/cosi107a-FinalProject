from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

PASSWORD = ""
# # Connect to MySQL database
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="unsafe_database"
# )

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

        # Insert data into MySQL database
        mycursor = mydb.cursor()
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        val = (name, email)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM users")
        data = mycursor.fetchall()
        columns = mycursor.description
        mydb.close()

        # Return success message
        return render_template("display.html", columns = columns , data=data)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)