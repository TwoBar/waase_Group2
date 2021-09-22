#SenseHat is an add-on board that enables us to measure and collect sensor data and output info using built-in LED matrix.
import subprocess
from sense_hat import SenseHat
import time
import bluetooth
import urllib2
import mysql.connector
import os

sense = SenseHat()
blue = (0, 0, 255)
red = (100, 0, 70)
green = (0, 150, 100)



host = ""
port = 1        # Raspberry Pi uses port 1 for Bluetooth Communication
# Creaitng Socket Bluetooth RFCOMM communication
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')
try:
        server.bind((host, port))
        print("Bluetooth Binding Completed")
        sense.show_message("BC", text_colour=blue)
except:
        print("Bluetooth Binding Failed")
        sense.show_message("BF", text_colour=red)
server.listen(1) # One connection at a time
# Server accepts the clients request and assigns a mac address.
client, address = server.accept()
print("Connected To", address)
print("Client:", client)
sense.show_message("GO!", text_colour=green)
datalist =[]

def internet_on():
    try:
        urllib2.urlopen('https://www.google.com/', timeout=10)
        print("wifi connected!")
        sense.show_message("Wifi!", text_colour=green)
        return True
    except urllib2.URLError as err:
        print("insert credential:")
        sense.show_message("x", text_colour=red)
        return False



while internet_on() == False and (len(datalist)) < 2:
    
    
    data = client.recv(1024) # 1024 is the buffer size.
    print(data)
    datalist.append(data)
    if (len(datalist)) == 2 and (len(datalist[1])) > 7:
        ssid=datalist[0]
        print(datalist[0], datalist[1])
        passkey=datalist[1]
        
        p1 = subprocess.Popen(["wpa_passphrase", ssid, passkey], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["sudo","tee","-a","/etc/wpa_supplicant/wpa_supplicant.conf",">","/dev/null"], stdin=p1.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()  # Give p1 a SIGPIPE if p2 dies.
        output,err = p2.communicate()
        sense.show_message("reboot!", text_colour=green)
        os.system('sudo shutdown -r now')
    elif (len(datalist)) == 2 and (len(datalist[1])) < 7:
        print("error")
        datalist =[]
    elif (len(datalist)) == 1:
        sense.show_message("insert wifi psw:", text_colour=red)
    elif (len(datalist)) == 0:
        sense.show_message("insert wifi name:", text_colour=red)
        
        
while internet_on() == True:
    try:
        conn = mysql.connector.connect(user='baba@barnaserver',
                                       password='BBgang22',
                                       database='northwind',
                                       host='barnaserver.mysql.database.azure.com')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM customers")
        myresult = mycursor.fetchall()
        sense.show_message("Azure!", text_colour=blue)
        while True:
            
            datalist =[]
            data = client.recv(1024) # 1024 is the buffer size.
            print(data)
            datalist.append(data)
            
            for idd in datalist:
                for x in myresult:
                    if idd == x[0]:
                        print(x[1])
                        sense.show_message(x[1], text_colour=green)
                    elif idd == "q":
                            sense.show_message("Bye!", text_colour=red)
                            print("good bye")
                            quit()
                    


    except mysql.connector.Error as err:
        sense.show_message("X", text_colour=red)
        print(err)
        client.close()
        server.close() 
