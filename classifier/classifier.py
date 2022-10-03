import torch
import cv2
import numpy as np


def moving_object_detection_video():
    model = torch.hub.load('ultralytics/yolov5', 'custom',
                           path='classifier/model/best.pt')
    cap = cv2.VideoCapture(0)
    print('\n Pulse [CTRL+c] para salir\n')
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
        menu_option = input('\nDigita [P] para una imagen personalizada \n'
                     'Digita [D] para una imagen por defecto \n')

        if menu_option == 'p' or menu_option == 'P':
            img_name = input('\nDigita el nombre de la imágen con la extención .PNG o .JPG\n')
            try:
                frame = cv2.imread('classifier/' + img_name)
                detect = model(frame)
                print('\n Pulse [S] o [CTRL+c] para salir\n')

            except Exception:
                print('La imágen no se encuentra,\n'
                      ' - Recuerde mover la imágen a la carpeta classifier\n'
                      ' - Recuerde digitar con la extención .PNG o .JPG\n')
                continue
            break
        elif menu_option == 'd' or menu_option == 'D':
            frame = cv2.imread('classifier/DJI_0370.JPG')
            detect = model(frame)
            print('\n Pulse [CTRL+c] para salir\n')

            break



    info = detect.pandas().xyxy[0]

    while True:

        cv2.imshow('MovingObjectDetection', np.squeeze(detect.render()))
        t = cv2.waitKey(5)
        if t == 27:
            break
