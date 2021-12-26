import cv2
import numpy as np
from Utils import Utility

framewidth = 640
frameheight = 480

cap = cv2.VideoCapture(0)  # 0은 노트북 내장웹캠 사용, 1은 노트북 외장 웹캠을 사용

cap.set(3, framewidth)  # .set(3)은 화면의 width를 의미
cap.set(4, frameheight)  # .set(4)는 height를 의미


def empty(_):
    pass


cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold 1", "Parameters", 150, 255, empty)
cv2.createTrackbar("Threshold 2", "Parameters", 255, 255, empty)
cv2.createTrackbar("Area", "Parameters", 5000, 30000, empty)


def getContours(img, imgContour):

    # img를 보내고 retrieval method를 이용한다. externel outer line을 보내 그리는 방식.
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area", "Parameters")
        if area > areaMin:  # 일정 area 이하에서는 Contour를 그리지 않겠다는 것.
            cv2.drawContours(imgContour, contours, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)  # 만들어진 Contour Curve의 길이를 구한다
            # 형상을 근사하는 함수로 복수의 컨투어 점 어레이, 근사정확도, 근사커프 개폐 여부
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(imgContour, "Points : {}".format(str(len(approx))),
                        (x+w+20, y+20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(imgContour, "Area : {}".format(
                str(int(area))), (x+w+20, y+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)


while True:
    _, img = cap.read()
    imgContour = img.copy()

    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_RGB2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold 1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold 2", "Parameters")

    kernel = np.ones((5, 5))

    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    getContours(imgDil, imgContour=imgContour)

    imgStack = Utility.StackImages(
        0.8, ([img, imgGray, imgCanny], [imgDil, imgContour, imgContour]))

    cv2.imshow("Result", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
