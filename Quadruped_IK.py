from Parameters import *
import math
from Transformation_Matrices import *

## Inverse Kinematics

'''
cos(theta2) = (1/2*L1*L2)*(x*x + y*y - L1*L1 - L2*L2)
sin(theta2) = +-sqrt(1-cos(theta2*theta2))

theta2 = +- atan(sin(theta2)/cos(theta2))

sin(theta1) = ((L1+L2*cos(theta2))*y - L2*sin(theta2)*x)/(x*x + y*y) 

cos(theta1) = ((L1+L2*cos(theta2))*x + L2*sin(theta2)*y)/(x*x + y*y)

theta1 = atan(sin(theta1)/cos(theta1))

'''
x = 0
y = 0

# Leg 2 (Type 2)
# theta 2
cos(theta22) =  (1 / (0.5 * l12 * l22)) * (x**2 + y**2 - l12**2 - l22**2)
# +/- ()
sin (theta22) = sqrt(1 - cos(theta22)**2)
# +/- atan
theta22 = atan(sin(theta22) / cos(theta22))

# theta 1
sin (theta12) = ((l12 + l22 * cos(theta22)) * y - l22 * sin(theta22) * x) / (x**2 + y**2)

cos (theta12) = ((l12 + l22 * cos(theta22)) * x + l22 * sin(theta22) * y) / (x**2 + y**2)

theta12 = atan(sin(theta12) / cos(theta12))

# Leg 1 (Type 1)
phi = theta11 + theta12 + theta13
x_w = x - l3 * cos(phi)
y_w = y - l3 * sin(phi)
alpha = atan(y_w / x_w)

# theta 2
theta21 = pi - acos((l11**2 + l21**2 - x_w**2 - y_w**2) / (2 * l11 * l21))

# theta 1
theta11 = alpha - acos((x_w**2 + y_w**2 + l11**2 - l21**2) / (2 * l11 * sqrt(x_w**2 + y_w**2)))

# theta3
theta31 = phi - theta11 - theta21