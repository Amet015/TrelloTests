import requests

url = "https://api.trello.com/1/boards/"

querystring = {"name": "testwithjason", "defaultLabels": "true", "defaultLists": "true", "keepFromSource": "none",
               "prefs_permissionLevel": "private", "prefs_voting": "disabled", "prefs_comments": "members",
               "prefs_invitations": "members", "prefs_selfJoin": "true", "prefs_cardCovers": "true",
               "prefs_background": "blue", "prefs_cardAging": "regular", "key": "dbdf36f955ae385a680d31cfff5155b9", "token": "072268c051c53d1ead6954957960f2b6b28ee83938f3b8dbb15fb76907609da8"}

response = requests.request("POST", url, params=querystring)

print(response.json())
