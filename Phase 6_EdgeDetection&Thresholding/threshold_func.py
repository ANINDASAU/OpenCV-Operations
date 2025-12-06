import cv2

image = cv2.imread(r"Phase 6_EdgeDetection&Thresholding\canny_test.jpg")

ret, thresh_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", image)
cv2.imshow("Threshold image", thresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows()