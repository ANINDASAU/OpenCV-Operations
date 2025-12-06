import cv2
import numpy as np

image1 = np.zeros((300,300), dtype ="uint8")
image2 = np.zeros((300,300), dtype ="uint8")

cv2.circle(image1, (150,150), 100, 255, -1)

cv2.rectangle(image2, (100,100), (250,250), 255, -1)

bitwise_and = cv2.bitwise_and(image1,image2)
bitwise_or = cv2.bitwise_or(image1,image2)
bitwise_not = cv2.bitwise_not(image1)

cv2.imshow("Circle", image1)
cv2.imshow("Resctangle", image2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()