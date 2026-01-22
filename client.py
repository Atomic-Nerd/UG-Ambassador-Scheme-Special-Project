import requests
from helper import displayMaze

def register_user():
    url = "http://127.0.0.1:5000/register"
    data = {"username": "Jonny"}

    request = requests.post(url, json=data)

    return request.json()

def get_map():
    url = "http://127.0.0.1:5000/map"

    request = requests.get(url)
    return request.json()

def move(direction):
    url = "http://127.0.0.1:5000/move"
    data = {"direction": direction}

    request = requests.post(url, json=data)

    return request.json()

print (move('down'))
for i in range(4):
    print (move('right'))

for i in range(2):
    print (move('up'))

for i in range(5):
    print (move('right'))

displayMaze(get_map()['data']['map'])
'''
print (register_user())
displayMaze(get_map()['data']['map'])

print (move('wrong direction'))
print (move('up'))
displayMaze(get_map()['data']['map'])

print (move('right'))
displayMaze(get_map()['data']['map'])

print (move('right'))
displayMaze(get_map()['data']['map'])
'''