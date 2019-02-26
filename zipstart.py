#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

token = token # Get it from cookie or session

myurl = "https://api.s3zipper.com/v1/zipstart"
bearer = 'Bearer {}'.format(token)
headers={"Authorization": bearer }

payload = {'awsKey':    'xxxx',
           'awsSecret': 'xxxx',
           'awsBucket': 'my-bucket',
           'awsRegion': 'us-east-1',
           'filePaths': ['my-bucket/path/to/file/one', 'my-bucket/path/to/file/two', 'my-bucket/path/to/folder']} #backend expects a list


r = requests.request("POST", myurl, data=payload ,headers=headers)

#Get raw text and save it
zipstart_output = r.text

print(zipstart_output)

#save zipstart_output "as is" for zipstate & zipresult
