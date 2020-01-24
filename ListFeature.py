import requests
import json


def main():
    post_list()
    # get_list()


def post_list():
    url = "https://api.trello.com/1/lists"
    querystring = {"name": "restponsePOST", "idBoard": "5e2adce2ddb6038a18305c68", "key": "dbdf36f955ae385a680d31cfff5155b9",
                   "token": "072268c051c53d1ead6954957960f2b6b28ee83938f3b8dbb15fb76907609da8"}
    response = requests.request("POST", url, params=querystring)
    res = response.json()
    print(res['idBoard'], res['name'])
    print(response.text)


def get_list():
    url = "https://api.trello.com/1/lists/5e2af8a7288ddf065cf7e49d"
    querystring = {"fields": "name,closed,idBoard,pos", "key": "dbdf36f955ae385a680d31cfff5155b9",
                   "token": "072268c051c53d1ead6954957960f2b6b28ee83938f3b8dbb15fb76907609da8"}
    response = requests.get(url, params=querystring)
    res = response.json()
    print(type(response))
    print()
    print(response.status_code)
    print(res['id'])


def put_list():
    url = "https://api.trello.com/1/lists/id"

    querystring = {"name": "NewNameList", "key": "dbdf36f955ae385a680d31cfff5155b9",
                   "token": "072268c051c53d1ead6954957960f2b6b28ee83938f3b8dbb15fb76907609da8"}
    response = requests.request("PUT", url, params=querystring)
    print(response.json())


if __name__ == '__main__':
    main()
