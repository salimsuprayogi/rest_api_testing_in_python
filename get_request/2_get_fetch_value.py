#!python3
# -*- coding: utf-8 -*-
# apitesting
# 01 Januay 2021
# Salim Suprayogi

import requests
import json
import jsonpath

"""
Endpoint : https://reqres.in/api/users?page=2 [ Method Get ]
Data :
{
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}
"""

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)

# Parse response to Json Format
json_response = json.loads(response.text)
# print(json_response)

# Fetc value Using Json Patch
page = jsonpath.jsonpath(json_response,"page") # return Data Type is list
per_page = jsonpath.jsonpath(json_response,"per_page")
total = jsonpath.jsonpath(json_response,"total")
total_pages = jsonpath.jsonpath(json_response,"total_pages")
data = jsonpath.jsonpath(json_response,"data")

# Validation
print("Page:",page[0])
try:
    assert page[0] == 2
    print("Result :", page[0])
    print("Status : Success")
except AssertionError:
    print("Result :", page[0])
    print("Status : Failed")
    
print("per_page:",per_page[0])
try:
    assert per_page[0] == 6
    print("Result :", per_page[0])
    print("Status : Success")
except AssertionError:
    print("Result :", per_page[0])
    print("Status : Failed")

print("total:",total[0])
try:
    assert total[0] == 12
    print("Result :", total[0])
    print("Status : Success")
except AssertionError:
    print("Result :", total[0])
    print("Status : Failed")

print("total_pages:",total_pages[0])
try:
    assert total_pages[0] == 2
    print("Result :", total_pages[0])
    print("Status : Success")
except AssertionError:
    print("Result :", total_pages[0])
    print("Status : Failed")
    
print("data:",data[0])
