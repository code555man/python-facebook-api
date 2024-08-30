import requests

# Replace with your actual Access Token and Group ID
access_token = 'access_token'
group_id = 'group_id'

# Function to get all posts in a group
def get_all_posts(access_token, group_id):
    url = f'https://graph.facebook.com/v14.0/{group_id}/feed'
    posts = []
    params = {'access_token': access_token}

    while True:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f'Failed to get posts. Status code: {response.status_code}')
            print('Response:', response.json())
            break

        data = response.json()
        posts.extend(data.get('data', []))

        next_page = data.get('paging', {}).get('next')
        if not next_page:
            break
        url = next_page

    return posts

print(get_all_posts(access_token, group_id))

# Function to delete a post
def delete_post_group(access_token, post_id):
    url = f'https://graph.facebook.com/v14.0/{post_id}'
    response = requests.delete(url, params={'access_token': access_token})
    return response.status_code == 200

# Get all posts in the group
posts = get_all_posts(access_token, group_id)

# Delete each post
for post in posts:
    post_id = post['id']
    if delete_post_group(access_token, post_id):
        print(f'Successfully deleted post {post_id}')
    else:
        print(f'Failed to delete post {post_id}')

print('All posts processed.')
