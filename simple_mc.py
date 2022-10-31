import random
import energy_lj_opt
import math

displacement = 0.1

def sample(n,l,beta,en_save,coord,reject):
	#choose a randome particle
	o = random.randint(0,n-1)
	rx = (random.random() - 0.5)*displacement
	ry = (random.random() - 0.5)*displacement
	rz = (random.random() - 0.5)*displacement
	#move the particle in a random displacement
	coord[o] = coord[o] + [rx,ry,rz]
	#calculate the energy of the new configuration
	en_new = energy_lj_opt.energy_cal(n,l,coord)
	if en_new - en_save > 0:
		if random.random() > math.exp(-beta*(en_new-en_save)):
			coord[o] = coord[o] - [rx,ry,rz]
			en_new = en_save
			reject += 1
	return en_new, reject 
