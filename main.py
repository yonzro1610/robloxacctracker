UID = input("Enter a user ID > ")

URLS = {
    "checkPresence": "https://presence.roblox.com/v1/presence/users",
    "checkFriendsPresence": f"https://friends.roblox.com/v1/users/{UID}/friends?userSort=0"
}

