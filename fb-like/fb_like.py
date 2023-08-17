import requests, json

# type reaction

# reaction 'LOVE'
# reaction 'WOW'
# reaction 'HAHA'
# reaction 'SAD'
# reaction 'LIKE'
# reaction 'ANGRY'

token = ""
fb_target_id = ""
reaction_type = "LIKE"

res = requests.get("https://graph.facebook.com/v3.0/%s?fields=feed.limit(10)&access_token=%s"%(fb_target_id,token))
result = json.loads(res.text)
for post_id in result['feed']['data']:
    parameters = {'access_token' : token , 'type' : reaction_type}
    url = "https://graph.facebook.com/{0}/reactions".format(post_id['id'])
    s = requests.post(url, data = parameters)
    print(s.text)
