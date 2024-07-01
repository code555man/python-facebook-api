import requests

access_token = '<access token>'

message = 'test auto post facebook from api'

url = f'https://graph.facebook.com/me/feed'

params = {
    'access_token': access_token,
    'message': message
}

response = requests.post(url, data=params)

if response.status_code == 200:
    print("Post created successfully!")
else:
    print("Error creating post:", response.text)

