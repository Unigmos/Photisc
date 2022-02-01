#-------------------------------------------------------------------------------
# Name:         make_content
# Purpose:      画像作成用プログラム
#
# Author:       Shaneron
#
# Created:      2022/01/09
# Copyright:    (c) Shaneron 2022
#-------------------------------------------------------------------------------

def circle_test():
    try:
        from matplotlib import pyplot as plt
        from matplotlib import patches as patch
        import matplotlib.patches as patches

        img = plt.imread('blank.png')
        fig, ax = plt.subplots()
        im = ax.imshow(img)
        circle = patch.Circle((540, 520), radius=320, transform=ax.transData)
        im.set_clip_path(circle)
        ax.axis('off')
        plt.savefig('clip_circle.png',dpi=150)

    except ModuleNotFoundError as NO_MODULE_ERROR:
        print(f"ModuleNotFoundError:{NO_MODULE_ERROR}at test")
    except FileNotFoundError as NOT_FOUND_ERROR:
        print(f"ModuleNotFoundError:{NOT_FOUND_ERROR}at test")

def canvas():
    try:
        import cv2
        import numpy as np

        height = 500
        width = 1500
        blank = np.zeros((height, width, 3))
        # 背景色設定
        blank += [84,66,59][::-1]

        # 線描画(外枠)
        cv2.line(blank, (50, 50), (1450, 50), (255, 255, 255), thickness=6, lineType=cv2.LINE_AA, shift=0)
        cv2.line(blank, (50, 50), (50, 80), (255, 255, 255), thickness=6, lineType=cv2.LINE_AA, shift=0)
        cv2.line(blank, (1450, 50), (1450, 80), (255, 255, 255), thickness=6, lineType=cv2.LINE_AA, shift=0)

        cv2.line(blank, (50, 450), (1450, 450), (255, 255, 255), thickness=6, lineType=cv2.LINE_AA, shift=0)
        cv2.line(blank, (50, 450), (50, 420), (255, 255, 255), thickness=6, lineType=cv2.LINE_AA, shift=0)
        cv2.line(blank, (1450, 450), (1450, 420), (255, 255, 255), thickness=6, lineType=cv2.LINE_AA, shift=0)

        # 線描画(中心円)
        cv2.circle(blank, (750, 250), 100, (255, 255, 255), thickness=3, lineType=cv2.LINE_AA)

        # 線描画(円左側横線)
        cv2.line(blank, (50, 245), (650, 245), (255, 255, 255), thickness=3, lineType=cv2.LINE_AA, shift=0)
        cv2.line(blank, (50, 255), (650, 255), (255, 255, 255), thickness=3, lineType=cv2.LINE_AA, shift=0)

        # 線描画(円右側横線)
        cv2.line(blank, (850, 245), (1450, 245), (255, 255, 255), thickness=3, lineType=cv2.LINE_AA, shift=0)
        cv2.line(blank, (850, 255), (1450, 255), (255, 255, 255), thickness=3, lineType=cv2.LINE_AA, shift=0)

        # 画像書き出し
        cv2.imwrite('blank.png',blank)

    except ModuleNotFoundError as NO_MODULE_ERROR:
            print(f"ModuleNotFoundError:{NO_MODULE_ERROR}at test")

def main():
    pass


if __name__ == '__main__':
    #circle_test()
    canvas()
