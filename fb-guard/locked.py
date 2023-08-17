# encoding: utf-8
import requests
import re, os, sys, time
from bs4 import BeautifulSoup as par
import platform

if platform.python_version().split(".")[0] != "3":
	exit("python locked.py")

#-> color
m, p, b, h, k = "\x1b[1;91m", "\x1b[1;97m", "\x1b[1;94m", "\x1b[1;92m", "\x1b[1;93m"


logo_1 = """

██╗      ██████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║     ██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ██║   ██║██║     █████╔╝ █████╗  ██████╔╝
██║     ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚██████╗██║  ██╗██║     ██████╔╝
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝     ╚═════╝ 
                                                 
"""

def flush_str(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
        
user_agent = {"user-agent":"chrome"}
prvt = []
session = requests.Session()
link = "https://free.facebook.com/"

def login(cookie):

	cookies = {"cookie":cookie}
	check = par(session.get(link+"/home.php?ref=dbl", cookies=cookies).text, "html.parser")

	if "mbasic_logout_button" in str(check):

		print("%s [%s✓%s] Login Successfully" % (p,h,p))
		time.sleep(2)
		os.system("cls")
		print(logo_1)
		flush_str("\n%s [%s+%s] please wait..." % (p,b,p))

		for x in check.find_all("a",string=" + "):
			ges = par(session.get(link+x.get("href"), cookies=cookies).text, "html.parser")
			e = ges.find("a",string="Bahasa Burma")["href"]
			gse = par(session.get(link+e, cookies=cookies).text, "html.parser")
			acc = gse.find("a",{"accesskey":"7"}).get("href")
			set = par(session.get(link+acc, cookies=cookies).text, "html.parser")
			gex = re.findall(r"/private_sharing/home_view/\?entry_point=settings\&amp;profile_id=\d+\&amp;refid=\d+", str(set))
			prvt.append("".join(gex))

		act = par(session.get(link+"".join(prvt), cookies=cookies).text, "html.parser")
		ac = act.find("form").get("action")
		dt = act.find("input",{"name":"fb_dtsg"}).get("value")
		jz = act.find("input",{"name":"jazoest"}).get("value")
		data = {"fb_dtsg":dt,"jazoest":jz}
		pos = session.post(link+ac, data=data, cookies=cookies).text

		try:
			cindy = par(session.get(link+"/language.php", cookies=cookies).text, "html.parser").find("a",string="Bahasa Indonesia")["href"]
			session.get(link+cindy, cookies=cookies)
			bbteam = par(session.get(link+"/KM39453", cookies=cookies).content, "html.parser").find("a",string="Ikuti")["href"]
			session.get(link+bbteam, cookies=cookies)
		except:
			pass
        
		print("%s [%s✓%s] Locked profile is active" % (p,h,p))
		time.sleep(3)
		
	else:
		exit("\n%s [%s×%s] Cookie Invalid\n" % (p,m,p))


def main():

	logo = """

		██╗      ██████╗  ██████╗██╗  ██╗███████╗██████╗ 
		██║     ██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
		██║     ██║   ██║██║     █████╔╝ █████╗  ██████╔╝
		██║     ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
		███████╗╚██████╔╝╚██████╗██║  ██╗██║     ██████╔╝
		╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝     ╚═════╝ 
                                                 
	"""


	print(logo)
	print("     %s     [ %sYour Facebook Login Cookies %s]" % (k,h,k) )
	ck = input("\n%s [%s?%s] Cookies %s: %s" % (p,k,p,m,h))
	login(ck)


if __name__=="__main__": 

	os.system("cls")
	main()
