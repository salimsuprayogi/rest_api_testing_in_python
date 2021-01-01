#!python3
# -*- coding: utf-8 -*-
# apitesting
# 01 Januay 2021
# Salim Suprayogi

import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)
print(response) # result = <Response [200]>

# Display Response Content
print("content = ", response.content)

# Display Response Header
print("headers = ", response.headers)

# Display Status Code
print("status_code = ", response.status_code)
