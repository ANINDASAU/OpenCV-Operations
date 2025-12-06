import cv2

image = cv2.imread(r"Phase 7_Contours&ShapeDetection\images_test.png", cv2.IMREAD_UNCHANGED)  # loads 4-channel
image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)          # convert to BGR
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 200, 250, cv2.THRESH_BINARY_INV)

#FIND CONTOURS
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image, contours, -1, (0,255,0), 3)

cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
