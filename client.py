import requests
from helper import displayMaze

url = "http://127.0.0.1:5000/register"
data = {"username": "Jonny"}

#request = requests.post(url, json=data)

url = "http://127.0.0.1:5000/map"

request = requests.get(url)
maze = request.json()["data"]["map"]

displayMaze(maze)