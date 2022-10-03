from classifier.classifier import moving_object_detection_video, moving_object_detection_frame

if __name__ == '__main__':
    print('\n Detección de desechos plásticos \n sobre superficies acuáticas mediante \n el uso de inteligencia artificial \n\n'
          '-------------------------------------\n')

    while True:
        op = input('Pulse [V] para detectar con video '
                   '\n Pulse [I] para detectar con imágen'
                   '\n Pulse [S] o [CTRL+c] para salir\n')

        if op == 'v' or op == 'V':
            moving_object_detection_video()
            break
        elif op == 'i' or op == 'I':
            moving_object_detection_frame()
            break
        elif op == 's' or op == 'S':
            print('Salida')
            break
