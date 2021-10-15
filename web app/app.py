from flask import Flask, render_template, request, redirect,jsonify
from flask_mysqldb import MySQL
from datetime import datetime
import mysql.connector



app = Flask(__name__)

# Configure db
conn = mysql.connector.connect(user='group2@waaseteam2',
                                   password='Waaseteam2',
                                   database='waaseteam2',
                                   host='waaseteam2.mysql.database.azure.com')
mycursor = conn.cursor()
mycursor.execute("SELECT * FROM user")
myresult = mycursor.fetchall()


@app.route('/', methods=['GET', 'POST'])
def mac():
    mac = request.form
    mac  = mac['eventType']
    print(mac)
    for x in myresult:
        if mac == x[3]:
            print(x)
            return jsonify(message="My name is " + x[2])
    return jsonify(message="My name is " + mac)



if __name__ == '__main__':
    app.run(debug=True, port=5001)
