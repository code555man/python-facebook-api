from fbchat import Client
from fbchat.models import *
import time

email = "username"
pwd = "password"

client = Client(email,pwd)

uid_firend_list = ["100000","100000"]

for u_id in uid_firend_list:
    print('Own id: {}'.format(client.uid))
    client.send(Message(text="test"), thread_id=u_id, thread_type=ThreadType.USER)
    time.sleep(2)
client.logout() 
