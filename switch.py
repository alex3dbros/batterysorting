import RPi.GPIO as GPIO
from time import sleep  # this lets us have a time delay (see line 15)

GPIO.setmode(GPIO.BCM)  # set up BCM GPIO numbering

x_switch = 17
y_switch = 27
z_switch = 22

GPIO.setup(x_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP) # X switch
GPIO.setup(y_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Y switch
GPIO.setup(z_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Z switch

try:
    while True:  # this will carry on until you hit CTRL+C
        if GPIO.input(x_switch):
            print("pressed x")

        if GPIO.input(y_switch):
            print("pressed y")

        if GPIO.input(z_switch):
            print("pressed z")

        sleep(0.1)  # wait 0.1 seconds

finally:  # this block will run no matter how the try block exits
    GPIO.cleanup()  # clean up after yourself