
import cv2

print("running tracker.py")

cap = cv2.VideoCapture("C:/Users/saifz/summer2025-ai-robotics-track/ai-sports-tracker/sample_input2.mp4")

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

    # Resize the frame to fit the window
    frame = cv2.resize(frame, (800, 400))
    # Display the frame  
    cv2.imshow("Video", frame)

    #converting BGR into HSV
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #define the color range in HSV for the basket ball
    lower = (125, 8, 14)  # Lower bound for basketball color
    upper = (170, 66, 38)  # Upper bound for basketballcolor

    # Create a mask for the color
    mask = cv2.inRange(hsv, lower, upper)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #loop through the contours and draw circles around the detected ball by filtering out small contours
    for contour in contours:
        if cv2.contourArea(contour) > 100:
            # Find the minimum enclosing circle for the contour
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            # Draw the circle on the frame
            cv2.circle(frame, center, radius, (0, 255, 0), 2)
            #show mask
            cv2.imshow("Mask", mask)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()