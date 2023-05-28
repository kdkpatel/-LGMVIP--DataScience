import cv2
image = cv2.imread('img1.jpg') 
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img) 
invertedblur = cv2.bitwise_not(grey_img)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
cv2.imwrite("img1.jpg", sketch) 


