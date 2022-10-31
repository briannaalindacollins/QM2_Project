import math

# Cut off distance between LJ particles
rc = 2.5
rc2 = rc**2.0
rc6 = rc2**3.0
rc12 = rc6**2.0

#Energy between LJ particles at the cut off distance
ecut = 4.*(1./rc12 - 1./rc6)

# Subroutine takes the number of particles, boxlength, and coordinates of all particles
# and  returns the energy
def energy_cal(n,l,coord):
	en = 0.0
	# Loop over particles 1 to N-1
	for i in range(0,n-1):
		# x1 contains [x, y, z] coordinates for particle i
		x1 = coord[i]
		# Loop over particles i+1 to N
		for j in range(i+1,n):
			# x2 contains [x, y, z] coordinates for particle j
			x2 = coord[j]
			dist = x1 - x2
			# Subtract off box length to get the nearest perodic image.
			dist[0] = dist[0] - round(dist[0]/l)*l
			dist[1] = dist[1] - round(dist[1]/l)*l
			dist[2] = dist[2] - round(dist[2]/l)*l
			dist2 = dist**2.
			r2 = sum(dist2)
			# Calculate LJ energy and subtract off cut off energy. 
			if r2 < rc2:
				r6 = r2**3.
				r12 = r6**2.
				en = en + 4.*(1./r12 - 1./r6) - ecut
	return en
