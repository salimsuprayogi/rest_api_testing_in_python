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
response = requests.delete(url)

#Fetch Response Code
# print(response.status_code)

# Validation
try:
    assert response.status_code == 204
    print("Result :", response.status_code)
    print("Status : Success")
except AssertionError:
    print("Result :", response.status_code)
    print("Status : Failed")