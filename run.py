import threading
import time
import RPi.GPIO as GPIO

import functions as fn


# maxX = 1200 mm
# maxY = 1200 mm
# maxZ = 16200 steps

print("Starting motor")
fn.find_zero()
current_x_pos = 0
current_y_pos = 0
current_z_pos = 0
current_a_pos = 0
# current_a_pos = fn.move("A", 1600, current_a_pos)
# current_x_pos = fn.move("X", 600, current_x_pos)
#current_y_pos = fn.move("Y", 600, current_y_pos)
#current_z_pos = fn.move("Z", -8, current_z_pos)






print(current_x_pos)



