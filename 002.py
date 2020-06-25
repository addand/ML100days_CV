import cv2

img = cv2.imread('D:/lena.png', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
while True:
    cv2.imshow('hsv', hsv)
    cv2.imshow('hls', hls)
    cv2.imshow('lab', lab)
    if cv2.waitKey(0):
        cv2.destroyAllWindows()
        break
