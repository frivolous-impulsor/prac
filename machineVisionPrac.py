import numpy as np
from math import sin, cos, pi, sqrt
import matplotlib.pyplot as plt
from warping import *
from scipy import ndimage
from PIL import Image


class PerspProj:
    K = np.array([])
    R = np.array([])
    M = np.array([])
    
    def __init__(self):
        pass

    def setK(self, f: float, c_x: float = 0, c_y: float = 0):
        self.K = np.array([
            [f, 0, c_x],
            [0, f, c_y],
            [0, 0, 1]
        ])
    
    def setR(self, theta_x: float, theta_y: float, theta_z: float):
        rotX = np.array(
            [
                [1, 0, 0],
                [0, cos(theta_x), -sin(theta_x)],
                [0, sin(theta_x), cos(theta_x)]
            ]
        )
        rotY = np.array(
            [
                [cos(theta_y), 0, sin(theta_y)],
                [0, 1, 0],
                [-sin(theta_y), 0, cos(theta_y)]
            ]
        )
        rotZ = np.array(
            [
                [cos(theta_z), -sin(theta_z), 0],
                [sin(theta_z), cos(theta_z), 0],
                [0, 0, 1]
            ]
        )

        rotR = np.matmul(np.matmul(rotX, rotY), rotZ)
        self.R = rotR
    
    def setM(self, t_x, t_y, t_z):
        t_array = np.array([[t_x],
                           [t_y],
                           [t_z]])
        self.M = np.append(self.R, t_array, 1)

    def getC(self, X, Y, Z):
        worldVec = np.array(
            [
                [X],
                [Y],
                [Z],
                [1]
            ]
        )

        cameraVec = np.matmul(self.M, worldVec)
        return cameraVec
    
    def getS(self, C):
        sensorVec = np.matmul(self.K, C)
        return sensorVec 

def generatePrettyGradient():
    n = 256
    im = np.zeros((n,n,3))  #n by n by 3, 3 corresponding RGB color dimension
    for i in range(n):
        im[i,:,0] = i*0.0039
        im[i,:,1] = 1-i*0.0039
        im[i,:,2] = 1

    plt.imshow(im)    
    plt.show()

def removeDistortion():
    im = Image.open("IMG_0625.JPEG")
    [ydim, xdim] = im.size
    mid = round(max(xdim, ydim)/2)

    n = 100
    dst = griddify(shape_to_rect(im.size), n, n)
    src = dst

    k = 0.0000005
    dst = dst - mid

    dist = [0, 233, 467, 701, 935]
    distSize = len(dist)

    grid = np.zeros((distSize, distSize, 2))
    for row in range(distSize):
        for col in range(distSize):
            grid[row, col] = [dist[col], dist[row]]

    plt.plot(dst)
    plt.show()
    
def jpegCompression():
    pix = np.random.randint(255, size=(8,8))
    quant = np.ones((8,8)) * 2
     
    DCT = np.zeros((8,8))
    for row in range(8):
        for col in range(8):
            a_u = sqrt(1/8) if row ==0 else sqrt(x/8)
            a_v = sqrt(2/8) if col ==0 else sqrt(x/8)
            a = a_u*a_v
            sum = 0
            for x in range(8):
                for y in range(8):
                    sum+= pix[x,y]* cos((2*x+1)* row* pi/16)* cos((2*y+1)* col* pi/16)
            DCT[row, col] = a*sum

    quantized = np.floor(np.divide(DCT, quant))

    f, axarr = plt.subplots(1,2)
    axarr[0].imshow(pix)
    axarr[1].imshow(quantized)
    plt.show()

def convolution():
    fig, axarr = plt.subplots(1,4)
    img = Image.open('IMG_0625.JPEG')
    colored = np.asarray(img)
    grayed = np.dot(colored[...,:3], [0.299, 0.589, 0.114])
    axarr[0].imshow(grayed, aspect='auto' )
    #plt.imshow(grayed, cmap='gray', vmin=0, vmax=255)

    k_v = np.array([
        [-0.125,-0.25,-0.125],
        [0,0,0],
        [0.125, 0.25, 0.125]
    ])
    
    g_x = ndimage.convolve(grayed, k_v, mode='constant', cval=0.0)
    #plt.imshow(g_x, cmap='gray', vmin=0, vmax=255)
    axarr[1].imshow(g_x, aspect='auto' )


    k_h = np.array([
        [-0.125, 0, 0.125],
        [-0.25, 0, 0.25],
        [-0.125, 0, 0.125]
    ])

    g_y = ndimage.convolve(grayed, k_h, mode='constant', cval=0.0)
    #plt.imshow(g_y, cmap='gray', vmin=0, vmax=255)
    axarr[2].imshow(g_y, aspect='auto' )

    gradient = np.sqrt(np.square(g_x) + np.square(g_y))
    axarr[3].imshow(gradient, aspect='auto' )


    
    
    plt.show()

def convolution2():
    img_og = 1.0 * plt.imread('IMG_0625.JPEG')
    img = np.dot(img_og[...,:3], [0.299, 0.589, 0.114])
    filter = np.array([
        [-0.125,-0.25,-0.125],
        [0,0,0],
        [0.125, 0.25, 0.125]
    ])
    img_y = ndimage.convolve(img, filter, mode='reflect')
    img_x = ndimage.convolve(img, filter.T, mode='reflect')
    img_g = np.sqrt(img_x**2 + img_y**2)

    plt.figure(figsize=(15,5))
    plt.subplot(1,3,1)
    plt.imshow(img_y, cmap='gray')

    plt.subplot(1,3,2)
    plt.imshow(img_x, cmap='gray')
    plt.subplot(1,3,3)
    plt.imshow(img_g, cmap='gray')
    plt.show()
def main():
    convolution2()

main()