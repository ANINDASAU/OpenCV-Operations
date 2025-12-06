import cv2

image = cv2.imread("Phase 1\Test_Image.jpg")

if image is not None:
    h, w, c = image.shape
    print(f"Image Dimensions: \nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("Error: Image Could not loaded successfully")