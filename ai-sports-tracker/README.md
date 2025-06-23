This is a computer vision-based system that processes sports video footage and automatically tracks moving objects — such as balls or players — using classical CV techniques.

Unlike generic object detection demos, this project is focused on:
- Frame-level precision
- Tracking persistence
- Real-world application in sports analysis

Later versions will include deep learning (YOLOv8), speed estimation, and dashboard analytics.

My current plan includes 4 phases to grow my skills: 
✅ Phase 1: Basic Visual Tracker (No ML)
Input: short .mp4 clip

Technique: HSV color filtering or contour-based motion detection

Output: object is tracked and marked on video

Tools: OpenCV, NumPy

🔜 Phase 2: Intelligent Tracking + Analysis
Use DeepSort or YOLOv8 for smart object detection

Add multiple-object tracking (MOT)

Add frame-wise data logging (CSV or JSON)

🧠 Phase 3: Sports-Specific Intelligence
Identify player vs. ball

Measure distance traveled, speed

Create action tags (e.g. "pass", "shoot", "intercept")

📈 Phase 4: Dashboard/Analytics Layer
Build a lightweight Streamlit or Dash app

Visualize paths, heatmaps, player interactions
