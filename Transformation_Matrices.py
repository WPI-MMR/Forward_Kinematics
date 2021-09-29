from math import *
from sympy import *

# Defining a general DH Transformation Matrix

def DH_Transformation(theta, alpha, a, d):

    T = [[cos(theta),             -sin(theta),            0,            a            ],
        [sin(theta)*cos(alpha),  cos(theta)*cos(alpha),  -sin(alpha),   -d*sin(alpha)],
        [sin(theta)*sin(alpha),  cos(theta)*sin(alpha),   cos(alpha),    d*cos(alpha)],
        [0,                      0,                      0,             1            ]]

    return T
    
# Defining a general Transformation Matrix from Origin to Hip

def Transformation(l, b, h):

    T = [[1, 0, 0, l],
         [0, 1, 0, b],
         [0, 0, 1, h],
         [0, 0, 0, 1]]


    return T
