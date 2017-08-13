# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 15:50:58 2017

@author: Regan
"""
from PIL import Image
import numpy as np
np.set_printoptions(threshold=np.inf)

#interested in the behaviour of 0 under iteration
#do these numbers converge (<=2) or go to infinity?
#let C represent the complex plane

#Mandelbrot set M  = {c in C: lim as n goes to infinity c_n = 0^2+c_(n-1) <=2 for c_0=c C}

p_x = 500
p_y = 500

R = 25


M = np.zeros((p_x,p_y,3), dtype=np.uint8)

for x in range(p_x):
    for y in range(p_y): 
        #need to resize x and y so that image is centered at 0,0 and goes from -3,3
        re_const = ((x-(p_x/2))/p_x)*4.2-.5
        re = re_const
        im_const = ((y-(p_y/2))/p_y)*3.2
        im = im_const
        m=0
        iter_count = 0
        for r in range(R):
            re_cur = re
            re = re_cur*re_cur-im*im+re_const
            im = 2*re_cur*im+im_const
            
            m = re*re+im*im
            if m>4:
                break
        if m > 4:            
            c = (r/R)*255
            if c > 100:
                M.itemset((y,x, 0), c)
                M.itemset((y,x, 1), c)
            elif c > 50:
                M.itemset((y,x, 0), c)
                M.itemset((y,x, 1), c/2)

        else:
            M.itemset((y,x,0), 200)
            M.itemset((y,x,1), 25)
    
            
mandelbrot = Image.fromarray(M, 'RGB')
mandelbrot.save("mandelbrot.png")


