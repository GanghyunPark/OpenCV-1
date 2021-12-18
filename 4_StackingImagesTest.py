import cv2
import numpy as np
from Utils import Utility


frameWidth = 640
frameHeight = 480

#cap = cv2.VideoCapture("Resource/testVideo.mp4")
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    kernel = np.ones((5, 5), np.uint8)

    # Making img filter 5가지
    #img = cv2.imread("Resource/ganghyun.jpg")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=3)
    imgEroded = cv2.erode(imgDilation, kernel, iterations=2)

    imgBlank = np.zeros((100, 100), np.uint8)

    stackImages = Utility.StackImages(0.5, ([img, imgGray, imgBlur], [
        imgCanny, imgDilation, imgBlank]))
    cv2.imshow("Stack Images", stackImages)

    # cv2.imshow("Ganghyun", img)
    # cv2.imshow("Gray", imgGray)
    # cv2.imshow("Blur", imgBlur)
    # cv2.imshow("Canny", imgCanny)
    # cv2.imshow("Dilation", imgDilation)
    # cv2.imshow("Eroded", imgEroded)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
