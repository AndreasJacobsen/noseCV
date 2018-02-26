# Here we import openCV2. We can change the name of this import by typing "as" and give it another name. We are not doing this.
import cv2
import os

# Here we download the nose cascade file. This is the xml file that contains the code for recognizing  noses.
#The file is optained from https://github.com/opencv/opencv_contrib/blob/master/modules/face/data/cascades/haarcascade_mcs_nose.xml
#Here we create a relative path so that the software can be used on different computers without getting path errors.
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'haarcascade_mcs_nose.xml')
nose_cascade = cv2.CascadeClassifier(filename)

#At this time it we want to have a checker that throws an error if there is any issues with the xml file handling.
if nose_cascade.empty():
  raise IOError('Unable to load the nose cascade classifier xml file')

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
    for (x,y,w,h) in nose_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
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
