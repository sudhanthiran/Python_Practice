import requests

url = "https://euintegration.sirioninc.net:8443/nifi-api/processors/c93e3309-eacd-1451-cbe5-4323f115574b"

payload = "{\r\n    \"revision\": {\r\n        \"clientId\": \"c93e36bd-eacd-1451-3a72-d3be3d05c9a0\",\r\n        \"version\": 1\r\n    },\r\n\r\n    \"component\": {\r\n        \"id\": \"c93e3309-eacd-1451-cbe5-4323f115574b\",\r\n        \"state\": \"RUNNING\"\r\n    }\r\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjbj1hZG1pbixvdT1wZW9wbGUsZGM9c2lyaW9uaW5jLGRjPW5ldCIsImlzcyI6IkxkYXBQcm92aWRlciIsImF1ZCI6IkxkYXBQcm92aWRlciIsInByZWZlcnJlZF91c2VybmFtZSI6ImFkbWluIiwia2lkIjoxLCJleHAiOjE1Njg4MzA5NjQsImlhdCI6MTU2ODc4Nzc2NH0.Jx1HIPwJnF8d6jAD069VW6esSmyZS4hZeaQ542pj9Hg",
    'cache-control': "no-cache",
    'Postman-Token': "de9a86bd-c5f6-4629-8f7d-387f8335adbc"
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)