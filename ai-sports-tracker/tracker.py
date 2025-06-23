
import cv2

print("running tracker.py")

cap = cv2.VideoCapture("C:/Users/saifz/summer2025-ai-robotics-track/ai-sports-tracker/sample_input.mp4")

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()
else:
    print("Video file opened successfully.")

#resize the window popup
cv2.namedWindow("Video",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video", 800, 400)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the frame
    frame_resized = cv2.resize(frame, (800, 400))
    cv2.imshow("Video", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()