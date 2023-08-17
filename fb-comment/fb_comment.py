import requests, json

token = ""
fb_id = ""
message = ""  

res = requests.get("https://graph.facebook.com/v3.0/%s?fields=feed.limit(1)&access_token=%s"%(fb_id,token))
result = json.loads(res.text)
for post_id in result['feed']['data']:
    parameters = {'access_token' : token, 'message' : message}
    url = "https://graph.facebook.com/{0}/comments".format(post_id["id"])
    r = requests.post(url, data = parameters)
    print(r.text)
