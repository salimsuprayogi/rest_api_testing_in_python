#!python3
# -*- coding: utf-8 -*-
# apitesting
# 01 Januay 2021
# Salim Suprayogi

import requests
import json
import jsonpath

"""
1. Read Input json from file
2. Parse into json format
3. Hit post method
4. Parse response to json format
5. Validate response

Endpoint : hhttps://reqres.in/api/users [ Method Post ]
Status : 201
Response :
{
    "name": "morpheus",
    "job": "leader",
    "id": "585",
    "createdAt": "2021-01-01T09:29:35.458Z"
}
"""

# API URL
url = "https://reqres.in/api/users"

# Read input Json File
file = open("..\get_method\data_create_user.json", "r")
json_input = file.read()
# print(json_input) # ceck read json
request_json = json.loads(json_input)
# print(request_json) # cekc load json

# Make POST request with Json Input Body
response = requests.post(url, request_json)
# print(response.content) # Result : {"name":"morpheus","job":"leader","id":"392","createdAt":"2021-01-01T09:42:31.613Z"}

# Validation Status Code
try:
    assert response.status_code == 201
    print("Result :", response.status_code)
    print("Status : Success")
except AssertionError:
    print("Result :", response.status_code)
    print("Status : Failed")

# Fecth header from Response
header = response.headers  # ceck header
# print("Headaers:", header)
# fetch content length from header
content_lengt = response.headers.get("Content-Length")
# print("Content-Length:", content_lengt)

# Parse response to Json Format
response_json = json.loads(response.text)
print("Result Request:",response_json) # format json

# Pick Data User using Json Path
name = jsonpath.jsonpath(response_json,"name") # return data type is list
job = jsonpath.jsonpath(response_json,"job") # return data type is list
id_user = jsonpath.jsonpath(response_json,"id") # return data type is list
created_at = jsonpath.jsonpath(response_json,"createdAt") # return data type is list

name_user = name[0]
job_user = job[0]
result_id = id_user[0]
created_at_user = created_at[0]

print("name:", name_user)
print("job:", job_user)
print("result_id:", result_id)
print("created_at:", created_at_user)