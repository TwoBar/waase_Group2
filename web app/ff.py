import json
import requests

eth_mac = input("email:") #get_mac_address()

url = 'http://127.0.0.1:5001/'
myobj = eth_mac
data = {"mac": myobj}
x = requests.post(url, data = data)

message = x.text
messagedict = json.loads(message)

lastname = messagedict['message']
print(lastname)