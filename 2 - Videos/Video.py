import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)     
# Instead of the Camera sindex we can specify the audio file like 'test.avi, nad theta gets played frame by frame.

##############fourcc = cv2.VideoWriter_fourcc(*'XVID') 
# Here XVID is most suitable, MJPG gic=ves high size videos. X264 give low size videos.

#############out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
# Here the 20 is the snumber sof frames per second. The tuple is the Frame size we want tod record.

while(True):
    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    # Used to convert the frame in ther video to gray scale

    cv2.imshow('Video',frame)
    #Display the frame
    cv2.imshow('Gray',gray)
    ###################out.write(frame)
    key = cv2.waitKey(1)
    # Waits for 1ms to read the dinput of a key, and stores the UNICODE value in the variable key

    if key ==  ord('q'):
        break               # Breaks from the Loop if the enterd keyd is q

cap.release()
##########out.release()
cv2.destroyAllWindows()