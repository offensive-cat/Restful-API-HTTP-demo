import requests
import json

# Header and Payload goes here
url = 'https://api.restful-api.dev/objects'
headers = {"content-type": "application/json"}
payload = json.dumps({
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
})

# GET
r = requests.get(url)
print('\nMETHOD : GET')
print(r)
print(r.json())

# POST
r = requests.post(url, data = payload, headers = headers)
print('\nMETHOD : POST')
print(r)
print(r.json())

# url + idObj
idObj = r.json()['id']
url = url + '/' + idObj

# PUT
r = requests.put(url, data = payload, headers = headers)
print('\nMETHOD : PUT')
print(r)
print(r.json())

# DELETE
r = requests.delete(url, data = payload, headers = headers)
print('\nMETHOD : DELETE')
print(r)
print(r.json())

input()