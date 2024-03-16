import cv2

# Load an image
image = cv2.imread("C:\Users\Родион\Pictures\Костя_2017.jpeg")

# Display the image
cv2.imshow("OpenCV Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# end