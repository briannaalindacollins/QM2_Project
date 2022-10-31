import math

def vir(number_of_particles,vol,beta,rho,coord,L):
	rc = 2.5
	vir = 0
	force = 0
	#print ('worked')
	for i in range(number_of_particles-1):
		stacked = coord[i]
		xi = stacked[0]
		yi = stacked[1]
		zi = stacked[2]
		for j in range(1, number_of_particles):
			stack2 = coord[j]
			xj = stack2[0]
			yj = stack2[1]
			zj = stack2[2]
			dx = xi-xj - (round(xi-xj))*rc
			dy = yi-yj - (round(yi-yj))*rc
			dz = zi-zj - (round(zi-zj))*rc
			r2 = ((dx*dx)+(dy*dy)+(dz*dz))**(1/2.0)
			#print (r2)	
			if r2 < rc and r2 != 0:
				
				#r2 = float(r2)
				fr2 = 1/r2 
				fr6 = fr2**3
				vir = float(vir)
				vir = vir - (8.0*fr6*(1.-(2*fr6)))
				force = force + (vir/r2)
	
	p = (float(rho)/beta)+(vir/float(vol))
	print (p, 'is the pressure')
	print (vir, 'is the virial')
	print (force, 'is the force')

	
