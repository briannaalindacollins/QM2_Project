#Simple Lennard-Jones simulation
import math
import random
import initialize_coordinates
import energy_lj_opt
import pickle
import os 
import simple_mc
import time
import vir
########################################
### Time for profiling #################
########################################

start = time.time()

########################################
### INPUT VARIABLES IN REDUCED UNITS ###
########################################
rho = 0.4
box_length = 6
temp = 0.9
steps = 1000

###########################################################
# Calculate Beta in reduced units and number of particles #
###########################################################
beta = 1.0 / temp
vol = box_length**3.0
number_of_particles = int(round(vol*rho))

#########################################################################
### Check to see if coordinate files exists, if it does read the file ###
### if it does not, call initialized coordinates ########################
filename = "coordinates.xyz"
if os.path.isfile(filename):
	with open (filename, 'rb') as fp:
		coord = pickle.load(fp)
else:
	coord = initialize_coordinates.init_coord(number_of_particles,box_length)
#########################################################################

energy = energy_lj_opt.energy_cal(number_of_particles,box_length,coord)
vir = vir.vir(number_of_particles,vol,beta,rho,coord,box_length)
#print ('worked') 
print('init energy',energy)

reject = 0 
for i in range(steps):
	energy_new, reject = simple_mc.sample(number_of_particles,box_length,beta,energy,coord,reject)
	if (i%1 == 0):
		print('Step', i, 'Energy=', energy_new, 'reject %', 100.*(float(reject)/(i+1)))
		energy = energy_new

#################################
# Write the current coordinates #
#################################
with open(filename, 'wb') as fp:
    pickle.dump(coord, fp)

#################################
### Print time for Profiling ####
#################################

duration = time.time() - start
print('duration', duration)

#from mpl_toolkits.mplot3d import Axes3D
#import matplotlib.pyplot as plt
#
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(coord[:,0],coord[:,1],coord[:,2], c='r', marker='o')
#
#ax.set_xlim(0,box_length)
#ax.set_ylim(0,box_length)
#ax.set_zlim(0,box_length)
#
#ax.set_xlabel('X Label')
#ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')
#
#plt.show()

