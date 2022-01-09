#-------------------------------------------------------------------------------
# Name:         make_content
# Purpose:      画像作成用プログラム
#
# Author:       Shaneron
#
# Created:      2022/01/09
# Copyright:    (c) Shaneron 2022
#-------------------------------------------------------------------------------

def test():
    try:
        import cv2
        import numpy as np

        height = 400
        width = 400
        blank = np.zeros((height, width, 3))
        blank += [0,255,0][::-1]

        cv2.imwrite('blank.png',blank)

    except ModuleNotFoundError as NO_MODULE_ERROR:
        print("ModuleNotFoundError:", NO_MODULE_ERROR, "at test")
    except FileNotFoundError as NOT_FOUND_ERROR:
        print("FileNotFoundError:", NOT_FOUND_ERROR, "at test")

def main():
    pass


if __name__ == '__main__':
    test()