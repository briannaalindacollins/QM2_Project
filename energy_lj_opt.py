import math
import numpy as np
import numba

# Cut off distance between LJ particles
rc = 2.5
rc2 = rc**2.0
rc6 = rc2**3.0
rc12 = rc6**2.0

#Energy between LJ particles at the cut off distance
ecut = 4.*(1./rc12 - 1./rc6)

# Subroutine takes the number of particles, boxlength, and coordinates of all particles
# and  returns the energy
def energy_cal(n, l, coord):
	rij = [0.] * 3
	epot = energy_cal_code(n, l, coord, rij, ecut, rc2)
	return epot


@numba.jit
def energy_cal_code(n,l,coord,rij,ecut,rc2):
    epot = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            for d in range(3):
                rij[d] = coord[i][d] - coord[j][d]
                rij[d] -= round(rij[d] / l) * l
            r2 = rij[0] ** 2 + rij[1] ** 2 + rij[2] ** 2
            #print('test2',r2,epot)
            if(r2 < rc2):
                epot += 4. * (1. / r2 ** 6 - 1. / r2 ** 3) - ecut
            #print('test',i,j,n,epot)
    return epot
