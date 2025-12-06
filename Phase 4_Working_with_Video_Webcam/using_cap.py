import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read frame")
        break

    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) == ord('q'):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()
