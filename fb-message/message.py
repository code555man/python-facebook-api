import requests

def send_message(recipient_id, message_text, access_token):
    params = {
        "access_token": access_token
    }
    data = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }
    response = requests.post("https://graph.facebook.com/v12.0/me/messages", params=params, json=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message. Response:", response.text)

recipient_id = "<fb profile id>" 
message_text = "Hello, this is a test message!"
access_token = "<access token>"  
send_message(recipient_id, message_text, access_token)
