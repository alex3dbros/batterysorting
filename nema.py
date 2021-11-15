import RPi.GPIO as GPIO
import time
import sys


class Nema(object):

    def __init__(self, direction_pin, step_pin, axis):
        self.direction_pin = direction_pin
        self.step_pin = step_pin
        self.axis = axis
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.x_switch = 17
        self.y_switch = 27
        self.z_switch = 22

        GPIO.setup(self.x_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # X switch
        GPIO.setup(self.y_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Y switch
        GPIO.setup(self.z_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Z switch

    def check_switch(self, axis):

        switch_pressed = False
        count = 0
        if axis == "X" and GPIO.input(self.x_switch):
            for i in range(100):
                if GPIO.input(self.x_switch):
                    count += 1
            if count > 90:
                switch_pressed = True

            return switch_pressed

        if axis == "Y" and GPIO.input(self.y_switch):
            for i in range(100):
                if GPIO.input(self.y_switch):
                    count += 1
            if count > 90:
                switch_pressed = True

            return switch_pressed

        if axis == "Z" and GPIO.input(self.z_switch):
            for i in range(100):
                if GPIO.input(self.z_switch):
                    count += 1
            if count > 90:
                switch_pressed = True

            return switch_pressed


    def motor_zero(self):

        delay = 0.1 / 1000

        clockwise = False

        if self.axis == "X":
            clockwise = False

        if self.axis == "Y":
            clockwise = True

        if self.axis == "Z":
            clockwise = False

        # setup GPIO
        GPIO.setup(self.direction_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.output(self.direction_pin, clockwise)
        try:
            time.sleep(.05)

            for i in range(5000000):
                GPIO.output(self.step_pin, True)
                time.sleep(delay)
                GPIO.output(self.step_pin, False)
                time.sleep(delay)

                if self.axis == "X" and self.check_switch("X"):
                    print("X Switch pressed, reversing and stopping motion")
                    GPIO.output(self.direction_pin, True)
                    for i in range(200):
                        GPIO.output(self.step_pin, True)
                        time.sleep(delay)
                        GPIO.output(self.step_pin, False)
                        time.sleep(delay)
                    break

                if self.axis == "Y" and self.check_switch("Y"):
                    print("Y Switch pressed, stopping motion and getting back")

                    GPIO.output(self.direction_pin, False)
                    for i in range(200):
                        print("Getting back")
                        GPIO.output(self.step_pin, True)
                        time.sleep(delay)
                        GPIO.output(self.step_pin, False)
                        time.sleep(delay)
                    break

                if self.axis == "Z" and self.check_switch("Z"):
                    print("Z Switch pressed, stopping motion and getting back")
                    GPIO.output(self.direction_pin, True)
                    for i in range(200):
                        GPIO.output(self.step_pin, True)
                        time.sleep(delay)
                        GPIO.output(self.step_pin, False)
                        time.sleep(delay)
                    break



        except KeyboardInterrupt:
            print("User Keyboard Interrupt : RpiMotorLib:")
        except Exception as motor_error:
            print(sys.exc_info()[0])
            print(motor_error)
            print("RpiMotorLib  : Unexpected error:")
        finally:
            # cleanup
            GPIO.output(self.step_pin, False)
            GPIO.output(self.direction_pin, False)

    def motor_go(self, steps, stepdelay, verbose, initdelay):
        clockwise = None
        direction = ""

        if steps > 0:
            direction = "backward"


        if steps < 0:
            direction = "forward"
            steps = steps * -1

        if self.axis == "X" and direction == "forward":
            clockwise = True

        if self.axis == "Y" and direction == "forward":
            clockwise = False

        if self.axis == "Z" and direction == "forward":
            clockwise = True

        if self.axis == "A" and direction == "forward":
            clockwise = True



        if self.axis == "X" and direction == "backward":
            clockwise = False

        if self.axis == "Y" and direction == "backward":
            clockwise = True

        if self.axis == "Z" and direction == "backward":
            clockwise = False


        if self.axis == "A" and direction == "backward":
            clockwise = False



        if clockwise is None:
            print("Invalid Direction, aborting")
            return

        # setup GPIO
        GPIO.setup(self.direction_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.output(self.direction_pin, clockwise)
        try:
            time.sleep(initdelay)

            for i in range(steps):
                GPIO.output(self.step_pin, True)
                time.sleep(stepdelay)
                GPIO.output(self.step_pin, False)
                time.sleep(stepdelay)
                if verbose:
                    print("Steps count {}".format(i))

                if self.axis == "X" and self.check_switch("X"):
                    print("X Switch pressed, stopping motion")
                    break

                if self.axis == "Y" and self.check_switch("Y"):
                    print("Y Switch pressed, stopping motion")
                    break

                if self.axis == "Z" and self.check_switch("Z"):
                    print("Z Switch pressed, stopping motion")
                    break


        except KeyboardInterrupt:
            print("User Keyboard Interrupt : RpiMotorLib:")
        except Exception as motor_error:
            print(sys.exc_info()[0])
            print(motor_error)
            print("RpiMotorLib  : Unexpected error:")

        finally:
            # cleanup
            GPIO.output(self.step_pin, False)
            GPIO.output(self.direction_pin, False)