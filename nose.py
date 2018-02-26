# Here we import openCV2. We can change the name of this import by typing "as" and give it another name. We are not doing this.
import cv2
import os
from pymouse import PyMouse as mouse
# TODO: Delete this example and implement mouse
# TODO: Implement eyes casacde
m = mouse()
m.move(2,42)

m = PyMouse()
# PLEASE NOTE This program requires pywin32 to run in Windows
# Sadly since pywin32 contains allot of C++ it cannot be installed through pip
# Download PyWin excecutable from https://github.com/mhammond/pywin32/releases
# Works in Linux through pip packages included in requirements.txt

# Here we download the nose cascade file. This is the xml file that contains the code for recognizing  noses.
#The file is optained from https://github.com/opencv/opencv_contrib/blob/master/modules/face/data/cascades/haarcascade_mcs_nose.xml
#Here we create a relative path so that the software can be used on different computers without getting path errors.
dir = os.path.dirname(__file__)
nosefile = os.path.join(dir, 'haarcascade_mcs_nose.xml')
facefile = os.path.join(dir, 'haarcascade_frontalface_default.xml')
eyefile = os.path.join(dir, 'eyes.xml')
nose_cascade = cv2.CascadeClassifier(nosefile)
face_cascade = cv2.CascadeClassifier(facefile)
eye_cascade = cv2.CascadeClassifier(eyefile)

#At this time it we want to have a checker that throws an error if there is any issues with the xml file handling.
if nose_cascade.empty():
    raise IOError('Unable to load the nose cascade xml file')

if face_cascade.empty():
    raise IOError('Unable to load the face cascade xml file')

if eye_cascade.empty():
    raise IOError('Unable to load the eye cascade xml file')


# Here we create a variable cap that contains the information about which camera the program is to use.
#  In this case we have set it to 0 (expecting the user to use a intergrated camera if they have one.from
# IF the user is using an external camera instead of an his/hers intergrated one, we would have to change the input to 1.
cap = cv2.VideoCapture(0)
# display_factor is set to 1 to keep the original size of the captured image.. (Might be an issue if screen is lower ress than webcam).
# this facot will be used further down in the frame variable that contains cv2.resize.
ds_factor = 1

#  Here we start a loop that will countinue uintill the Esc-button is pushed (27).
while True:
    # Capture the frames right now
    ret, frame = cap.read()
    # Re-size based on the factor from before.
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    # Since the face-detector only works on balck and white images we do a convertion to BGR2GRAY here.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)
    # Here we draw the square around the nose that is detected.
    x_dim, y_dim = m.screen_size()
    face_rect = face_cascade.detectMultiScale(gray, 1.3, 5)
    eye_rect = eye_cascade.detectMultiScale(gray, 1.3, 5)
    # Here we draw the square around the nose, face and eyes that is detected.
    for (x,y,w,h) in nose_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 3)
        break
    for (x,y,w,h) in face_rect:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        m.move(x, y)
        break
    for (x,y,w,h) in eye_rect:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (205,0,0), 3)
        break

    cv2.imshow('Nesehorn deteksjonsprogram', frame)
# venter 1 millisekund før den fanger den neste framen
    c = cv2.waitKey(1)
# Close the program if the escape key is cli ked. The number 27 directs to the escape key.
    if c == 27:
        break
# Here we release the webcam to be used by other programs before we shut down the program.
cap.release()
# Terminating the window the software is running in. 
cv2.destroyAllWindows()
