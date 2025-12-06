import cv2

image = cv2.imread(r"Phase 3_Image_Drawing_function\Test_Image.jpg")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")
    cv2.putText(image, "Hello Python Programer", (50,300),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,0,255),2)

    cv2.imshow("Adding text over image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()