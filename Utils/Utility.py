import cv2
import numpy as np


def StackImages(scale, inputImage):
    rows = len(inputImage)
    cols = len(inputImage[0])
    # 들어오는 inputImage가 리스트형인지 isinstance로 알아본다. True and False로 출력된다.
    rowsAvailable = isinstance(inputImage[0], list)
    width = inputImage[0][0].shape[1]
    height = inputImage[0][0].shape[0]

    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                # 두세번째로 들어오는 이미지가 첫 이미지와 크기가 같을경우엔 scale에 따라 규모만 바꾸어주고, 크기가 다를경우엔 [0][0]이미지를 기준으로 크기를 맞춘 후 규모를 바꾼다.
                if inputImage[x][y].shape[:2] == inputImage[0][0].shape[:2]:
                    inputImage[x][y] = cv2.resize(
                        inputImage[x][y], (0, 0), None, scale, scale)
                else:
                    inputImage[x][y] = cv2.resize(
                        inputImage[x][y], (inputImage[0][0].shape[1], inputImage[0][0].shape[0]), None, scale, scale)

                # 오류사항 중, input되는 이미지가 흑백의 2차원일경우 컨버트하여 3차원으로 교체해준다
                if len(inputImage[x][y].shape) == 2:
                    inputImage[x][y] = cv2.cvtColor(
                        inputImage[x][y], cv2.COLOR_GRAY2BGR)

        blank = np.zeros((height, width, 3), np.uint8)
        hor = [blank] * rows
        hor_con = [blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(inputImage[x])
        ver = np.vstack(hor)

    else:
        for x in range(0, rows):
            if inputImage[x].shape[:2] == inputImage[0].shape[:2]:
                inputImage[x] = cv2.resize(
                    inputImage[x], (0, 0), None, scale, scale)
            else:
                inputImage[x] = cv2.resize(
                    inputImage[x], (inputImage[0].shape[1], inputImage[0].shape[0]), None, scale, scale)
            if len(inputImage[x].shape) == 2:
                inputImage[x] = cv2.cvtColor(inputImage[x], cv2.COLOR_GRAY2BGR)

        hor = np.hstack(inputImage)
        ver = hor
    return ver
