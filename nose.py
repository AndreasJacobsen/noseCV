# Importerer cv2, vi kan sette den som "as cv" om vi ikke gidder å skrive cv2 i fremtiden
import cv2

# Laster nose cascade filen, filen henten fra https://github.com/opencv/opencv_contrib/blob/master/modules/face/data/cascades/haarcascade_mcs_nose.xml
# NB Bug i file path, du må sette din egen file path
nose_cascade = cv2.CascadeClassifier('/home/andreas/PycharmProjects/learnOpen/haarcascade_mcs_nose.xml')

if nose_cascade.empty():
  raise IOError('Unable to load the nose cascade classifier xml file')

# Starter video capture, 0-en viser hvilket kamera programmet skal bruke.
# Bruker vi ett USB kamera kan IDen være noe annet
cap = cv2.VideoCapture(0)
# Faktor definerer størrelsen i faktorer, hva nå enn en faktor er
ds_factor = 1

# Starter en evig løkke som fortsettere å fange frames helt til vi kaller Esc-knappen (27)
while True:
    # Fang nåværende frames
    ret, frame = cap.read()
    # Re-size bassert på ds_factor variabelen over
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    # face detectoren kjører bare med sort hvit bilder, så vi konverterer til grayscale her
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)
    # tegner en firkant rundt nesa 
    for (x,y,w,h) in nose_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        break

    cv2.imshow('Nose Detector', frame)
# venter 1 millisekund før den fanger den neste framen
    c = cv2.waitKey(1)
# Lukker programmet om vi klikker på esc knappen, wait i 1 millisekund (sjekk dette) før vi kan lukke programmet

    if c == 27:
        break
# Slipp kamera fri s så du kan bruke det til andre ting
cap.release()
# SKru av programmet
cv2.destroyAllWindows()
