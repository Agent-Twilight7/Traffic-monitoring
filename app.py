from flask import Flask, Response, request
from flask_cors import CORS
import cv2
import torch
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication
from ultralytics import YOLO

# Load the trained YOLOv8 model
model_path = "models/best.pt"  # Path to your saved model
model = YOLO(model_path)  # Load the trained model

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def generate_frames(video_source):
    cap = cv2.VideoCapture(video_source)  # Webcam (0) or uploaded video path

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        # Run YOLOv8 inference
        results = model(frame)  

        # Draw bounding boxes and labels
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
                conf = float(box.conf[0])  # Confidence score
                cls = int(box.cls[0])  # Class index

                label = f"{model.names[cls]} {conf:.2f}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Encode frame as JPEG
        _, buffer = cv2.imencode(".jpg", frame)
        frame_bytes = buffer.tobytes()
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n")

    cap.release()


@app.route("/video_feed")
def video_feed():
    source = request.args.get("source", "webcam")  # Default: webcam
    video_path = 0 if source == "webcam" else os.path.join(UPLOAD_FOLDER, source)
    return Response(generate_frames(video_path), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/upload", methods=["POST"])
def upload_video():
    if "file" not in request.files:
        return {"error": "No file uploaded"}, 400

    file = request.files["file"]
    filename = file.filename
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    return {"video_path": filename}, 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
