import cv2

# Use a raw string (r"...") to avoid path errors with backslashes
image = cv2.imread(r"Phase 2_Image_Resizing_Reshaping\Test_Image.jpg")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")

    # Resize the image to 300x300 pixels
    resized_image = cv2.resize(image, (300, 300))

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resized_image)

    # Save the resized image
    cv2.imwrite("Phase 2_Image_Resizing_Reshaping/resized_image.jpg", resized_image)
    print("Resized image saved as resized_image.jpg")

    # Wait for any key press to close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
