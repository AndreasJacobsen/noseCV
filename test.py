import cv2
import numpy as np

img = cv2.imread('img/kristian.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
while True:
    k = cv2.waitKey(0) & 0xFF     # Why 0xFF? We only want the lowest byte. This is mainly for cross-platform safety.j
    if k == ord('s'):
        cv2.imwrite('test.png',img)
    if k == 27: break             # Code for the ESC key
cv2.destroyAllWindows()