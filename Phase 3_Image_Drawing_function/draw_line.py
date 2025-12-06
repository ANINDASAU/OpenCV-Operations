import cv2

image = cv2.imread(r"Phase 3_Image_Drawing_function\Test_Image.jpg")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")

    pt1 = (50,100)
    pt2 = (400,200)

    color = (255,0,0)
    thickness = 4

    cv2.line(image,pt1,pt2,color, thickness)

    cv2.imshow("Line Drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()