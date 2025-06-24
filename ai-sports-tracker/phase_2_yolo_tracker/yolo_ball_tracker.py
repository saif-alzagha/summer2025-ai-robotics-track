from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # Load a pre-trained YOLOv8 model

cap = cv2.VideoCapture("C:/Users/saifz/summer2025-ai-robotics-track/ai-sports-tracker/sample_input1.mp4")

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()
else:
    print("Video file opened successfully.")

cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video", 800, 400)

# Save the output video as YoloOutput.mp4 with fps of 20.0 and resolution of 800x400
out = cv2.VideoWriter('ai-sports-tracker/phase_2_yolo_tracker/YoloOutput.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (800, 400))    

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 400))  # Resize the frame to fit the window

    results = model(frame)[0] # Perform inference on the frame

    for r in results.boxes:
        cls = int(r.cls[0])  # Get the class ID of the detected object
        conf= float(r.conf[0])  # Get the confidence score for 0 to 1

        if model.names[cls] == "sports ball" and conf > 0.3:
            x1, y1, x2, y2 = map(int, r.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, "Soccer Ball", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    out.write(frame)  # Write the processed frame to the output video
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release
cv2.destroyAllWindows()
