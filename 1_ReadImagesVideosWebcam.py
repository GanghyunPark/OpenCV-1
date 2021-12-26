import cv2

frameWidth = 640
frameHeight = 480

#cap = cv2.VideoCapture("Resource/testVideo.mp4")
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Video", img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
