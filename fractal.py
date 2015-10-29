# -*- coding: utf-8 -*-

# this module contains both its own implementation of the Fractal class as well
# as a wrapper class of the C++ Fractal class.

import ctypes
import matplotlib.pyplot as plt
import time

MAX_ITERATIONS = 150
EPSILON        = 1.0e-8

class PyFractal(object):
   def __init__(self, xRange, yRange, granularity):
      self.xmin, self.xmax = xRange
      self.ymin, self.ymax = yRange
      self.granularity = granularity
      
   def compute(self):
      done = False
      x = self.xmin
      y = self.ymax
      xidx = 0
      points = []
      points.append([])
    
      while not done:
         c = complex(x, y)
         p = complex(0.0, 0.0)
    
         iteration = 1
         while iteration < MAX_ITERATIONS:
            if abs(p) >= 2.0:
               break
            p = self.mandelbrot(p, c)
            iteration += 1
    
         if iteration == MAX_ITERATIONS:
            points[xidx].append(-1)
         else:
            points[xidx].append(iteration)
    
         x += self.granularity
         if x - self.xmax > EPSILON:
            x = self.xmin
            y -= self.granularity
            xidx += 1
            if y - self.ymin < EPSILON:
               done = True
            else:
               points.append([])
               
      return points

   def mandelbrot(self, point, constant):
      return point * point + constant;
      
if __name__ == '__main__':
   print '\n\n'
   print 'Processing PyFractal...'
   start = time.time()
   f2 = PyFractal([-2.5, 1.5], [-1.5, 1.5], 0.0005)
   m2 = f2.compute()
   end = time.time()
   print 'PyFractal time elapsed: ', end - start
   plt.imshow(m2)
   plt.show()
     