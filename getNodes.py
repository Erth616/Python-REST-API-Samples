# [GET I-Server nodes information --> /api/monitors/iServer/nodes]
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

# [ URL --> /api/monitors/iServer/nodes]
nodes_url = base_url + "/monitors/iServer/nodes"

h1 = {
"Accept":"application/json",
"Content-Type":"application/json",
"X-MSTR-AuthToken": authToken 
}

r1 = requests.get(nodes_url, headers=h1, cookies=cookies)

print(r1.text)