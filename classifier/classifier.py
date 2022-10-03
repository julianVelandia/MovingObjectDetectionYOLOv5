import torch
import cv2
import numpy as np


def moving_object_detection_video():
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


def moving_object_detection_frame():
    model = torch.hub.load('ultralytics/yolov5', 'custom',
                           path='classifier/model/best.pt')
    while True:
        img_name = input('\nDigita [P] para una imagen personalizada \n'
                     'Digita [D] para una imagen por defecto \n')

        if img_name == 'p' or img_name == 'P':
            try:
                frame = cv2.imread('classifier/' + img_name)
            except Exception as e:
                print('La imágen no se encuentra,\n'
                      ' - Recuerde mover la imágen a la carpeta classifier\n'
                      ' - Recuerde digitar con la extención .PNG o .JPG\n')
            break
        elif img_name == 'd' or img_name == 'D':
            frame = cv2.imread('classifier/DJI_0370.JPG')
            break


    detect = model(frame)

    info = detect.pandas().xyxy[0]

    while True:

        cv2.imshow('MovingObjectDetection', np.squeeze(detect.render()))
        t = cv2.waitKey(5)
        if t == 27:
            break
