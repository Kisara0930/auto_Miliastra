import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
import time

def screenshot():
    global x_window, y_window
    window_title = '原神'
    app_window = gw.getWindowsWithTitle(window_title)[0]
    x_window, y_window, width, height = app_window.left, app_window.top, app_window.width, app_window.height
    shot = pyautogui.screenshot(region=(x_window, y_window, width, height))
    image_np = np.array(shot)
    img = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    return img

templ1 = cv2.imread('ready.png')
templ2 = cv2.imread('end.png')

def match(templ):
    img = screenshot()
    re = cv2.matchTemplate(img, templ, cv2.TM_SQDIFF_NORMED)
    if re[0][0] < 0.1:
        return True
    else:
        return False
    
def main():
    times = 0
    while True:
        time.sleep(3)
        pyautogui.press('p')


        if match(templ1):
            pyautogui.press('f')
            print(f'第{times+1}次开始')

        if match(templ2):
            x = x_window + 1400
            y = y_window + 880
            pyautogui.click(x, y, clicks=1, button='left')
            times += 1
            print(f"已经玩{times}次喵")


if __name__ == '__main__':
    main()
