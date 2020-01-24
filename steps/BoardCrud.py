import requests


class BoardCrud(object):
    def __init__(self):
        self.id_board = 0
        self.name = ""
        self.key = "dbdf36f955ae385a680d31cfff5155b9"
        self.token = "072268c051c53d1ead6954957960f2b6b28ee83938f3b8dbb15fb76907609da8"
        self.url = ""
        self.response = ""

    def set_url(self, url):
        self.url = url

    def set_name(self, name):
        self.name = name

    def post_response(self):
        querystring = {"name": self.name, "defaultLabels": "true", "defaultLists": "true",
                       "keepFromSource": "none", "prefs_permissionLevel": "private", "prefs_voting": "disabled",
                       "prefs_comments": "members", "prefs_invitations": "members", "prefs_selfJoin": "true",
                       "prefs_cardCovers": "true", "prefs_background": "blue", "prefs_cardAging": "regular",
                       "key": self.key, "token": self.token}
        self.response = requests.post(self.url, querystring)
        print(self.response.json())

    def delete_response(self):
        querystring = {"key": self.key, "token": self.token}
        self.response = requests.request("DELETE", self.url, params=querystring)

    def get_response(self):
        return self.response
