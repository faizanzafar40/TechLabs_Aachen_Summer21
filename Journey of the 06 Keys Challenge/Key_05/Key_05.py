import cv2

image1 = cv2.imread("Encoded_Key.png")
image2 = cv2.imread("original.png")

difference = cv2.subtract(image1, image2)

Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
difference[mask != 255] = [0, 0, 255]

cv2.imwrite('diff.png', difference)