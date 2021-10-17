from flask import Flask, render_template, request, redirect,jsonify
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)

# Configure db



@app.route('/', methods=['GET', 'POST'])
def mac():
    conn = mysql.connector.connect(user='group2@waaseteam2',
                                   password='Waaseteam2',
                                   database='waaseteam2',
                                   host='waaseteam2.mysql.database.azure.com')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM user")
    users = mycursor.fetchall()
    mycursor.execute("SELECT * FROM device")
    devices = mycursor.fetchall()
    mycursor.execute("SELECT * FROM input_data")
    data = mycursor.fetchall()
    mac = request.form
    mac  = mac['mac']
    print(mac)
    for x in devices:
        if mac == str(x[0]):
            print(x[3])
            userID = x[3]
            for y in data:
                if userID == y[0]:
                    print(data)
                    data.clear()
                    print(data)
                    return jsonify(message=y[3])

    return jsonify(message="Mac not found:" + mac)



if __name__ == '__main__':
    app.run(debug=True, port=5001)
