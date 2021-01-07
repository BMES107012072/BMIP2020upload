## 1. Implement the Marr-Hildreth edge-detection algorithm
import numpy as np
import cv2
# MarrHildreth演算法說明
##第一變數為原圖像,第二變數為高斯濾波size大小nxn之n,第三變數為高斯濾波之sigma
##第四變數是可調整的比例,threshold=比例*原圖經LoG後的最大值
def MarrHildreth(image,n,sigma,percect):
    Gaussian(image,n,sigma)
    Laplacian(blurred)
    zerocrossing(laplacian,percect)
#高斯滤波    
def Gaussian(image,n,sigma):
 ##step1  Gaussian filter
 global blurred
 blurred =cv2.GaussianBlur(image,(n,n),sigma)
 cv2.imshow("Gaussian filter",blurred)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
 return blurred
 ##step2  Laplacian 
def Laplacian(blurred):
 global laplacian
 laplacian=np.zeros((256,256))   
 for m in range (1,255): ##圖像最外圍一圈不做處理
     for n in range(1,255):
         laplacian[m][n]=int(blurred[m-1][n-1])+int(blurred[m][n-1])+int(blurred[m+1][n-1])\
                   +int(blurred[m-1][n])-8*int(blurred[m][n])+int(blurred[m+1][n])\
                   +int(blurred[m-1][n+1])+int(blurred[m+1][n])+int(blurred[m+1][n+1]) 
 cv2.imshow("laplacian",laplacian)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
 return laplacian                            
 ##step3  zero crossing
def zerocrossing(laplacian,percect): 
    threshold=percect*np.max(laplacian)
    global crossing
    crossing=np.zeros((256,256))
    for j in range(1,255): ##圖像最外圍一圈不做處理 j=1,2,3....254不含255及0
        for k in range(1,255): 
            opposing=0
            for jj in range(j-1,j+2):  #jj=j-1 ,j, j+1
                 for kk in range(k-1,k+2): #kk=k-1 k k+1
                     if laplacian[j][k]*laplacian[jj][kk]<0: ##check上下左右 斜前斜後 自己乘自己>0 不影響
                         difference=np.abs(laplacian[j][k])+np.abs(laplacian[jj][kk])
                         if difference>threshold:
                             opposing=opposing+1    
           
            if opposing>=2:
                crossing[j][k]=laplacian[j][k]
    cv2.imshow("Edge",crossing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return crossing            
            
#%%2 Apply the Marr-Hildreth edge-detection algorithm to three mri images
with open("mri-a.256", "rb") as binary_file:
    #read in the entire data set as an 1-d array
   a = np.fromfile(binary_file, dtype=np.ubyte)

# reshape the data into row * col 
a= a.reshape([256,256])

##演算法實施
##第一變數為原圖像,第二變數為高斯濾波size大小nxn之n,第三變數為高斯濾波之sigma
##第四變數是可調整的比例,threshold=比例*原圖經LoG後的最大值
##threshold percent=0.04
MarrHildreth(a,7,1,0.04) 

##threshold percent=0.1
MarrHildreth(a,7,1,0.1)

##threshold percent=0.2
MarrHildreth(a,7,1,0.2)

