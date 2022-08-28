import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

sensor_output = 16
object_count_till_now = 0;

GPIO.setup(sensor_output, GPIO.IN)

while 1:
    if(GPIO.input(sensor_output) == 0):
        print("Object Detected")
        object_count_till_now += 1
        
    else:
        print("No Object Detected")
        
    print(object_count_till_now)