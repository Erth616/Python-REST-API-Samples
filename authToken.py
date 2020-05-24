# Generate Auth Token and Session Cookies
# https://github.com/MicroStrategy/mstrio-py
# pip3 install mstrio-py
import requests

base_url="http://localhost:8080/MicroStrategyLibrary/api"

auth_url = base_url + "/auth/login"

username = "administrator"
password = ""

body = {
    'username': username,
    'password': password,
    'loginMode': 1
    }

r1 = requests.post(auth_url, data=body)

# [Pass AuthToken and Cookies in ALL subsequent requests]
# EG --> r = requests.get(url, headers=h1, cookies=c1)

authToken = r1.headers['X-MSTR-AuthToken']
cookies = dict(r1.cookies)
