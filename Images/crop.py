import cv2

img = cv2.imread("image.jpg")

# TO get actual size of Image
print("Original Image size :",img.shape)

# Parameters (image source , ( width , Height))
resizedimg = cv2.resize(img,(720,480))

print("Resized Image size =",resizedimg)

# Cropped Image
# Parameters img.[height , width ]
# imp :- Img Coordinates are different from general mathamatical conventions

imgCropped = resizedimg[0:300,0:480]

cv2.imshow("Resized output", resizedimg)
cv2.imshow("Cropped Image",imgCropped)

cv2.waitKey(0)
