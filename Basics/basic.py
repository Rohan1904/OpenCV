import cv2

# 0 is id for our webcam
cap = cv2.VideoCapture(0)

# set is used to set size  3 = width 4 = height 10 = set briteness 
cap.set(3,1000)
cap.set(4,1000)
cap.set(10,100)
while True:
    # read() returns bool and img a
    success,img= cap.read()

    # To detect Edges canny image = all black with with white borders.
    # Canny para (image , threshold ,threshold) threshold for better face detection
    imgcanny = cv2.Canny(img,100,40)

    # TO convert to Gray Scale 
    imggrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Functions to show image output
    cv2.imshow("MyImage",img)
    cv2.imshow("Canny image",imgcanny)
    cv2.imshow("Gray Image",imggrey)
    cv2.waitKey(5)
