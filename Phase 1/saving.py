import cv2

image = cv2.imread("Phase 1\Test_Image.jpg")

if image is not None:
    success = cv2.imwrite("Phase 1\Output_Image.jpg", image)
    if success:
        print("Image saved successfully as 'Output_Image.jpg'")
    else:
        print("Failed to save the image")
else:
    print("Error: Could not load the image")