import requests

def get_post_ids(access_token):
    url = f"https://graph.facebook.com/v12.0/me/feed?access_token={access_token}"
    response = requests.get(url)
    if response.status_code == 200:
        posts_data = response.json()
        post_ids = [post['id'] for post in posts_data['data']]
        return response.json()
    else:
        print("Error getting posts. Status code:", response.status_code)
        print("Response:", response.json())
        return []
    
access_token = "<access token>"

post_ids = get_post_ids(access_token)
print("Post IDs:", post_ids)
