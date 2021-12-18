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

# 사진을 같은 크기로 resize 하거나 줄이기
scale = 0.5
img = cv2.resize(img, (0, 0), None, scale, scale)
imgGray = cv2.resize(imgGray, (0, 0), None, scale, scale)
imgBlur = cv2.resize(imgBlur, (0, 0), None, scale, scale)
imgCanny = cv2.resize(imgCanny, (0, 0), None, scale, scale)
imgDilation = cv2.resize(imgDilation, (0, 0), None, scale, scale)
imgEroded = cv2.resize(imgEroded, (0, 0), None, scale, scale)

# Gray 상태를 BGR 상태인 3차원으로 돌리기
imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)
imgBlur = cv2.cvtColor(imgBlur, cv2.COLOR_GRAY2BGR)
imgCanny = cv2.cvtColor(imgCanny, cv2.COLOR_GRAY2BGR)
imgDilation = cv2.cvtColor(imgDilation, cv2.COLOR_GRAY2BGR)
imgEroded = cv2.cvtColor(imgEroded, cv2.COLOR_GRAY2BGR)

# 두개를 행렬합으로 이어붙이기
hor = np.hstack((img, imgGray, imgBlur))
hor2 = np.hstack((imgCanny, imgDilation, imgEroded))
var = np.vstack((hor, hor2))

cv2.imshow("5 Step Filters", var)

cv2.waitKey(0)
