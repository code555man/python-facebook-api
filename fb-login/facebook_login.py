import requests, hashlib, json

user = "phone or email"
pwd = "password"

API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":user,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+user+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET

x = hashlib.md5(bytes(sig,encoding='utf8')).hexdigest()
data.update({'sig':x})

res = requests.get('https://api.facebook.com/restserver.php',params=data)

a = json.loads(res.text)

if "access_token" in res.text:
    print(f"Login Success.")
else:
    print(f"Login Fail.")