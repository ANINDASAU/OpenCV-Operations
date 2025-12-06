import cv2

image = cv2.imread("Phase 1\Test_Image.jpg")

if image is None:
    print("Error: Image not found")
else:
    print("Image loaded successfully")