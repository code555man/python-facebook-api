import requests

access_token = '<your access token>'
group_id = '<group id>'

post_data = {
    'message': '<Your message here>',
    'link': '<your link>', 
    'access_token': access_token
}

url = f'https://graph.facebook.com/{group_id}/feed'

response = requests.post(url, data=post_data)

if response.status_code == 200:
    print('Post shared successfully!')
else:
    print('Error:', response.json())
