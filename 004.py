import cv2
import numpy as np
import time

img = cv2.imread('D:/lena.png', cv2.IMREAD_COLOR)

img_vflip = img[::-1, :, :]
img_hflip = img[:, ::-1, :]
img_hvflip = img[::-1, ::-1, :]

hflip = np.vstack((img, img_vflip, img_hvflip))
#while True:
#    cv2.imshow('flip image', hflip)
#    k = cv2.waitKey(0)
#    if k == 27:
#        cv2.destroyAllWindows()
#        break

img_test = cv2.resize(img, None, fx=0.2, fy=0.2)
fx, fy = 8, 8
# 鄰近差值 scale + 計算花費時間
start_time = time.time()
img_area_scale = cv2.resize(img_test, None, fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)
print('INTER_NEAREST zoom cost {}'.format(time.time() - start_time))

start_time = time.time()
img_cubic_scale = cv2.resize(img_test, None, fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
print('INTER_CUBIC zoom cost {}'.format(time.time() - start_time))

# 組合 + 顯示圖片
img_zoom = np.hstack((img_area_scale, img_cubic_scale))
while True:
    cv2.imshow('zoom image', img_zoom)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break

# 設定 translation transformation matrix
# x 平移 50 pixel; y 平移 100 pixel
M = np.array([[1, 0, 50],
             [0, 1, 100]],
             dtype=np.float32)
shift_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# 組合 + 顯示圖片
img_shift = np.hstack((img, shift_img))
while True:
    cv2.imshow('shift image', img_shift)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break