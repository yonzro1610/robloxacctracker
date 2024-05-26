import requests
import json

UID = input("Enter a user ID > ")
UID2 = input("A second > ")

payload = {
    "userIds": [UID, UID2]
}

URLS = {
    "checkPresence": "https://presence.roblox.com/v1/presence/users",
    "checkFriendsPresence": f"https://friends.roblox.com/v1/users/{UID}/friends?userSort=0"
}

response = requests.post(URLS["checkPresence"], json=payload)

print(response.json())