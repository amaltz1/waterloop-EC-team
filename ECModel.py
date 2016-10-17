import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

b=0.348
a=0.0541
t=0.0079502
s=36.9e6
m=1.25e-6
y0=[]
y1=[]
y2=[]
lm = 0.3556
hm = 0.0254
uo = 4*np.pi*10e-7

# evenly sampled time at 200ms intervals
x0 = np.arange(1., 200., 1)
x1 = np.arange(0.1, 1, 0.1)
x2 = np.arange(1, 200, 1)
vp=2/(s*m*t)

def BrakingForce(v):
    if (v > 2/(s*m*t)):
        return (1/v)*b**2*a*t*s*(1.75/2)
    else:
        return (v)*b**2*a*t*s*(1.75/2)
        
def DragForce(v):
    return 283*vp*v/(v**2 + vp**2)

def BrakingForce2(v): 
    return BrakingForce(vp)*(v/vp)/(1+ (v/vp)**2)

def ForceBetweenMagnetsMax():
    return b**2*lm*hm*(1.75)/(2*uo)

def ForceBetweenMagnets(x):
    return (b**2*(lm*hm)**2*(1.75)*((lm)**2 + hm**2)/(np.pi*uo*lm**2))*(1/((2*x+t)**2)
    + 1/(((2*x+t) + 2*lm)**2) - 2/(((2*x+t)+ lm)**2))

def KineticEnergy(v):
    return 0.5*m*v**2

def BrakeTime(v):
    return 2*KineticEnergy(v)/(BrakingForce2(v)*v)

for i in range(1,200):
    y0.append(BrakingForce2(i))
    
for i in range(1,10):
    y1.append(ForceBetweenMagnets(i*0.1))
    
for i in range(1,200):
    y2.append(BrakeTime(i))
    
plt.plot(x0,y0)
plt.title('Braking Force vs Velocity')
plt.ylabel('Braking Force (N) ')
plt.xlabel('Velocity (m/s) ')
plt.show()

print 'Critical point veloicty: ' + str(vp) + ' m/s'

plt.plot(x1,y1)
plt.title('Attraction Force vs Seperation')
plt.ylabel('Force (N) ')
plt.xlabel('Distance from Rail (mm)')
plt.show()

print 'Max Magnet Force: ' + str(ForceBetweenMagnetsMax()) + ' N'

plt.plot(x2/y2,y2)
plt.title('Brake Time vs Acceleration')
plt.ylabel('Brake Time (s) ')
plt.xlabel('Acceleration (m/s^2)')
plt.show()

for i in range(1,11):
    print 'Brake time at : ' + str(i) +' m/s   ' + str(BrakeTime(i)) + ' s'