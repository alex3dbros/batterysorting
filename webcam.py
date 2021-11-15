import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)

width = 640
height = 478

center_coordinates = (int(width / 2), int(height / 2))
crosshair_radius = 45
color = (255, 0, 0)
crosshair_thickness = 2

cap.set(3, width)
cap.set(4, height)


def sample_crosshair(hsv_image):
    low_range = np.array([0, 0, 36])
    high_range = np.array([90, 126, 217])

    empty_hole_mask = cv2.inRange(hsv_image, low_range, high_range)

    x = int(width / 2)
    y = int(height / 2)

    crop_img = empty_hole_mask[y - 50:y + 50, x - 50:x + 50]

    white_pixels = np.round(cv2.countNonZero(crop_img), 2)
    # print('brown pixel percentage:', white_pixels)

    if white_pixels < 5000:
        print("Cell is present")
    else:
        print("Empty cell hole")

    cv2.imshow("mask", crop_img)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sample_crosshair(hsv_frame)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.line(frame, (200, int(height / 2)), (width - 200, int(height / 2)), color,crosshair_thickness)
    cv2.line(frame, (int(width / 2), 100), (int(width / 2), height - 100), color, crosshair_thickness)
    cv2.circle(frame, center_coordinates, crosshair_radius, color, crosshair_thickness)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()