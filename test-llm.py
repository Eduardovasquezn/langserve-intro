import requests

response=requests.post(
    "http://localhost:8002/king/invoke",
    json={'input':{"chat_history":[],'text':"what did you do today?"}})

print(response.json()['output'])
