import cv2
import numpy as np

# 512, 512, 3 의 빈 uint8 상태의 array 생성
img = np.zeros((512, 512, 3), np.uint8)

print(img)
# BGR 순 이며, img[] 내부는 height와 width 순
#img[20:30, 60:100] = 255, 0, 0

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)
cv2.rectangle(img, (350, 100), (450, 200), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (150, 400), 50, (255, 0, 0), cv2.FILLED)
cv2.putText(img, "Draw Shapes", (75, 50),
            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)
