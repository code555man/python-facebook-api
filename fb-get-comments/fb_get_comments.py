import requests, json

token = "access token"
profile = "profile id"

url = f"https://graph.facebook.com/v13.0/{profile}/feed?fields=comments.limit(10)&access_token={token}"

res = requests.get(url)

comment = json.loads(res.text)

for i in comment['data'][0]['comments']['data']:

    print(i['message'], i['from']['name'])
    




        
