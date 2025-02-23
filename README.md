
# 📌 Project Description

This project is a **real-time object detection system** that leverages **YOLOv8 (You Only Look Once)** for fast and accurate object detection.  
The system is built using **Flask** for the backend and **React.js** for the frontend, allowing users to:  

🔹 **Stream live video from a webcam** for real-time object detection.  
🔹 **Upload a video file**, which is processed frame-by-frame to detect objects.  
🔹 **View detected objects** with bounding boxes and labels drawn on the video feed.  

The backend uses **OpenCV** to process video frames and **Ultralytics YOLOv8** for inference, while the frontend provides an **intuitive interface** for users to interact with the system.

---

## 📌 Features
✅ Real-time object detection using YOLOv8  
✅ Option to use **webcam** or **upload a video**  
✅ Flask API for video streaming and processing  
✅ React-based **UI for easy interaction**  

---

## 🛠️ Installation & Setup

###  Clone the Repository
```sh
git clone https://github.com/your-username/your-repo-name.git
```
cd your-repo-name
### Install Dependencies
Backend (Flask)
Ensure you have Python installed, then run:

```sh
pip install -r requirements.txt
```
Frontend (React)
Navigate to the frontend folder and install dependencies:

```sh
cd frontend
npm install
```
### Running the Application
Start the Flask Backend
Run the backend server:

```sh
python app.py
```
The backend will start at http://localhost:5000/.

Start the React Frontend
Navigate to the frontend folder and start React:

```sh
cd frontend
npm start
```
The frontend will be available at http://localhost:3000/.

### 📂 Repository Structure
```sh
📦 project-root/
│── 📂 backend/            # Flask backend (YOLO inference, API)
│   ├── app.py             # Main Flask server
│   ├── models/            # YOLO model files
│   ├── uploads/           # Uploaded video storage
│   ├── requirements.txt   # Python dependencies
│
│── 📂 frontend/           # React frontend
│   ├── src/
│   │   ├── components/    # React UI components
│   │   │   ├── VideoStream.js
│   │   ├── styles.css     # Styling for UI
│   ├── package.json       # React dependencies
│
│── README.md  
```
### Summary
The Flask backend runs YOLOv8 for object detection.
The React frontend provides a UI to choose between a live webcam or an uploaded video for detection.
The detected objects are displayed with bounding boxes and labels.

###  Features
✔️ Real-time object detection
✔️ Upload video for analysis
✔️ Flask-React integration
✔️ Simple UI with minimal setup
