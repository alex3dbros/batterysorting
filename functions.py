import motorThread as motor_control

threads = []

def find_zero():

    threadX = motor_control.MotorZero(1, "X")
    threadX.start()
    threads.append(threadX)

    threadY = motor_control.MotorZero(2, "Y")
    threadY.start()
    threads.append(threadY)

    threadZ = motor_control.MotorZero(3, "Z")
    threadZ.start()
    threads.append(threadZ)

    for t in threads:
        t.join()
    print ("Exiting Main Thread")


def move(axis, position, current_position):
    steps_permm = 1
    speed = 1000
    if axis == "X" or axis == "Y":
        steps_permm = 26.66

    if axis == "Z":
        speed = 5000
        steps_permm = 198.591

    steps = (current_position * steps_permm) - (steps_permm * position)
    print(steps)
    # steps = current_position - position

    threadX = motor_control.MotorRun(1, axis, int(steps), speed)
    threadX.start()
    threads.append(threadX)

    # threadY = motor_control.MotorRun(2, "Y", 30000, "forward", 5000)
    # threadY.start()
    # threads.append(threadY)
    #
    # threadZ = motor_control.MotorRun(3, "Z", 10000, "forward", 5000)
    # threadZ.start()
    # threads.append(threadZ)

    for t in threads:
        t.join()
    print ("Exiting Main Thread")
    return position