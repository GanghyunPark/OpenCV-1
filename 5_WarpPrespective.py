import cv2
import numpy as np

img = cv2.imread('Resource/credit.jpg')
# 281,33  747,67   391,1259   867,1141

width, height = 300, 600
pts1 = np.float32([[281, 33], [747, 67], [391, 1259], [867, 1141]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, matrix, (width, height))
print(pts1)

for x in range(4):
    cv2.circle(img, (int(pts1[x][0]), int(pts1[x][1])),
               5, (0, 0, 255), cv2.FILLED)

cv2.imshow("Original Image", img)
cv2.imshow("Output Image", output)
cv2.waitKey(0)
