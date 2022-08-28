import base64
import json                    

import requests

api = 'http://10.105.24.44:8080/index'
image_file = 'test.jpg'

print("started")
response = requests.get(api)
print(response)
print("ended")

with open(image_file, "rb") as f:
    im_bytes = f.read()
im_b64 = base64.b64encode(im_bytes).decode("utf8")

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
payload = json.dumps({"image": im_b64, "other_key": "value"})
response = requests.get(api) #, data=payload, headers=headers)

try:
    data = response.json()     
    print(data)                
except requests.exceptions.RequestException:
    print(response.text)
