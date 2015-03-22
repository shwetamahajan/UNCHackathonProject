#!/usr/bin/python
import httplib2
import time
import datetime
import urllib

# Set the request authentication headers

            # 'Api-Key': '1700022a6f05d5ed3cb6ed6c4e',
            # 'appid': appid,
            # 'application/x-wwww-form-urlencoded'
           # "content-type" : 'application/json',
appid = '406596'
headers = {'Api-Key': '62b75d4b18fa5086c767e6c004',
           "content-type" : 'application/json'
           }
data = dict(appid=appid, name="chatbot")
# Send the GET request
url = 'http://hackathonapi.inin.com/api/' + appid + "/chat/create/"    
h = httplib2.Http(".cache")
# h.add_credentials(appid, '1700022a6f05d5ed3cb6ed6c4e')
(resp, content) = h.request(url, "POST", body="{\"name\":\"chatbot\"}", headers=headers)
# (resp, content) = h.request(url, "POST", body=urllib.parse.urlencode(data), headers=headers)
print(content)
# print(resp)

# '4d2d36a7-f2e5-4f73-97d0-c64bb0799535'
