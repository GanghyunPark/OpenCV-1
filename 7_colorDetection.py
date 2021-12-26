import cv2
from numpy import empty
import numpy as np

framewidth = 640
frameheight = 480
cap = cv2.VideoCapture(0)  # 0은 노트북 내장웹캠 사용, 1은 노트북 외장 웹캠을 사용

cap.set(3, framewidth)  # .set(3)은 화면의 width를 의미
cap.set(4, frameheight)  # .set(4)는 height를 의미


def empty(a):
    pass


# Tracker를 만들어 적정 Min Max HSV를 조절할 수 있게 한다.
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)


while True:
    _, img = cap.read()

    # HSV(Hue, Saturation, value)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 트랙바를 생성
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

    # 트랙바가 mask에서 작동할 수 있도록 조정 및 result에서 mask와 img가 동시에 보일수 있도록 함
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    h_stack = np.hstack((img, mask, result))

    # cv2.imshow("Original", img)
    # cv2.imshow("HSV Color Space", imgHSV)
    # cv2.imshow('Mask', mask)
    # cv2.imshow('Result', result)
    cv2.imshow("Stacked img, mask, result", h_stack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
