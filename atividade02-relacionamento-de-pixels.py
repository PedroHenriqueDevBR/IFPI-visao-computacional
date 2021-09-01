import cv2
import numpy as np

img = cv2.imread('/home/pedro/Dev/PythonProjects/VisaoComputacional/assets/perfil-2.jpg', 0)
img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
ret, labels = cv2.connectedComponents(img)

label_hue = np.uint8(179*labels/np.max(labels))
blank_ch = 255*np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

labeled_img[label_hue==0] = 0

cv2.imshow('/home/pedro/Dev/PythonProjects/VisaoComputacional/assets/perfil-result.jpg', labeled_img)
cv2.waitKey()