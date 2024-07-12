import requests, time

token = "access token"
link = "link post"

url = f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}"


for _ in range(100):
    res = requests.post(url)
    print(res.text)
    time.sleep(0.5)

