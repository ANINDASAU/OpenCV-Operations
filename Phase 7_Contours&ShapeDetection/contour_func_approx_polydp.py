import cv2

# Load image (4-channel) and convert to BGR
image = cv2.imread(r"Phase 7_Contours&ShapeDetection\pentagon_test.png", cv2.IMREAD_UNCHANGED)
image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary inverse threshold to make shapes white, background black
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# Optional: remove small noise
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

# Find external contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # Ignore very small contours (noise)
    if cv2.contourArea(cnt) < 100:
        continue

    # Approximate contour to polygon
    approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
    corners = len(approx)

    # Determine shape
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        # Check rectangle vs square
        x, y, w, h = cv2.boundingRect(approx)
        if abs(w - h) <= 5:
            shape_name = "Square"
        else:
            shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    else:
        shape_name = "Circle"

    # Draw contours and put text
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
    x, y = approx.ravel()[0], approx.ravel()[1] - 10
    cv2.putText(image, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
