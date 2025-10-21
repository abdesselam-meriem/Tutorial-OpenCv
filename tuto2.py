import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/bird.jpg", 1)

H, W = img.shape[:2]
print(H, W)

#lines 
img = cv2.line(img, (0,0),(0,200),(255,0,0),5)
img = cv2.line(img, (0,0),(200,0),(255,0,0),5)
img = cv2.arrowedLine(img, (0,0),(200,200),(255,255,0),5)


pts = np.array([[0, H-1],[W-1, H-1],[W-1, 0]], np.int32)
img = cv2.polylines(img, [pts], True, (0,255,0),5)


#rectangle
img = cv2.rectangle(img, (300,300), (400,400), (0,0,255), 5)

#text
img = cv2.putText(img, "OpenCV bird  ", (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)

#circle
img = cv2.circle(img, (30,30), 30, (0,255,255), 3)


#pour inverser les canaux de couleur BGR à RGB
plt.imshow(img [:,:,::-1])
plt.show()




