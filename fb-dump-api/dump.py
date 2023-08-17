import requests,json

def get_friends(token,limit):
    url = "https://graph.facebook.com/me/friends?limit="+str(limit)+"&access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_posts(token):
    # link = "https://graph.facebook.com/v5.0/uid/posts?access_token="
    url = "https://graph.facebook.com/me/posts?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text)) 

def get_feed(token):
    url = "https://graph.facebook.com/me/feed?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_photos(token):
    url = "https://graph.facebook.com/me/photos?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_albums(token):
    url = "https://graph.facebook.com/me/albums?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_videos(token):
    url = "https://graph.facebook.com/me/videos?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_events(token):
    url = "https://graph.facebook.com/me/events?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_groups(token):
    url = "https://graph.facebook.com/me/groups?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_checkins(token):
    url = "https://graph.facebook.com/me/checkins?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_likes(token):
    url = "https://graph.facebook.com/me/likes?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_music(token):
    url = "https://graph.facebook.com/me/music?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_books(token):
    url = "https://graph.facebook.com/me/books?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_movies(token):
    url = "https://graph.facebook.com/me/movies?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_television(token):
    url = "https://graph.facebook.com/me/television?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_games(token):
    url = "https://graph.facebook.com/me/games?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_about(token):
    url = "https://graph.facebook.com/me/about?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_bio(token):
    url = "https://graph.facebook.com/me/bio?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_quotes(token):
    url = "https://graph.facebook.com/me/quotes?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_sports(token):
    url = "https://graph.facebook.com/me/sports?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_favorite_athletes(token):
    url = "https://graph.facebook.com/me/favorite_athletes?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_favorite_teams(token):
    url = "https://graph.facebook.com/me/favorite_teams?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_inspirational_people(token):
    url = "https://graph.facebook.com/me/inspirational_people?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_family(token):
    url = "https://graph.facebook.com/me/family?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_work(token):
    url = "https://graph.facebook.com/me/work?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text)) 

def get_education(token):
    url = "https://graph.facebook.com/me/education?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_location(token):
    url = "https://graph.facebook.com/me/location?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_hometown(token):
    url = "https://graph.facebook.com/me/hometown?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_phone(token):
    url = "https://graph.facebook.com/100018342640179/phone?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))

def get_website(token):
    url = "https://graph.facebook.com/me/website?access_token="+token
    res = requests.get(url)
    print(json.loads(res.text))
