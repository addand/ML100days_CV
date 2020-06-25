import cv2

img = cv2.imread('D:/lena.png', cv2.IMREAD_COLOR)

# set other channel to 0
b = img.copy()
b[:,:,1] = 0
b[:,:,2] = 0

g = img.copy()
g[:,:,0] = 0
g[:,:,2] = 0

r = img.copy()
r[:,:,0] = 0
r[:,:,1] = 0

while True:
    cv2.imshow('rgb', img)
    cv2.imshow('B',b)
    cv2.imshow('G',g)
    cv2.imshow('R',r)
    if cv2.waitKey(0):
        cv2.destroyAllWindows()
        break
