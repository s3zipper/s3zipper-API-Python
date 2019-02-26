# -*- coding: utf-8 -*-

import requests
url = "https://api.s3zipper.com/gentoken"
payload = {'userKey': 'xxxxxxxxx', 'userSecret': 'xxxxxxxxx'} 

r = requests.request("POST", url, data=payload)
print(r.json())

d = r.json()

#Extract only the token part
token = d['token']

# save token in cookie or session for zipstart, zipstate & zipresult.
