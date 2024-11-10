# Enter your code here
import cv2
import numpy as np

# Remove bounding boxes with low confidence using non-maximum suppression
def postprocess(frame, outs, trackers, tracked):
    classIds = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]

            if confidence > confThreshold and classId == classes.index("sports ball"):
                centerX = int(detection[0] * frame.shape[1])
                centerY = int(detection[1] * frame.shape[0])
                width = int(detection[2] * frame.shape[1])
                height = int(detection[3] * frame.shape[0])

                left = int(centerX - width / 2)
                top = int(centerY - height / 2)

                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

                if classId not in trackers:
                    trackers[classId] = cv2.TrackerKCF_create()
                    trackers[classId].init(frame, (left, top, width, height))
                    tracked[classId] = True
                else:
                    success, box = trackers[classId].update(frame)
                    if success:
                        tracked[classId] = True
                        cv2.putText(frame, "Ball Detected By KCF Tracking", (0, 45), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0))
                    else:
                        tracked[classId] = False
                        cv2.putText(frame, "Ball Detected By YOLOV3 Detection!", (0, 45), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0))

    if not boxes:
        cv2.putText(frame, "Failed to Detect the Ball!", (0, 45), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255))

    indices = cv2.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    if len(indices) > 0:
        for i in indices.flatten():
            box = boxes[i]
            drawPred(classIds[i], confidences[i], box[0], box[1], box[0] + box[2], box[1] + box[3], frame, tracked[classIds[i]])


# Draw the predicted bounding box for detection
def drawPred(classId, conf, left, top, right, bottom, frame, tracked):
    # Draw a rectangle around the detected object
    color = (0, 255, 0) if tracked else (255, 0, 0)
    cv2.rectangle(frame, (left, top), (right, bottom), color, 3)

    # Get the label for the class name and its confidence
    label = '%.2f' % conf
    if classes:
        assert(classId < len(classes))
        label = '%s:%s' % (classes[classId], label)

    # Display the label at the top of the bounding box
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.5
    fontColor = (0, 0, 0)
    lineType = 1

# initialize the parameters for object detection
objectnessThreshold = 0.5    # Objectness threshold
confThreshold = 0.5          # Confidence threshold
nmsThreshold = 0.2           # Non-maximum suppression threshold
inpWidth = 416               # Width of network's input image
inpHeight = 416              # Height of network's input image

# Load names classes
classes = []
with open('coco.names', 'r') as f:
    lines = f.readlines()
    for line in lines:
        classes.append(line.strip())

# Load the DNN
net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

# load video
cap = cv2.VideoCapture('soccer-ball.mp4')
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS) 

trackers = {}
tracked = {}

# initiate videowriter
codec = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
filename = "output.avi"
writer = cv2.VideoWriter(filename, codec, fps, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (inpWidth, inpHeight), (0, 0, 0), True, False)

    #Sets the input to the network
    net.setInput(blob)

    # Runs the forward pass to get output of the output layers
    outs = net.forward(net.getUnconnectedOutLayersNames())

    # Remove bounding boxes with low confidence using non-maximum suppression
    postprocess(frame, outs, trackers, tracked)

    # put effeciency information the function getPerProfile returns the overall time for inference(t)
    # and the timings for each of the layers (in layersTimes)
    t, _ = net.getPerfProfile()
    label = "Inference time for a frame : %.2f ms" % (t * 1000.0 / cv2.getTickFrequency())
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0,2))
    cv2.putText(frame, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

    cv2.imshow("Object Detection and Tracking", frame)
    writer.write(frame)

    # Check for ESC key press to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
writer.release()