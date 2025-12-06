import cv2

image = cv2.imread(r"Phase 3_Image_Drawing_function\Test_Image.jpg")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")
    pt1 = (150,150)
    pt2 = (450,650)
    color = (0,0,255)
    thickness = 3

    cv2.rectangle(image,pt1,pt2,color,thickness)

    cv2.imshow("Image focusing rectangle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()