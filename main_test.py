import cv2
import argparse
 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="img/K_2017.jpeg")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
# end