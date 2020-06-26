import cv2
import numpy as np

img = cv2.imread('D:/lena.png', cv2.IMREAD_COLOR)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# item 1
change_percentage = 0.2
img_hsv_down = img_hsv.astype('float32')
img_hsv_down[:, :, -1] = img_hsv_down[:, :, -1]/255 - change_percentage
img_hsv_down[img_hsv_down[:, :, -1] < 0] = 0
img_hsv_down[:, :, -1] = img_hsv_down[:, :, -1]*255
img_hsv_down = img_hsv_down.astype('uint8')
img_hsv_down = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

img_hsv_up = img_hsv.astype('float32')
img_hsv_up[:, :, -1] = img_hsv_up[:, :, -1]/255 + change_percentage
img_hsv_up[img_hsv_up[:,:,-1] > 1] = 1
img_hsv_up[:,:,-1] = img_hsv_up[:,:,-1]*255
img_hsv_up = img_hsv_up.astype('uint8')
img_hsv_up = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img_composed = np.hstack((img_hsv_up, img_hsv_down))
while True:
    cv2.imshow('change saturation', img_composed)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break

# item 2 : case 1
# 每個 channel 個別做直方圖均衡
(b, g, r) = cv2.split(img)
img_bH = cv2.equalizeHist(b)
img_gH = cv2.equalizeHist(g)
img_rH = cv2.equalizeHist(r)

# 組合經過直方圖均衡的每個 channel
img_bgr_equal = cv2.merge([img_bH, img_gH, img_rH])

# item2 : case 2 - 轉換 color space 後只對其中一個 channel 做直方圖均衡
img_hsv_equal = img_hsv.copy()
img_hsv_equal[..., 1] = cv2.equalizeHist(img_hsv_equal[..., 1])
img_hsv_equal = cv2.cvtColor(img_hsv_equal, cv2.COLOR_HLS2BGR)

# 組合圖片 + 顯示圖片
img_bgr_equalHist = np.hstack((img_bgr_equal, img_hsv_equal))
while True:
    # 比較 (原圖, BGR color space 對每個 channel 做直方圖均衡, HSV color space 對明度做直方圖均衡)
    cv2.imshow('bgr equal histogram', img_bgr_equalHist)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break

# item 3
add_contrast = cv2.convertScaleAbs(img, alpha=2.0, beta=0)
add_lightness = cv2.convertScaleAbs(img, alpha=1.0, beta=100)
# 組合圖片 + 顯示圖片
img_contrast_light = np.hstack((add_contrast, add_lightness))
while True:
    # 比較不同程度的對比 / 明亮
    cv2.imshow('adjust contrast and brighness', img_contrast_light)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break