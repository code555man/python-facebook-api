import requests,json
from requests.api import get

token = "your_token"


def get_friends(token,limit):

    url = "https://graph.facebook.com/me/friends?limit="+str(limit)+"&access_token="+token
    res = requests.get(url)
    f = open("list.txt", "w")
    for data in json.loads(res.text)['data']:
        f.write("{:15} = {}\n".format(data["id"],data["name"]))
    f.close()

get_friends(token,10)
