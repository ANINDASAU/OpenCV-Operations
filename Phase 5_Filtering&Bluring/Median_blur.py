import cv2
image = cv2.imread(r"Phase 5_Filtering&Bluring\image_for_test.jpg")

blurred = cv2.medianBlur(image, 11)

frame_width =500
frame_height = 500
image_resize = cv2.resize(image, (frame_width, frame_height))
blurred_resized =  cv2.resize(blurred, (frame_width, frame_height))


combined = cv2.hconcat([image_resize, blurred_resized])


cv2.imshow("Output image", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()