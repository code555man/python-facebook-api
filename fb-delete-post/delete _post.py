import requests

def delete_post(post_id, access_token):
    url = f"https://graph.facebook.com/v12.0/{post_id}?access_token={access_token}"
    response = requests.delete(url)
    if response.status_code == 200:
        print("Post deleted successfully.")
    else:
        print("Error deleting post. Status code:", response.status_code)
        print("Response:", response.json())

post_id = "<post id>"
access_token = "<your access token>"

delete_post(post_id, access_token)
