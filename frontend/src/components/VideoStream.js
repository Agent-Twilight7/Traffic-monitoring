import React, { useState, useEffect } from "react";
import "../styles.css";  // Import the CSS file

const VideoStream = () => {
    const [videoUrl, setVideoUrl] = useState("");

    const handleUpload = async (event) => {
        const file = event.target.files[0];
        if (!file) return;

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await fetch("http://localhost:5000/upload", {
                method: "POST",
                body: formData,
            });

            const data = await response.json();
            if (response.ok) {
                const videoPath = encodeURIComponent(data.video_path);
                setVideoUrl(`http://localhost:5000/video_feed?source=${videoPath}`);
            }
        } catch (error) {
            console.error("Upload failed:", error);
        }
    };

    const handleSourceChange = () => {
        setVideoUrl(`http://localhost:5000/video_feed?source=webcam`);
    };

    return (
        <div className="container">
            <h2>Real-Time Object Detection</h2>

            {/* Buttons for Live Webcam & Upload */}
            <div className="button-container">
                <button onClick={handleSourceChange}>Live Webcam</button>
                <input type="file" accept="video/*" onChange={handleUpload} />
            </div>

            {/* Video Stream */}
            {videoUrl && (
                <div className="video-container">
                    <h3>Streaming:</h3>
                    <img
                        src={`${videoUrl}&t=${new Date().getTime()}`} // Prevent caching
                        alt="Video Stream"
                        className="video-frame"
                    />
                </div>
            )}
        </div>
    );
};

export default VideoStream;
