import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

image = img.imread("C:\\Users\\komputer 31\\Downloads\\pp.jpg", mode='F')

sx = np.array([
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]
    
])

SY = np.array([
    [-1,-2,-1],
    [0,0,0],
    [1,2,1]
])

imgPad = np.pad(image,pad_width=1,mode='constant', constant_values=0)
GX = np.zeros_like(image)
GY = np.zeros_like(image)

for y in range(1,imgPad.shape[0]-1):
    for x in range(1,imgPad.shape[1]-1):
        area = imgPad[y-1:y+2,x-1:x+2]
        GX[y-1,x-1] = np.sum(area * sx)
        GY[y-1,x-1] = np.sum(area * SY)
        
G = np.sqrt(GX**2 + GY**2)
G = (G/G.max()) * 255
G = np.clip(G,0,255)
G = G.astype(np.uint8)

plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.imshow(image)

plt.subplot(2,2,2)
plt.imshow(GX,cmap='gray')

plt.subplot(2,2,3)
plt.imshow(GY,cmap='gray')
        
plt.subplot(2,2,4)
plt.imshow(G,cmap='gray')
            
plt.show()