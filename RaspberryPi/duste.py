import RPi.GPIO as GPIO
import os
import base64
import json
import requests
import time

print("Requirements Loaded")

api = 'http://13.89.58.120:8080/predict'
files=[]
headers = {}
payload = {}

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

sensor_output = 16
servo_input_1 = 19
servo_input_2 = 21
pulse_freq = 50
capture_command = "libcamera-jpeg -o garbage_image.jpg -t 5 --width 480 --height 480 --shutter 100000"
GPIO.setup(sensor_output, GPIO.IN)
GPIO.setup(servo_input_1, GPIO.OUT)
GPIO.setup(servo_input_2, GPIO.OUT)
motor1 = GPIO.PWM(servo_input_1, pulse_freq) # GPIO 19 for PWM with 50Hz
motor2 = GPIO.PWM(servo_input_2, pulse_freq) # GPIO 21 for PWM with 50Hz

#Waste Categories:
food = "0"
metal = "1"
plastic = "2"
paper = "3"

print("Variables Initialized")

def open_flap():
    print("Flap Mechanism Started")
    motor2.ChangeDutyCycle(6)
    time.sleep(1)
    motor2.ChangeDutyCycle(11)
    time.sleep(0.5)
    print("Flap Mechanism Ended")
    return

def invoke_assembly(data):
    print("Assembly Tasks Running")
    motor1.start(7.5) # Initialization
    motor2.start(11) # Initialization
    print("Mechanical Assembly Ready")
    
    if(data == food):
        print("Food Targeted")
        
    elif(data == metal):
        motor1.ChangeDutyCycle(5)
        time.sleep(0.5)
        print("Metal Targeted")
        
    elif(data == plastic):
        motor1.ChangeDutyCycle(10)
        time.sleep(0.5)
        print("Plastic Targeted")
        
    else:
        print("Paper Targeted")
    
    print("Assembly Targeting Complete")
    open_flap()
    motor1.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    print("Waste Disposed Successfully")
    motor1.ChangeDutyCycle(0)
    motor2.ChangeDutyCycle(0)
    print("Mechanical Assembly Reset and Stopped")
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
    time1 = time.time();
    response = requests.request("POST", api, headers=headers, data=payload, files=files)
    time2 = time.time();
    print("API Request Completed in " + str(time2-time1) + " Seconds")
    
    try:
        data = response.text
        print("Waste Category: " + data)
        print("Starting Assembly Task")
        invoke_assembly(data)
        print("Assembly Task Completed")
        return
        
    except requests.exceptions.RequestException:
        print("Error: " + response.text)
        
    return
    
print("Functions Loaded")
print("Starting Garbage Segregator")
print("Hi! I am Dust-E. I was built by Team SKYRaD.")
print("I am always hungry. Go ahead and give me something to munch :)")

while 1:
    if(GPIO.input(sensor_output) == 0):
        print("Waste Detected")
        segregate()

print("Garbage Segregator Operations Ended. Everything Alright")