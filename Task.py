import cv2
img = cv2.imread('car.jpg')
def edge(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(src=gray, ksize = (3,5), sigmaX = 0.5)
    edges = cv2.Canny(blurred, 70, 135)
    return blurred, edges
blurred, edges  = edge(img)
cv2.imshow('Edges', edges)
cv2.imshow('Original', img)
cv2.waitKey(0)