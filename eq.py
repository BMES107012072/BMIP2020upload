#https://medium.com/@cindylin_1410/%E6%B7%BA%E8%AB%87-opencv-%E7%9B%B4%E6%96%B9%E5%9C%96%E5%9D%87%E8%A1%A1%E5%8C%96-ahe%E5%9D%87%E8%A1%A1-clahe%E5%9D%87%E8%A1%A1-ebc9c14a8f96
import cv2
import numpy as np

from matplotlib import pyplot as plt

# read image
with open("mri-bright.256", "rb") as binary_file:
    #read in the entire data set as an 1-d array
   I0 = np.fromfile(binary_file, dtype=np.ubyte)

# reshape the data into row * col 
I0 = I0.reshape([256,256])


# open the binary data file as binary_file
with open("mri-dark.256", "rb") as binary_file:
    #read in the entire data set as an 1-d array
   I1 = np.fromfile(binary_file, dtype=np.ubyte)

# reshape the data into row * col 
I1 = I1.reshape([256,256])


# image equalization
equalize_imgI0 = cv2.equalizeHist(I0)
# create clahe image
clahe = cv2.createCLAHE()
clahe_imgI0 = clahe.apply(I0)

## show image
cv2.imshow("image", I0)
cv2.imshow("equal_image", equalize_imgI0)
cv2.imshow("clahe_image", clahe_imgI0)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# plot image histogram
plt.hist(I0.ravel(), 256, [0, 255],label= 'original image')
plt.hist(equalize_imgI0.ravel(),256, [0, 255],label= 'equalize image')
plt.hist(clahe_imgI0.ravel(), 256, [0, 255],label= 'clahe image')
plt.legend()

#%%

# image equalization
equalize_imgI1 = cv2.equalizeHist(I1)
# create clahe image
clahe = cv2.createCLAHE()
clahe_imgI1 = clahe.apply(I1)

## show image
cv2.imshow("image", I1)
cv2.imshow("equal_image", equalize_imgI1)
cv2.imshow("clahe_image", clahe_imgI1)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# plot image histogram
plt.hist(I1.ravel(), 256, [0, 255],label= 'original image')
plt.hist(equalize_imgI1.ravel(),256, [0, 255],label= 'equalize image')
plt.hist(clahe_imgI1.ravel(), 256, [0, 255],label= 'clahe image')
plt.legend()

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
#%%
# read image
with open("mri-bright.256", "rb") as binary_file:
    #read in the entire data set as an 1-d array
   I0 = np.fromfile(binary_file, dtype=np.ubyte)

# reshape the data into row * col 
I0 = I0.reshape([256,256])


equ = cv.equalizeHist(I0)
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




