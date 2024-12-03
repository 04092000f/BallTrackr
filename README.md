# **BallTrackr**

**BallTrackr** is a video analysis tool designed to detect and track a soccer ball in videos. Combining the powerful object detection capabilities of **YOLOv3** with the real-time performance of the **KCF (Kernelized Correlation Filters)** tracker, this application ensures accurate and efficient soccer ball tracking.

## **Features**

1. **Soccer Ball Detection**  
   - Uses the YOLOv3 object detection model to identify the soccer ball in video frames reliably.

2. **Object Tracking**  
   - Tracks the soccer ball across frames with the KCF tracker for real-time efficiency.

3. **Recovery Mechanism**  
   - Handles scenarios where the tracker loses the ball by automatically switching back to YOLOv3 detection. The tracker resumes once the ball is detected again.


## **Requirements**

Before starting up, ensure the following dependencies and files are set up:

### **Dependencies**
- Python 3.x Installed
- Required Python packages **OpenCV**(using `pip install` command):  
  ```bash
  pip install opencv-contrib-python

### Files to Download
- Download **YOLOV3** Weights file from [here](https://drive.google.com/file/d/1CT_uOn_Ja35WHYjrXHiEf99p7ygcMX3G/view?usp=sharing)

- Download **Input** Video file from [here](https://drive.google.com/file/d/1Y8JWb09jndGwXC1X-d6PQXBm8XXsS1KI/view?usp=sharing)

### How to Run
1. Clone the repository or download the project files.
2. Ensure all required libraries are installed and the necessary files (YOLOv3 weights and input video) are downloaded.
3. Run the application with the following command:
```bash
python detect-track.py
````

## Final Output
- The application processes the video and highlights the soccer ball as it moves through the frames. Here's an example of the output:
<br>![c1_project2_detection_and_tracking](./output.gif)
