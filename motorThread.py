import threading
import nema as nm


pins = {"dirX": 21, "stepX": 20, "dirY": 16, "stepY": 12, "dirZ": 25, "stepZ": 24, "dirA": 26, "stepA": 19}

threadLock = threading.Lock()



class MotorRun (threading.Thread):
    def __init__(self, threadID, name, steps, speed):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.steps = steps
        self.speed = speed
        self.GPIO_pins = (9, 9, 9)

    def run(self):

        delay = 0.1 / self.speed

        if self.name == "X":
            mymotor = nm.Nema(pins["dirX"], pins["stepX"], self.name)
            mymotor.motor_go(self.steps, delay, False, .05)

        if self.name == "Y":
            mymotor = nm.Nema(pins["dirY"], pins["stepY"], self.name)
            mymotor.motor_go(self.steps, delay, False, .05)

        if self.name == "Z":
            mymotor = nm.Nema(pins["dirZ"], pins["stepZ"], self.name)
            mymotor.motor_go(self.steps, delay, False, .05)

        if self.name == "A":
            mymotor = nm.Nema(pins["dirA"], pins["stepA"], self.name)
            mymotor.motor_go(self.steps, delay, False, .05)

        print ("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        # print_time(self.name, self.counter, 3)
        # # Free lock to release next thread
        threadLock.release()


class MotorZero (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.GPIO_pins = (9, 9, 9)

    def run(self):
        if self.name == "X":
            mymotor = nm.Nema(pins["dirX"], pins["stepX"], self.name)
            mymotor.motor_zero()

        if self.name == "Y":
            mymotor = nm.Nema(pins["dirY"], pins["stepY"], self.name)
            mymotor.motor_zero()

        if self.name == "Z":
            mymotor = nm.Nema(pins["dirZ"], pins["stepZ"], self.name)
            mymotor.motor_zero()



        print ("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        # print_time(self.name, self.counter, 3)
        # # Free lock to release next thread
        threadLock.release()
