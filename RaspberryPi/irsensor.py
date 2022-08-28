import RPi.GPIO as GPIO
import os


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

sensor_output = 16
image_count = 42
capture_command_base = "libcamera-jpeg -o image"
capture_command_parameters = "-t 5 --width 480 --height 480 --shutter 100000"

GPIO.setup(sensor_output, GPIO.IN)

while 1:
    if(GPIO.input(sensor_output) == 0):
        print("Object Detected")
        capture_command_final = capture_command_base + str(image_count) + ".jpg" + " " + capture_command_parameters;
        os.system(capture_command_final)
        image_count += 1
        
        
    else:
        print("No Object Detected")