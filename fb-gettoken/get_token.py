#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests, re

#  Color
###############################
W = "\033[0m"     # white
R = '\033[31;1m'  # red
G = '\033[32;1m'  # green
B = '\033[34m'    # blue
O = '\033[93m'
###############################

logo = """

 ██████╗ ███████╗████████╗    ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
██╔════╝ ██╔════╝╚══██╔══╝    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
██║  ███╗█████╗     ██║          ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
██║   ██║██╔══╝     ██║          ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
╚██████╔╝███████╗   ██║          ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
 ╚═════╝ ╚══════╝   ╚═╝          ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝               

"""

print(f"{G}{logo}")
print('[*] GET FB ACCESS TOKEN FROM COOKIE\n')
cookie = input('[*] Your Cookie : ')
try:
    data = requests.get('https://business.facebook.com/business_locations', headers = {
        'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # don't change this user agent.
        'referer'                   : 'https://www.facebook.com/',
        'host'                      : 'business.facebook.com',
        'origin'                    : 'https://business.facebook.com',
        'upgrade-insecure-requests' : '1',
        'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control'             : 'max-age=0',
        'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type'              : 'text/html; charset=utf-8'
    }, cookies = {
        'cookie'                    : cookie
    })
    find_token = re.search('(EAAG\w+)', data.text)
    results    = R + '\n[!] Fail : your cookie invalid !!' + W if (find_token is None) else G + '\n[*] Your fb access token : ' + B + find_token.group(1) + W
except requests.exceptions.ConnectionError:
    results    = R + '\n[!] Fail : no connection here !!' + W
except:
    results    = R + '\n[!] Fail : unknown errors, please try again !!' + W

print(results)