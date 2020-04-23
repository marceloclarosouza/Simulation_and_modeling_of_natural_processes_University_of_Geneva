["""  You need to provide the class with the minimum value xMin, maximum value xMax and the number of intervals N for integration. Then the integration process should be carried out accroding to the below information.

Suppose that S=∫xMinxMaxf(x)dx≈∑i=0N−1f(xi)ΔxS=\int_{xMin}^{xMax} f(x)dx\approx\sum_{i=0}^{N-1}f(x_i)\Delta xS=∫xMinxMax​f(x)dx≈∑i=0N−1​f(xi​)Δx (beware that the sum goes until N-1)

Δx=(xMax−xMin)/N\Delta x = (xMax-xMin)/NΔx=(xMax−xMin)/N

xi=xMin+iΔxx_i=xMin+i\Delta xxi​=xMin+iΔx.

The class is composed of three methods: _init_, integrate and show:

1. The method of _init_ should initialize the xMin, xMax, N and other related parameters .

2. The method of integrate should perform the integration process with the given parameters.

3. The method of show should print on the screen the result of integration. """]


import numpy as mp
import math as mt

class Integrator:
    def __init__(self, xMin, xMax, N):
        self.xMin = xMin
        self.xMax = xMax
        self.N = N
        self.Int = 0
        self.deltax = (self.xMax - self.xMin)/(self.N-1)
            
    def integrate(self):       
        for i in range(self.N-1):
            x = self.xMin + i*self.deltax
            fx = (x**2)*mt.exp(-x)*mt.sin(x)
            self.Int += fx*self.deltax
            
        
    def show(self):
        print(self.Int)
        print(round((self.Int), 5))

        

examp = Integrator(1,3,200000)
examp.integrate()
examp.show()