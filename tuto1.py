import cv2

img = cv2.imread("images/bird.jpg", -1)
print(img.shape)

cv2.imshow("Image test", img)

k = cv2.waitKey(0)


if k == ord('s'):
    cv2.imwrite("images/bird2.jpg", img)
    print("Image saved as bird2.jpg")
else:
    cv2.destroyAllWindows()
    print("Window closed without saving")