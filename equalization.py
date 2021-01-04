#%%Histogram Equalization wiki.jpg
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('wiki.jpg',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

equ = cv.equalizeHist(img)
cv.imshow("equal_image", equ)
cv.waitKey(0)
cv.destroyAllWindows() 
hist,bins = np.histogram(equ.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
#%%Histogram Equalization "mri-bright.256"
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# read image
with open("mri-bright.256", "rb") as binary_file:
    #read in the entire data set as an 1-d array
   I0 = np.fromfile(binary_file, dtype=np.ubyte)

# reshape the data into row * col 
I0 = I0.reshape([256,256])


equ = cv.equalizeHist(I0)
cv.imshow("bright equal_image", equ)
cv.waitKey(0)
cv.destroyAllWindows() 
hist,bins = np.histogram(equ.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.title('bright equal_image')
plt.show()
plt.hist(I0.ravel(), 256, [0, 255])
plt.title('bright original histogram')
plt.show()
#%%Histogram Equalization "mri-dark.256"
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# read image
with open("mri-dark.256", "rb") as binary_file:
    #read in the entire data set as an 1-d array
   I0 = np.fromfile(binary_file, dtype=np.ubyte)

# reshape the data into row * col 
I0 = I0.reshape([256,256])


equ = cv.equalizeHist(I0)
cv.imshow("dark equal_image", equ)
cv.waitKey(0)
cv.destroyAllWindows() 
hist,bins = np.histogram(equ.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.title('dark equal_image')
plt.show()
plt.hist(I0.ravel(), 256, [0, 255])
plt.title('dark original histogram')
plt.show()

