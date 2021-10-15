
import requests

eth_mac = input("email:")
print(eth_mac)

url = 'http://127.0.0.1:5001/'
myobj = eth_mac
data = {"eventType": myobj}
x = requests.post(url, data = data)

#print the response text (the content of the requested file):

print(x.text)