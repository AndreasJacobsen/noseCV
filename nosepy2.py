# Here we import openCV2. We can change the name of this import by typing "as" and give it another name. We are not doing this.
import cv2
# Here we import time to use sleep function for waiting during the loop
import time
# Here we import information about the operating system to ensure that the correct path for the xml files are used.
import os
#Here we import pymouse, a framework which makes mainpulation of the mouse cursor possible.
from pymouse import PyMouse

####################! PLEASE NOTE !############################
# PLEASE NOTE This program requires pywin32 to run in Windows
# Sadly since pywin32 contains allot of C++ it cannot be installed through pip
# Download PyWin executable from https://github.com/mhammond/pywin32/releases
# For MacOS/OS X install Quartz and AppKit
# Works in Linux through pip packages included in requirements.txt
#PLEASE NOTE This program is only designed to work with one nose at a time
##########################################################

# Here we download the nose cascade, face cascade and eye cascade file. This is the xml files that contains the code for recognizing  specific parts of the body.
# The file is optained from https://github.com/opencv/opencv_contrib/blob/master/modules/face/data/cascades/haarcascade_mcs_nose.xml
# Here we create a relative path so that the software can be used on different computers without getting path errors.
dir = os.path.dirname(__file__)
nosefile = os.path.join(dir, 'haarcascade_mcs_nose.xml')
facefile = os.path.join(dir, 'haarcascade_frontalface_default.xml')
eyefile = os.path.join(dir, 'eyes.xml')
smilefile = os.path.join(dir, 'smile.xml')
palmfile = os.path.join(dir, 'palm.xml')
nose_cascade = cv2.CascadeClassifier(nosefile)
face_cascade = cv2.CascadeClassifier(facefile)
eye_cascade = cv2.CascadeClassifier(eyefile)



# Error handling for empty files, due to us not wanting to force user to install GTK or QT these errors are displayed in the terminal instead
if nose_cascade.empty():
    raise IOError('Unable to load the nose cascade xml file')
    cv2.destroyAllWindows()

if face_cascade.empty():
    raise IOError('Unable to load the face cascade xml file')
    cv2.destroyAllWindows()

if eye_cascade.empty():
    raise IOError('Unable to load the eye cascade xml file')
    cv2.destroyAllWindows()

# Starting PyMouse for later use inside our loops
m = PyMouse()

# if smile_cascade.empty():
#     raise IOError('Unable to load the smile cascade xml file')
#     cv2.destroyAllWindows()
#denne var buggy
#if palm_cascade.empty():
  #  raise IOError('Unable to load the palm cascade cml file')
   # cv2.destroyAllWindows()

# Here we create a variable cap that contains the information about which camera the program is to use.
#  In this case we have set it to 0 (expecting the user to use a intergrated camera if they have one)
# IF the user is using an external camera instead of an his/hers intergrated one, we would have to change the input to 1.
cap = cv2.VideoCapture(0)
# Display_factor is set to 1 to keep the original size of the captured image.. (Might be an issue if screen is lower ress than webcam).
# This factor will be used further down in the frame variable that contains cv2.resize.
ds_factor = 1
c = cv2.waitKey(33) & 0xFF
#  Here we start a loop that will countinue uintill the Esc-button is pushed (27).
while True:
    # Capture the frames right now
    ret, frame = cap.read()
    # Flipping the image so that moving nose to the left equivilates to moving cursor left.
    frame = cv2.flip(frame, 1)
    # Re-size based on the factor from before.
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    # Since the face-detector only works on black and white images we convert the image to BGR2GRAY here.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Here we draw the square around the nose that is detected.
    x_dim, y_dim = m.screen_size()
    nose_rect = nose_cascade.detectMultiScale(gray, 1.3, 5)
    face_rect = face_cascade.detectMultiScale(gray, 1.3, 5)
    #eye_rect = eye_cascade.detectMultiScale(gray, 1.3, 5)
    #smile_rect = smile_cascade.detectMultiScale(gray,1.3, 5)
    #hpalm_rect = palm_cascade.detectMultiScale(gray,1.3,1)
    # Here we draw the square around the nose, face and eyes that is detected.
    # First we check if nose_rect contains any data
    # if not we use the face for mouse navigation instead

    if cv2.waitKey(1) & 0xFF == ord('q'):  # exit on pressing 'q'
            cap.release()
            cv2.destroyAllWindows()
            break
    for (x, y, w, h) in face_rect:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        regionface = gray[y:y+h, x:x+w]
        regioncolor = frame[y:y+h, x:x+w]
        nose = nose_cascade.detectMultiScale(regionface)
        for (nx, ny, nw, nh) in nose_rect:
                cv2.rectangle(regioncolor, (nx, ny), (nx+nw, ny+nh), (0, 255, 0), 2)
                # Here we say that m (the variable created before, should move the mouse using the x, and y variable from the nose rect.
                # We have set the variable times 3 as to make the cursor start aprox in the middel.
                m.move(x*8, y*8)
                if cv2.waitKey(1) == 32:
                    m.click(x*8, y*8, 2)
                    print("Click!")
                # if(len(palm_rect)>0):
                #      m.click(x,y,1)
                    break

    cv2.imshow('Nesehorn deteksjonsprogram', frame)
    time.sleep(0.005)  # Waiting 1 millisecond to show the next frame.
# Here we release the webcam to be used by other programs before we shut down the program.
cap.release()
# Terminating the window the software is running in.
cv2.destroyAllWindows()
