from Transformation_Matrices import *
from Parameters import *
from numpy.linalg import multi_dot

## Forward Kinematics

'''
Variable name convention as follows:

The first number represents the Frame # and the second number represents the Leg #

F11 is the First Frame on Leg 1
F21 is the Second Frame on Leg 1
F31 is the Third Frame on Leg 1

F14 is the First Frame on Leg 4
and so on...

'''

# Leg 1

O_T_F11 = Transformation(-l/2, -b/2, h/2)
F11_T_F21 = DH_Transformation(-90, 0, 0, 0)
F21_T_F31 = DH_Transformation(0, 0, l11, d1)
F31_T_F41 = DH_Transformation(0, 0, l21, d2)
F41_T_F51 = DH_Transformation(0, 0, l3, 0)

O_T_F51 = multi_dot([O_T_F11, F11_T_F21, F21_T_F31, F31_T_F41, F41_T_F51])


# Leg 4
O_T_F14 = Transformation(-l/2,  b/2, h/2)
F14_T_F24 = DH_Transformation(-90, 0, 0, 0)
F24_T_F34 = DH_Transformation(0, 0, l11, d1)
F34_T_F44 = DH_Transformation(0, 0, l21, d2)
F44_T_F54 = DH_Transformation(0, 0, l3, 0)

O_T_F53 = multi_dot([O_T_F14, F14_T_F24, F24_T_F34, F34_T_F44, F44_T_F54])

# Leg 2
O_T_F12 = Transformation(l/2, -b/2, h/2)
F12_T_F22 = DH_Transformation(-90, 0, 0, 0)
F22_T_F32 = DH_Transformation(0, 0, l12, d1)
F32_T_F42 = DH_Transformation(0, 0, l22, d2)

O_T_F42 = multi_dot([O_T_F12, F12_T_F22, F22_T_F32, F32_T_F42])

# Leg 3
O_T_F13 = Transformation(l/2,  b/2, h/2)
F13_T_F23 = DH_Transformation(-90, 0, 0, 0)
F23_T_F33 = DH_Transformation(0, 0, l12, d1)
F33_T_F43 = DH_Transformation(0, 0, l22, d2)

O_T_F43 = multi_dot([O_T_F13, F13_T_F23, F23_T_F33, F33_T_F43])

print ("Done:1")