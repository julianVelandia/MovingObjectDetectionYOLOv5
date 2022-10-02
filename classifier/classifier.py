import torch
import cv2
import numpy as np


def moving_object_detection():
    model = torch.hub.load('ultralytics/yolov5', 'custom',
                           path='classifier/model/best.pt')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        detect = model(frame)

        info = detect.pandas().xyxy[0]
        cv2.imshow('MovingObjectDetection', np.squeeze(detect.render()))

        t = cv2.waitKey(5)
        if t == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
