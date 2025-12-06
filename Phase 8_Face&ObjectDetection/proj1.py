import cv2

# Load Haar Cascade (use human face cascade, not cat face)
face_cascade = cv2.CascadeClassifier("Phase 8_Face&ObjectDetection\haarcascade_frontalface_default.xml")

# Webcam
cap = cv2.VideoCapture(0)

# Store previous face location to reduce shaking
prev_x, prev_y, prev_w, prev_h = 0, 0, 0, 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # More stable parameters
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=7,     # higher = more stable
        minSize=(80, 80),   # ignore very small false detections
    )

    for (x, y, w, h) in faces:
        # Smooth out the box movement (anti-shake)
        x = int((x + prev_x) / 2)
        y = int((y + prev_y) / 2)
        w = int((w + prev_w) / 2)
        h = int((h + prev_h) / 2)

        prev_x, prev_y, prev_w, prev_h = x, y, w, h

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show frame
    cv2.imshow("Haar Cascade Face Detection (Stable)", frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
