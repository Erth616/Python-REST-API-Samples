# [GET I-Server nodes information]

import requests
import json

base_url = "http://localhost:8080/MicroStrategyLibrary/api"

# [GENERATE AUTH TOKEN]

auth_url = base_url + "/auth/login"

username = "administrator"
password = ""

body = {
    'username': username,
    'password': password,
    'loginMode': 1
    }

r = requests.post(auth_url, data=body)

# [ Auth Token and Session Cookie for subsequent requests]

authToken = r.headers['X-MSTR-AuthToken']
cookies = dict(r.cookies)

# [ GET I SERVER NODE INFO --> /api/monitors/iServer/nodes]

nodes_url = base_url + "/monitors/iServer/nodes"

# WAS-PSALAZAR6 Tutorial ID --> B19DEDCC11D4E0EFC000EB9495D0F44F

h1 = {
"Accept":"application/json",
"Content-Type":"application/json",
"X-MSTR-AuthToken": authToken 
}

r1 = requests.get(nodes_url, headers=h1, cookies=cookies)

print(r1.text)

# r2 = requests.post(uri, headers=h2, data=b2)
