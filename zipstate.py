#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

token = token # Get it from cookie or session

myurl = "https://api.s3zipper.com/v1/zipstate"

bearer = 'Bearer {}'.format(token)
headers={'Content-Type':'application/json; charset=UTF-8',
         "Authorization": bearer }

payload = zipstart_output # Get it from cookie or session

r = requests.request("POST", myurl, data=payload ,headers=headers)

zipstate_output = r.text
print(zipstate_output)
