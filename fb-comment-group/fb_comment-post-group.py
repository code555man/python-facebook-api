import requests

# ระบุ Access Token, Group ID, และ Post ID ของคุณ
access_token = ''
group_id = ''
post_id = ''
comment_text = 'test auto comment'

def post_comment():
    url = f'https://graph.facebook.com/{group_id}_{post_id}/comments'
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    data = {
        'message': comment_text,
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print('คอมเมนต์ถูกโพสต์สำเร็จ.')
    else:
        print(f'ข้อผิดพลาด: {response.status_code}')
        print(response.text)


post_comment()