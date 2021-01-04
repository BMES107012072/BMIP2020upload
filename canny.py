import cv2
import numpy as np
with open("mri-a.256", "rb") as binary_file:
    #read in the entire data set as an 1-d array
   a = np.fromfile(binary_file, dtype=np.ubyte)

a= a.reshape([256,256])

edges = cv2.Canny(a,100,200)
cv2.imshow("canny",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
