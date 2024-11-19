# Detection and Tracking

In this project, we have created a **Video Analysis** application that performs object detection as well as object tracking. 

Specifically, the application performs 2 tasks:

1. Detecting the soccer ball using **YOLOv3**.
2. Perform tracking using **KCF** tracker.

If the application looses tracking, we continue looking for the next `n` frames (in our case, `n`is set to `10`) until the detector is able to detect the soccer ball again. Subsequently, the tracker then takes over for tracking it further.

**Pre-requisites**

- Download the **yolov3** weights file from [here](https://drive.google.com/file/d/1CT_uOn_Ja35WHYjrXHiEf99p7ygcMX3G/view?usp=sharing)
- Download the input video file from [here](https://drive.google.com/file/d/1Y8JWb09jndGwXC1X-d6PQXBm8XXsS1KI/view?usp=sharing)

Once these files are downloaded, one can start the application by running:

`python detect-track.py`


A sample video output is shown below.


![c1_project2_detection_and_tracking](./output.gif)


---
