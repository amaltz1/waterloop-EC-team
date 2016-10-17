'''

Objective: return the new distance between the rail such that the braking de-acceleration
does not exceed 2.4G. Note that before the inflection point, friction braking will be used
The braking force is based on the speed of the pod and the surface current density of
on the rail, which is based on the distance between the magnet and the rail

maximum separation distance 12-15mm
minimum separation distance 6mm

equation sources:

https://www.supermagnete.de/eng/faq/How-do-you-calculate-the-magnetic-flux-density#block-magnet b field due to block magnet

http://www.thompsonrd.com/OSEE-brakes.pdf brakign force
'''

from math import *

podMass = 250 #mass of pod is 250 kg assuming there are no passengers, there is a scale that will measure this
mu = 1.25e-6             #mag perm of aluminum
sigma = 36.9e6     #electrical conductivity of aluminum
t = 0.0079502          #thickness of rails 
vp = 2/(mu*sigma*T) #"drag peak" velocity (before drag peak, friction braking takes over, after )
Br = 1.47 #remanence of N52 grade neodymium magnets (in teslas). This is effectively the point magnetic field of the magnet
L = 0.0254 #dimensions of the block magnets (1x1x1 inch cube or 0.0254 m^3 cube)


def Bfield_cube(z):
	#returns the b-field at a point z meters away from the 1 cubic inch magnets
	B = (Br/pi)*(atan(L**2/(2*z*sqrt(4*z**2+2*L**2)))-atan(L**2/(2*(L+z)*sqrt(4*(L+z)**2+2*L**2))))
	return(B)

def Braking_force(v,z):
	B = Bfield_cube(z) #B varies with separation distance
	if (v > 2/(sigma*mu*t)):
        return (1/v)*B**2*a*t*sigma*(1.75/2)

def new_distance(v,z):
	maxforce = podMass * 9.812 * 2.4
	return()