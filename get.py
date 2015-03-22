#!/usr/bin/python
import httplib2
import time
import datetime

# Set the request authentication headers

            # 'Api-Key': '1700022a6f05d5ed3cb6ed6c4e',
            # 'appid': appid,
           # "content-type" : 'application/json',
appid = '406596'
headers = { 'Api-Key': '62b75d4b18fa5086c767e6c004',
           "content-type" : 'application/json'
           }

# Send the GET request
# data = dict()
url = 'http://hackathonapi.inin.com/api/' + appid + "/chat/poll/"  + "b8ecf6c2-a119-418a-b9a3-2d4899f31afe"
h = httplib2.Http(".cache")
# h.add_credentials(appid, '1700022a6f05d5ed3cb6ed6c4e')
(resp, content) = h.request(url, "GET", headers=headers)
print(content)
# print(resp)

# '4d2d36a7-f2e5-4f73-97d0-c64bb0799535'
