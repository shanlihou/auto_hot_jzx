import pyautogui
import cv2
from PIL import ImageGrab
import time
import ctypes
import win32con
import global_data
import utils
import gameconst


user32 = ctypes.windll.user32
ID1 = 105 #

class XzjState(object):
    START = 1
    AFTER_HUO_DON = 2
    RI_QIAN_START = 3

class NeedAct(object):
    RI_QIAN = 1


class AutoBot(object):
    def __init__(self) -> None:
        self.cur_state = XzjState.START

    def get_need_act(self):
        if utils.get_target_pos(gameconst.PicSearch.RI_QIAN) is not None:
            return NeedAct.RI_QIAN

    def run(self):
        while 1:
            utils.generate_screen()

            if self.cur_state == XzjState.START:
                pos = utils.get_target_pos(gameconst.PicSearch.HUO_DONG)
                if pos is not None:
                    pyautogui.click(pos[0] + 10, pos[1] + 10, duration=0.2)
                    self.cur_state = XzjState.AFTER_HUO_DON

            elif self.cur_state == XzjState.AFTER_HUO_DON:
                _need_act = self.get_need_act()
                if _need_act == NeedAct.RI_QIAN:
                    self.cur_state = XzjState.RI_QIAN_START

            elif self.cur_state == XzjState.RI_QIAN_START:
                pos = utils.get_target_pos(gameconst.PicSearch.RI_QIAN)
                if pos is not None:
                    pyautogui.click(pos[0] + 100, pos[1] + 200, duration=0.2)

            print('cur state', self.cur_state)
            time.sleep(1)


if __name__ == '__main__':
    ab = AutoBot()
    ab.run()
    # print(user32.RegisterHotKey(None, ID1, 0, win32con.VK_F10))
    # auto_go()
    # auto_shen_long_pan_one_turn()
