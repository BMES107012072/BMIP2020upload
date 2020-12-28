#%%1
import numpy as np
import cv2
from matplotlib import pyplot as plt
##part(a)
blackphantom=np.zeros((256,256))
constructedphantom=blackphantom
for i in range(100):
     for k in range(50):
         constructedphantom[83+i][108+k]=255
         
plt.imshow(constructedphantom, cmap = 'gray')
plt.title('constructedphantom'), plt.xticks([]), plt.yticks([])
plt.show()   
## part (b)
F = np.fft.fft2(constructedphantom)
magnitude = np.abs(F)
plt.subplot(121),plt.imshow(magnitude, cmap = 'gray')
plt.title('1.b  magnitude responses'), plt.xticks([]), plt.yticks([])

import math
real=np.real(F)
imag=np.imag(F)

phase=np.zeros((256,256))
for i in range(256):
    for j in range(256):
        phase[i][j]=math.atan2(imag[i][j],real[i][j])
plt.subplot(122),plt.imshow(phase, cmap = 'gray')
plt.title('1.b  phase responese'), plt.xticks([]), plt.yticks([])
plt.show()
    
##part(c)
Menhance= 5*np.log(1+magnitude)
plt.imshow(Menhance, cmap = 'gray')
plt.title('1.c after enhance '), plt.xticks([]), plt.yticks([])
plt.show()
##part(d)
NEWconstructedphantom=np.zeros((256,256))
for m in range(256):
    for n in range(256):
     NEWconstructedphantom[m][n]=(-1)**(m+n)*constructedphantom[m][n]
     
G= np.fft.fft2(NEWconstructedphantom)    
MenhanceG= 10*np.log(1+np.abs(G))
plt.subplot(121),plt.imshow(MenhanceG, cmap = 'gray')
plt.title('1.d  magnitude responses'), plt.xticks([]), plt.yticks([])

import math
realG=np.real(G)
imagG=np.imag(G)

Gphase=np.zeros((256,256))
for i in range(256):
    for j in range(256):
        Gphase[i][j]=math.atan2(imagG[i][j],realG[i][j])

plt.subplot(122),plt.imshow(Gphase, cmap = 'gray')
plt.title('1.d  phase responese'), plt.xticks([]), plt.yticks([])
plt.show()
#%%2
import numpy as np
import cv2
from matplotlib import pyplot as plt
# open the binary data file as binary_file
with open("mri-a.256", "rb") as binary_file:
    #read in the entire data set as an 1-d array
   image = np.fromfile(binary_file, dtype=np.ubyte)

# reshape the data into row * col 
image=  image.reshape([256,256])

NEWimage=np.zeros((256,256))
for m in range(256):
    for n in range(256):
     NEWimage[m,n]=image[m,n]*(-1)**(m+n)
     
FMRI=np.fft.fft2(NEWimage)
MenhanceFMRI= 10*np.log(1+np.abs(FMRI))
plt.subplot(121),plt.imshow(MenhanceFMRI, cmap = 'gray')
plt.title('2  magnitude responses'), plt.xticks([]), plt.yticks([])

import math
realMRI=np.real(FMRI)
imagMRI=np.imag(FMRI)

MRIphase=np.zeros((256,256))
for i in range(256):
    for j in range(256):
        MRIphase[i][j]=math.atan2(imagMRI[i][j],realMRI[i][j])

plt.subplot(122),plt.imshow(MRIphase, cmap = 'gray')
plt.title('2  phase responses'), plt.xticks([]), plt.yticks([])
plt.show() 
#%%3 
## part a
F3=np.fft.fft2(image)
magnitude3a = np.abs(F3)
f3a=np.abs(np.fft.ifft2(magnitude3a)) 
f3a=10*np.log(1+np.abs(f3a))
plt.imshow(f3a, cmap = 'gray')
plt.title('3.a phase=0'), plt.xticks([]), plt.yticks([])
plt.show()

## part b
import cmath
phase3b=np.unwrap(np.angle(F3))
F3b=np.zeros((256,256))*complex(0,1) ##convert data type to complex
Jphase3b=complex(0,1)*phase3b
for m in range(256):
    for n in range(256):
            F3b[m][n]=cmath.exp(Jphase3b[m][n])
f3b=np.log(1+np.abs(np.fft.ifft2(F3b))) 
plt.imshow(f3b, cmap = 'gray')
plt.title('3.b magnitude=1'), plt.xticks([]), plt.yticks([])
plt.show()

##another method for part b
magnitude_spectrum1=magnitude3a
F1=F3/magnitude_spectrum1
inverseF1=np.abs(np.fft.ifft2(F1))
inverseF1=np.log(1+inverseF1)
plt.imshow(inverseF1, cmap = 'gray')
plt.title('3.b magnitude=1 method 2'), plt.xticks([]), plt.yticks([])
plt.show()
## part c
plt.subplot(131),plt.imshow(image, cmap = 'gray')
plt.title('3.c original'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(f3a, cmap = 'gray')
plt.title('phase=0'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(f3b, cmap = 'gray')
plt.title('magnitude=1'), plt.xticks([]), plt.yticks([])
plt.show()


