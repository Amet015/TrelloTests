import requests


def main():
    post_board()
    get_board()


def post_board():
    url = "https://api.trello.com/1/boards/"
    querystring = {"name": "TestWithPython", "defaultLabels": "true", "defaultLists": "true", "keepFromSource": "none",
                   "prefs_permissionLevel": "private", "prefs_voting": "disabled", "prefs_comments": "members",
                   "prefs_invitations": "members", "prefs_selfJoin": "true", "prefs_cardCovers": "true",
                   "prefs_background": "blue", "prefs_cardAging": "regular",
                   "key": "dbdf36f955ae385a680d31cfff5155b9",
                   "token": "072268c051c53d1ead6954957960f2b6b28ee83938f3b8dbb15fb76907609da8"}
    response = requests.request("POST", url, params=querystring)
    print(response.text)


def get_board():
    url = "https://api.trello.com/1/boards/DKgRiAiy"
    querystring = {"actions": "all", "boardStars": "none", "cards": "none", "card_pluginData": "false",
                   "checklists": "none", "customFields": "false",
                   "fields": "name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames",
                   "lists": "open", "members": "none", "memberships": "none", "membersInvited": "none",
                   "membersInvited_fields": "all", "pluginData": "false", "organization": "false",
                   "organization_pluginData": "false", "myPrefs": "false", "tags": "false",
                   "key": "dbdf36f955ae385a680d31cfff5155b9",
                   "token": "072268c051c53d1ead6954957960f2b6b28ee83938f3b8dbb15fb76907609da8"}
    response = requests.request("GET", url, params=querystring)
    print(response.text)


def put_board():
    url = "https://api.trello.com/1/boards/DKgRiAiy"
    querystring = {"name": "testChangeName", "key": "dbdf36f955ae385a680d31cfff5155b9",
                   "token": "dbdf36f955ae385a680d31cfff5155b9"}
    response = requests.request("PUT", url, params=querystring)

    print(response.text)


if __name__ == '__main__':
    main()
