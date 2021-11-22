
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


sense = SenseHat()  # Initiate sense hat module

# define colours rgb codes
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

# Bluetooth connection
host = ""
port = 1        # Raspberry Pi uses port 1 for Bluetooth Communication
# Creaitng Socket Bluetooth RFCOMM communication
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')
try: # try to connect to a device if succeed
        server.bind((host, port))
        print("Bluetooth Binding Completed")
        sense.show_message("BC", text_colour=blue)# the pi display will allert BC(bluetooth connected)
except: # If connection failled
        print("Bluetooth Binding Failed")
        sense.show_message("BF", text_colour=red)# the pi display will allert BF(bluetooth failled)
server.listen(1) # One connection at a time
# Server accepts the clients request and assigns a mac address.
client, address = server.accept()
print("Connected To", address) # print out MAC address of the smartphone connected
print("Client:", client)
sense.show_message("GO!", text_colour=green) # allert the connection is working
# initiate datalist as a empty list
datalist =[]

def internet_on(): # function define if the raspberry has access to internet
    try:
        urllib.request.urlopen('https://www.google.com/', timeout=10)# test connection by connecting to google timeout after 10 sec
        return True
    except urllib.error.URLError as err:
        print("insert credential:")
        sense.show_message("x", text_colour=red)
        return False

if internet_on() == True:
    print("wifi connected!")
    sense.show_message("Wifi connected!", text_colour=green)

while internet_on() == False and (len(datalist)) <= 2:
    
    
    data = client.recv(1024) # 1024 is the bluetooth buffer size. retrive message sent by the smartphone via bt the socket is going to attempt to receive data, in a buffer size of 1024 bytes at a time.
    print(data)
    datalist.append(data)
    if (len(datalist)) == 2 and (len(datalist[1])) > 7:  # check if the user as inserted 2 values and the second is greater than 7
        if str(datalist[0]) == "b'Q'":  # allow to quit the app if user input capital letter Q
            print('exit!')
            sys.exit()
        ssid=datalist[0] # set the first value as the wifi name
        print(datalist[0], datalist[1])
        if str(datalist[1]) == "b'Q'": # allow to quit the app if user input capital letter Q
            print('exit!')
            sys.exit()
        passkey=datalist[1] # set the second value as the wifi psw
        
        p1 = subprocess.Popen(["wpa_passphrase", ssid, passkey], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["sudo","tee","-a","/etc/wpa_supplicant/wpa_supplicant.conf",">","/dev/null"], stdin=p1.stdout, stdout=subprocess.PIPE) # write the new credential in to wpa_supplicant.conf file
        p1.stdout.close()  # Give p1 a SIGPIPE if p2 dies.
        output,err = p2.communicate()
        sense.show_message("reboot!", text_colour=green)
        os.system('sudo shutdown -r now') # restart the device with the updated credential
    elif (len(datalist)) == 2 and (len(datalist[1])) < 7:
        print("error")
        datalist =[]
    elif (len(datalist)) == 1:# tell the user which credential to insert
        sense.show_message("insert wifi psw:", text_colour=red)
    elif (len(datalist)) == 0:
        sense.show_message("insert wifi name:", text_colour=red)

# ask the user to input the API addres via bluetooth
def insert_api():
    sense.show_message("API addres:", text_colour=red)
    data = client.recv(1024)    
    datalist.insert(0,data) # insert in to datalist 0 the API address
    if str(datalist[0]) == "b'Q'":
        print('exit!')
        sys.exit()

# retrive the mac address of the device
def Insert_username():
    data = get_mac_address()   
    datalist.insert(1,data)
    eth_mac = datalist[1] #get_mac_address()

# output data from the database for a given device mac address
def return_data(eth_mac, url):
    try:
        data = {"mac": eth_mac} # compile a dictionary for the mac address
        x = requests.post(url, data = data) # send request post to API
        message = x.text    # return the message the API has sent back
        messagedict = json.loads(message)   # unpack the json file
        dataB = messagedict['message']
        data_type = messagedict['data_type']
        print(messagedict)
        if data_type == 1: # sort the type of data and output them accordingly
            sense.show_message(dataB, text_colour=green)
        elif data_type == 2:
            if str(dataB) == 'D':
                screen_outputs.down() # Screen_output library contains the display formatting for datatype 2 and 3
                
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
           

    except (requests.exceptions.RequestException, ValueError) as e: # in case the api address is not working
        sense.show_message("Api connection failed", text_colour=red)
        print(e)
        api = insert_api()
    
    
    
while internet_on() == True and len(datalist) < 1: # tell user to insert the api address
    api = insert_api()
    print("API address: " + str(datalist[0]))
    
while internet_on() == True and len(datalist) >= 1:  # if internet is working and the api address is been inserted will try to connect to the database
    username = Insert_username()
    returnedData = return_data(datalist[1],datalist[0]) #run return_data for a given mac address and api address
    datalist.pop()
    
    
    
