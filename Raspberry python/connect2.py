
import subprocess
from sense_hat import SenseHat
import time
import bluetooth
import urllib.request 
import mysql.connector
import os
import json
import requests
import sys
import screen_outputs
from getmac import get_mac_address


sense = SenseHat()
blue = (0, 0, 255)
red = (100, 0, 70)
green = (0, 150, 100)
black = (0, 0, 0)
yellow = (180, 180, 100)
b = blue
r = red
g = green
n = black
y = yellow


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
        urllib.request.urlopen('https://www.google.com/', timeout=10)
        return True
    except urllib.error.URLError as err:
        print("insert credential:")
        sense.show_message("x", text_colour=red)
        return False

if internet_on() == True:
    print("wifi connected!")
    sense.show_message("Wifi connected!", text_colour=green)

while internet_on() == False and (len(datalist)) <= 2:
    
    
    data = client.recv(1024) # 1024 is the buffer size.
    print(data)
    datalist.append(data)
    if (len(datalist)) == 2 and (len(datalist[1])) > 7:
        if str(datalist[0]) == "b'Q'":
            print('exit!')
            sys.exit()
        ssid=datalist[0]
        print(datalist[0], datalist[1])
        if str(datalist[1]) == "b'Q'":
            print('exit!')
            sys.exit()
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
        
def insert_api():
    sense.show_message("API addres:", text_colour=red)
    data = client.recv(1024)    
    datalist.insert(0,data)
    if str(datalist[0]) == "b'Q'":
        print('exit!')
        sys.exit()
def Insert_username():
    data = get_mac_address()   
    datalist.insert(1,data)
    if str(datalist[1]) == "b'Q'":
        print('exit!')
        sys.exit()
    eth_mac = datalist[1] #get_mac_address()
def return_data(eth_mac, url):
    try:
        data = {"mac": eth_mac}
        x = requests.post(url, data = data)
        message = x.text
        messagedict = json.loads(message)
        dataB = messagedict['message']
        data_type = messagedict['data_type']
        print(messagedict)
        if data_type == 1:
            sense.show_message(dataB, text_colour=green)
        elif data_type == 2:
            if str(dataB) == 'D':
                screen_outputs.down()
                
            if str(dataB) == 'W':
                screen_outputs.up()
                
            if str(dataB) == 'L':
                screen_outputs.left()              
               
            if str(dataB) == 'R':
                screen_outputs.right()
        elif data_type == 3:
            tt = int(dataB[-1:])
            ss = int(dataB[-2:])
            mm = int(dataB[3:5])
            hh = int(dataB[0:2])
            print(ss)
            print(mm)
            print(hh)
            screen_outputs.watch(hh,mm,ss,tt)
            
        
        if str(dataB) == 'Q':
            print('EXIT!')
            sense.show_message('EXIT!', text_colour=red)
            sys.exit()
           
            
    except (requests.exceptions.RequestException, ValueError) as e:
        sense.show_message("Api connection failed", text_colour=red)
        print(e)
        api = insert_api()
    
    
    
while internet_on() == True and len(datalist) < 1:
    api = insert_api()
    print("API address: " + str(datalist[0]))
    
while internet_on() == True and len(datalist) >= 1:
    username = Insert_username()
    returnedData = return_data(datalist[1],datalist[0])
    datalist.pop()
    
    
    
