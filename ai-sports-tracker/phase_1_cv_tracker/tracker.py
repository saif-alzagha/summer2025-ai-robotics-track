import os
import cv2
import numpy as np

print("running tracker.py")
print(os.getcwd())


cap = cv2.VideoCapture("C:/Users/saifz/summer2025-ai-robotics-track/ai-sports-tracker/sample_input2.mp4")

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()
else:
    print("Video file opened successfully.")

#resize the window popup
cv2.namedWindow("Video",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video", 800, 400)


#save as output.mp4 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('ai-sports-tracker/phase_1_cv_tracker/CVoutput.mp4', fourcc, 20.0, (800, 400))


#initialize frame count
frame_count = 0 

while True:
    ret, frame = cap.read()
    if not ret:
        break


    # Increment frame count
    frame_count += 1  

    # Resize the frame to fit the window
    frame = cv2.resize(frame, (800, 400))

    #mask = np.zeros_like(frame[:, :, 0])  # Initialize mask with zeros

    #if frame_count > 5: 
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
    if contours:
        # Find the largest contour
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        #calculate shape metrics
        #bounding rectangle
        x, y, w, h = cv2.boundingRect(largest_contour)
        aspect_ratio = float(w) / h if h!= 0 else 0

        #minimum enclosing circle properties
        (circ_x, circ_y), radius = cv2.minEnclosingCircle(largest_contour)
        circle_area = np.pi * (radius ** 2)
        circularity = area / circle_area if circle_area != 0 else 0

        #filtering based on area
        min_area = 800
        max_area = 3000
        # min ratio for a circle
        min_aspect_ratio = 0.8
        # max ratio for a circle
        max_aspect_ratio = 1.2

        # min circularity for a circle
        # A perfect circle has a circularity of 1, but we allow some tolerance
        min_circularity = 0.7

        if (area > min_area and area < max_area) and \
            (min_aspect_ratio <= aspect_ratio <= max_aspect_ratio) and \
            (circularity > min_circularity):


            # Draw the bounding circle
            center = (int(circ_x), int(circ_y))
            radius = int(radius)

            # Draw the circle on the frame
            cv2.circle(frame, center, radius, (0, 255, 0), 2)
            cv2.putText(frame, "Basketball", (center[0] -30, center[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,0.5, (0,255,0), 2)
            
    #save the frames to output.mp4
    out.write(frame)

    # Display the frame  
    cv2.imshow("Video", frame)

    #show mask
    cv2.imshow("Mask", mask)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()