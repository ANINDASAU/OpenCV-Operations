import cv2

image =  cv2.imread("Phase 5_Filtering&Bluring\image_for_test.jpg")

blurred_img = cv2.GaussianBlur(image, (7,7), 3)

frame_width =500
frame_height = 500

image_resize = cv2.resize(image, (frame_width, frame_height))
blurred_resized =  cv2.resize(blurred_img, (frame_width, frame_height))


combined = cv2.hconcat([image_resize, blurred_resized])


cv2.imshow("Output image", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()