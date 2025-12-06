import cv2

image = cv2.imread(r"Phase 3_Image_Drawing_function\Test_Image.jpg")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")
    cv2.circle(image, (150,150), 50, (255,0,0), 5)

    cv2.imshow("Drawing Circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()