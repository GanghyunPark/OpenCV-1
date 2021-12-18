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
                        inputImage, (0, 0), None, scale, scale)
                else:
                    inputImage[x][y] = cv2.resize(
                        inputImage, (width, height), None, scale, scale)

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
                    inputImage, (inputImage[0].shape[1], inputImage[0].shape[0]), None, scale, scale)

        hor = np.hstack(inputImage)
        val = hor


kernel = np.ones((5, 5), np.uint8)

# Making img filter 5가지
img = cv2.imread("Resource/ganghyun.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(imgBlur, 100, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=3)
imgEroded = cv2.erode(imgDilation, kernel, iterations=2)

stackImages = StackImages(0.5, ([img, imgGray, imgBlur]))
cv2.imshow("Stack Images", stackImages)

# cv2.imshow("Ganghyun", img)
# cv2.imshow("Gray", imgGray)
# cv2.imshow("Blur", imgBlur)
# cv2.imshow("Canny", imgCanny)
# cv2.imshow("Dilation", imgDilation)
# cv2.imshow("Eroded", imgEroded)

cv2.waitKey(0)
