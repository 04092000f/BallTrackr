# **Soccer Ball Detection and Tracking**

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
- Python 3.8+
- Required Python packages (install via `requirements.txt`):  
  ```bash
  pip install opencv-contrib-python
`python detect-track.py`

---

## Final Output
![c1_project2_detection_and_tracking](./output.gif)


---
