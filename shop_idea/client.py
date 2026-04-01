import requests 

url = "http://192.168.1.147:67"

while True:
    print (requests.get(url + "/shop"))
    