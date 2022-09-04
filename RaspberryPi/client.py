import base64
import json                    
import requests

api = 'http://13.89.58.120:8080/predict'
#image_file = 'test.jpg'

files=[
  ('file',('image46.jpg',open('/home/admin/hackathon/WasteSegregator/RaspberryPi/image46.jpg','rb'),'image/jpg'))
]


#with open(image_file, "rb") as f:
#    im_bytes = f.read()
#im_b64 = base64.b64encode(im_bytes).decode("utf8")

headers = {} #{'Content-type': 'application/json', 'Accept': 'text/plain'}
  
payload = {} #json.dumps({"image": im_b64, "other_key": "value"})

print("Process Started")
#response = requests.post(api, data=payload, headers=headers, im_bytes)
#response = requests.get(api)
response = requests.request("POST", api, headers=headers, data=payload, files=files)

try:
    #data = response.json()
    data = response.text
    print(data)                
except requests.exceptions.RequestException:
    print(response.text)
    
print("Process Ended")
