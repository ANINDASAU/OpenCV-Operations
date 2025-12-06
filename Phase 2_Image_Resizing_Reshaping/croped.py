import cv2

image = cv2.imread(r"Phase 2_Image_Resizing_Reshaping\Test_Image.jpg")

if image is not None:
    cropped = image[100:200, 50:150]

    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    