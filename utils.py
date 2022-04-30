import global_data
import gameconst
from PIL import ImageGrab
import cv2
import os


def generate_screen():
    sc_region = (0, 0, 1900, 1000) #距离左上右下的像素
    sc_img = ImageGrab.grab(sc_region)
    save_path = os.path.join(gameconst.SCREEN_NAME, 'screen_region.jpg')
    sc_img.save(save_path)

    global_data.SCREEN = cv2.imread(save_path)

def get_target_pos(filename):
    target = cv2.imread(os.path.join(gameconst.PIC_NAME, filename))
    result = cv2.matchTemplate(target, global_data.SCREEN, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # print(min_val, max_val, min_loc, max_loc)
    if min_val < 0.01:
        _x, _y = min_loc
        return (_x, _y)

    return None