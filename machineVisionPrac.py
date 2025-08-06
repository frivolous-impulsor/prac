import numpy as np
from math import sin, cos, pi
import matplotlib.pyplot as plt


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
    





    


def main():
    p = PerspProj()
    p.setK(1)
    p.setR(pi/6, pi/6, 0)
    p.setM(-0.5, -0.5, 100)

    points = [[0, 0, 0],
              [1,0,0],
              [1,1,0],
              [0,1,0],
              [0,0,1],
              [1,0,1],
              [1,1,1],
              [0,1,1]]
    
    translated_points = []

    for point in points:
        C = p.getC(point[0], point[1], point[2])
        S = p.getS(C)
        lambdaVal = 20  #pixel/length
        p_vec = lambdaVal * S
        x = float(p_vec[0]/p_vec[2])
        y = float(p_vec[1]/p_vec[2])
        translated_points.append([x,y])
    
    coord_x, coord_y = zip(*translated_points)
    print(coord_x)
    print(coord_y)

    
    fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    ax.scatter(list(coord_x), list(coord_y), s=50, facecolor='C0', edgecolor='k')  # Plot some data on the Axes.
    plt.show()                           # Show the figure.

    
    





main()