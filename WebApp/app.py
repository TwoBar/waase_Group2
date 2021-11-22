# API



from flask import Flask, render_template, request, redirect,jsonify
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__) # initiate Flask

@app.route('/', methods=['GET', 'POST'])
def mac(): # get the mac address from the connected device
    conn = mysql.connector.connect(user='group2@waaseteam2',
                                   password='Waaseteam2',
                                   database='waaseteam2',
                                   host='waaseteam2.mysql.database.azure.com')
    mycursor = conn.cursor()



    mac = request.form
    mac  = mac['mac']
    mycursor.execute("SELECT * FROM device where MAC_address = %s", (str(mac),))
    devices = mycursor.fetchall()
    for x in devices: # if any data is stored on the device table match the request Mac address
        print(x[3])
        userID = x[3]
    mycursor.execute("SELECT * FROM input_data where user_ID_data = %s", (str(userID),))
    data = mycursor.fetchall()
    print(mac +'connected!')
    for y in data:
        return jsonify(message=y[3], data_type=y[2])  # return the data in a jeson file to the device


    return jsonify(message="Mac not found:" + mac)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
