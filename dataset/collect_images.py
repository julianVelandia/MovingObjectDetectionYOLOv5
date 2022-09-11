import time
import random
import pyautogui

START_X = 1920 / 2 - 1080 / 2
START_Y = 0
WIDTH = 1080
HEIGHT = 1080
TOTAL = 130
SLEEP_PER_FRAME = 3
TRAIN_PATH = 'images/train/'
VAL_PATH = 'images/val/'
EXTENSION_PNG = '.png'

if __name__ == '__main__':
    time.sleep(10)

    for count in range(TOTAL):
        time.sleep(SLEEP_PER_FRAME)

        # Train 70% test 30%
        if random.randint(0, 9) < 7:
            path = TRAIN_PATH
        else:
            path = VAL_PATH

        im = pyautogui.screenshot(
            path + 'my_screenshot' + str(count) + EXTENSION_PNG,
            region=(START_X, START_Y, WIDTH, HEIGHT),
        )
