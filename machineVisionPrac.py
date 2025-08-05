import numpy as np
from math import sin, cos, pi

class PerspProj:
    
    def __init__(self):
        pass

    def getK(self, f: float, c_x: float = 0, c_y: float = 0):
        return np.array([
            [f, 0, c_x],
            [0, f, c_y],
            [0, 0, 1]
        ])
    
    def getR(self, theta_x: float, theta_y: float, theta_z: float):
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
        return rotR
    
    def getM(self, mat, t_x, t_y, t_z):
        t_array = np.array([[t_x],
                           [t_y],
                           [t_z]])
        M = np.append(mat, t_array, 1)
        return M

    def getC(self, M, X, Y, Z):
        worldVec = np.array(
            [
                [X],
                [Y],
                [Z],
                [1]
            ]
        )

        cameraVec = np.matmul(M, worldVec)
        return cameraVec
    
    def getS(self, K, C):
        sensorVec = np.matmul(K, C)
        return sensorVec




    


def main():
    p = PerspProj()
    K = p.getK(1)
    M = p.getM(p.getR(0, 0, 0), 2, 1, 3)
    C = p.getC(M, 1, 2, 3)
    S = p.getS(K, C)
    lambdaVal = 20  #pixel/length
    p = lambdaVal * S
    print(p)
    





main()