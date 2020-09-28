import cv2

img = cv2.imread("image.jpg")

# TO get actual size of Image
print("Original Image size :",img.shape)

# Parameters (image source , ( width , Height))
resizedimg = cv2.resize(img,(720,480))


cv2.imshow("Resized Image output", resizedimg)

cv2.waitKey(0)
