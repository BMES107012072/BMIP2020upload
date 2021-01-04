##影像簡介##
import numpy as np
import matplotlib.pyplot as plt
# open the binary data file as binary_file
with open("mri-a.raw", "rb") as binary_file:
    #read in the entire data set as an 1-d array
    I = np.fromfile(binary_file, dtype=np.ubyte)
# reshape the I into row * col 
I = I.reshape([256,256])

plt.imshow(I, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()