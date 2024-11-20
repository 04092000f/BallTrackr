# **BallTrackr**

This project implements a **Video Analysis** application capable of detecting and tracking a soccer ball in a video. The application combines object detection using **YOLOv3** and object tracking using the **KCF** tracker to achieve accurate and efficient tracking.

---

## **Features**

1. **Soccer Ball Detection**  
   The application utilizes **YOLOv3** for robust object detection, specifically targeting the soccer ball.

2. **Object Tracking**  
   Once detected, the soccer ball is tracked using the **KCF (Kernelized Correlation Filters)** tracker for efficient real-time performance.

3. **Recovery Mechanism**  
   - If the tracker loses the soccer ball, the application continues detection for the next `n` frames (default: `n=10`).  
   - Upon successful detection, tracking resumes seamlessly.

---

## **Pre-requisites**

To get started, ensure the following dependencies and files are set up:

### **Dependencies**
- Python 3.x Installed
- Required Python packages **OpenCV**(using `pip install` command):  
  ```bash
  pip install opencv-contrib-python

- Download **YOLOV3** Weights file from [here](https://drive.google.com/file/d/1CT_uOn_Ja35WHYjrXHiEf99p7ygcMX3G/view?usp=sharing)

- Download **Input** Video file from [here]([url](https://drive.google.com/file/d/1Y8JWb09jndGwXC1X-d6PQXBm8XXsS1KI/view?usp=sharing))

 Once all the required sofwares, files and libraries are downloaded installed, finally run the application using: 
   `python detect-track.py`

---

## Final Output
![c1_project2_detection_and_tracking](./output.gif)


---
