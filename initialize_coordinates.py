import math
import numpy as np

#This subroutine initializes particles on a square lattice

def init_coord(n,l):
	n_3 = round(n**(1./3))
	ii = int(n_3) 
	iii = int(n - n_3**(3))
	if iii < 0:
	 iii = 0
	 p_box_x = l/n_3
	else:
         n1 = math.ceil((iii**(1./2))/n_3)
         p_box_x = l/(n_3+n1)
	p_box = l/n_3
	x = []
	y = []
	z = []
	jj = 0
	for i in range(ii+iii):
	 for j in range(ii):
	  for k in range(ii):
	   jj = jj + 1
	   if jj > n:
	    break
	   x.append(p_box_x*i+p_box_x/2.)	
	   y.append(p_box*j+p_box/2.)
	   z.append(p_box*k+p_box/2.)
	return np.column_stack((x,y,z))



