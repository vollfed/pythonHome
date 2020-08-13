#-----------------------------------------------------------------------
# ifs.py
#-----------------------------------------------------------------------

import sys 
import os
sys.path.append(os.path.abspath("/Users/vlafed/Desktop/work/learning/python/stdlib-python"))

import stdarray
import stdrandom
import stddraw
import math

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Read a
# 1-by-m vector (probabilities) and two m-by-3 matrices (coefficients
# for updating x and y, respectively) from standard input. Plot the
# results as a set of n points to standard draw.

def main():
    n = int(sys.argv[1])
    dist = stdarray.readFloat1D()
    cx = stdarray.readFloat2D()
    cy = stdarray.readFloat2D()
    x = 0.0
    y = 0.0

    #stddraw.setPenRadius(0.1)
    #stddraw.setPenColor(stddraw.ORANGE)
    #stddraw.point(0, 0)

    #stddraw.setPenRadius(0.1)
    #stddraw.setPenColor(stddraw.GREEN)
    #stddraw.point(1, 1)

    #stddraw.setPenRadius(0.1)
    #stddraw.setPenColor(stddraw.BLUE)
    #stddraw.point(0.5, 0.5)

    #stddraw.setPenColor(stddraw.BLACK)
    #stddraw.point(0.5, 0.288)

    stddraw.setPenRadius(0.003)
    #stddraw.setPenColor(stddraw.RED)
    
    for i in range(n):
        r = stdrandom.discrete(dist)
        x0 = cx[r][0]*x + cx[r][1]*y + cx[r][2]
        y0 = cy[r][0]*x + cy[r][1]*y + cy[r][2]
        x = x0
        y = y0
        #cos -sin  x
        #sin cos   y
        angle = (2* 3.14)/ 360  * i

        dvd = 4

        if(i%dvd == 0):
            stddraw.setPenColor(stddraw.BLUE)
            angle = 0

        if(i%dvd == 1):
            stddraw.setPenColor(stddraw.RED)
            angle = 22.5

        if(i%dvd == 2):
            stddraw.setPenColor(stddraw.GREEN)
            angle = 45

        if(i%4 == 3):
            stddraw.setPenColor(stddraw.ORANGE)
            angle = -22.5
        
        x_r = x - 0.5
        y_r = y - 0.288
        
        x_1 =  x_r * math.cos(angle) - y_r * math.sin(angle)
        y_1 =  x_r * math.sin(angle) + y_r * math.cos(angle)
        
        stddraw.point(x_1*0.5+0.5, y_1*0.5 + 0.5)
        #stddraw.point(x-0.5, y-0.288)

        #print(str(x_1) + "_" + str(y_1))
    
    stddraw.show()


    
if __name__ == '__main__':
    main()