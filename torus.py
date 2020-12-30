# -*- coding: utf-8 -*-
"""Torus.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YZmTW-7a1htNhtKOd3VxcG7YVB9mZEPG

#Torus
This python notebook will show the proof of the formula for volume of the torus using the Jacobian Method and the Triple Integrals Method computationally

###Import init_printing to display the integral result in a pretty way
"""

from sympy import init_printing
init_printing()

"""###Import required libraries"""

import numpy as np
import sympy as sp
from sympy import integrate, Symbol, symbols, cos, sin, Matrix, pi, exp, plot, diff
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

"""###Create the torus graph and the formula for volume of torus"""

#Generate torus
angle = np.linspace(0, 2 * np.pi, 20)
theta, phi = np.meshgrid(angle, angle)

#toroidal coordinate system
r, R = 3, 8.5
X = (R + r * np.cos(phi)) * np.cos(theta)
Y = (R + r * np.cos(phi)) * np.sin(theta)
Z = r * np.sin(phi)

x = sp.Symbol('x')
y = sp.Symbol('y')

#Volume of torus
R, r, phi, theta = symbols('R r phi theta')

attributes1 = (r, 0, r)
attributes2 = (phi, 0, 2*pi)
attributes3 = (theta, 0, 2*pi)

#f variable value below was from the jacobian matrix calculation
#of the coordinate system
f = r*(R + cos(phi))
I1 = integrate(f, attributes2)
I2 = integrate(I1, attributes3)
I3 = integrate(I2, attributes1)

"""###Displaying the Toroidal shape and its volume formula"""

# Display the shape
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlim3d(-10, 10)
ax.set_ylim3d(-10, 10)
ax.set_zlim3d(-10, 10)
ax.plot_surface(X, Y, Z, color = 'c', edgecolors='w', rstride = 1, cstride = 1)
plt.show()

print('\n  The formula for volume of the torus: ')
display(I3)

"""###Jacobian Matrix Calculation"""

#toroidal coordinate system
R, r, phi, theta = symbols('R r phi theta', real=True)
X = (R + r * cos(theta)) * cos(phi)
Y = (R + r * cos(theta)) * sin(phi)
Z = r*sin(theta)

#Jacobian matrix
J = Matrix([
    [diff(X, r),diff(X, theta),diff(X,phi)],
    [diff(Y, r),diff(Y, theta),diff(Y,phi)],
    [diff(Z, r),diff(Z, theta),diff(Z,phi)]
])

display('A is: ', J)
display('Det(A) = ', J.det())
