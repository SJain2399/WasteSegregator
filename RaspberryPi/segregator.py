import RPi.GPIO as GPIO
import os
import base64
import json                    
import requests
from time import sleep

print("Requirements Loaded")

api = 'http://13.89.58.120:8080/predict'
files=[]
headers = {}
payload = {}

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

sensor_output = 16
servo_input_1 = 19
servo_input_2 = 30
pulse_freq = 50
capture_command = "libcamera-jpeg -o garbage_image.jpg -t 5 --width 480 --height 480 --shutter 100000"
GPIO.setup(sensor_output, GPIO.IN)
GPIO.setup(servo_input_1, GPIO.OUT)
motor1 = GPIO.PWM(servo_input_1, pulse_freq) # GPIO 17 for PWM with 50Hz
motor1.start(7.5) # Initialization

#Waste Categories:
food = "0"
metal = "1"
plastic = "2"
paper = "3"

print("Variables Initialized")

def open_flap():
    print("Flap Mechanism")
    return

def invoke_assembly(data):
    print("Assembly Task Running")
    print("Mechanical Assembly Ready")
    
    if(data == food):
        print("Food Targeted")
        
    elif(data == metal):
        motor1.ChangeDutyCycle(5)
        sleep(0.5)
        motor1.ChangeDutyCycle(7.5)
        sleep(0.5)
        print("Metal Targeted")
        
    elif(data == plastic):
        motor1.ChangeDutyCycle(10)
        sleep(0.5)
        motor1.ChangeDutyCycle(7.5)
        sleep(0.5)
        print("Plastic Targeted")
        
    else:
        print("Paper Targeted")
    
    print("Assembly Targeting Complete")
    open_flap()
    print("Waste Disposed Successfully")
    return

def segregate():
    print("Camera Started")
    os.system(capture_command)
    print("Capture Completed")
    
    files=[
      ('file',('garbage_image.jpg',open('/home/admin/hackathon/WasteSegregator/RaspberryPi/garbage_image.jpg','rb'),'image/jpg'))
    ]
    print("Image File Loaded")
    
    print("API Request Invoked")
    response = requests.request("POST", api, headers=headers, data=payload, files=files)
    print("API Request Completed")
    
    try:
        data = response.text
        print("Waste Category: " + data)
        print("Starting Assembly Task")
        invoke_assembly(data)
        print("Assembly Task Completed")
        
    except requests.exceptions.RequestException:
        print("Error: " + response.text)
        
    return
    
print("Functions Loaded")
print("Starting Garbage Segregator")

while 1:
    print("IR Detection Cycle Started")
    
    if(GPIO.input(sensor_output) == 0):
        print("Waste Detected")
        segregate()
        
    else:
        print("No Waste Detected")
        
    print("IR Detection Cycle Complete. Everything OK")