import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture("C:/Users/saifz/summer2025-ai-robotics-track/ai-sports-tracker/sample_input1.mp4")
model = YOLO("yolov8n.pt")  # Load a pre-trained YOLOv8 model

cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video", 800, 400)  # Resize the window to fit the video

out= cv2.VideoWriter('ai-sports-tracker/phase_2_yolo_tracker/YoloOutputWithTracker.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (800, 400))  # Save the output video as YoloOutput.mp4 with fps of 20.0 and resolution of 800x400


tracker= None
tracking= False
track_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 400))  # Resize the frame to fit the window

    if not tracking or track_counter > 30:
        #detect the ball using YOLO
        results = model(frame)[0]

        for r in results.boxes:
            cls = int(r.cls[0])
            conf = float(r.conf[0])

            if model.names[cls] == "sports ball" and conf > 0.3:
                x1, y1, x2, y2 = map(int, r.xyxy[0])
                w= x2 - x1
                h = y2 - y1

                bbox = (x1, y1, w, h)

                tracker = cv2.TrackerCSRT_create()  # Create a new tracker
                tracker.init(frame, bbox)  # Initialize the tracker with the bounding box
                tracking = True
                track_counter = 0
                break  # Break the loop to avoid multiple initializations


    elif tracking:
        success, bbox = tracker.update(frame)  # Update the tracker with the current frame
        if success:
            x, y, w, h = map(int, bbox)
            # Draw the bounding box and label on the frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Tracking Ball", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            track_counter += 1
        else:
            tracking = False # If tracking fails, reset the tracking state and go to YOLO detection
    
    out.write(frame)  # Write the processed frame to the output video
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
# Release the video capture and writer objects
# cv2.destroyAllWindows()  # Close all OpenCV windows