import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

# Making img filter 5가지
img = cv2.imread("Resource/ganghyun.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(imgBlur, 100, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=3)
imgEroded = cv2.erode(imgDilation, kernel, iterations=2)


cv2.waitKey(0)
