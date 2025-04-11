import numpy as np
import  matplotlib.pyplot as plt

#constants and parameters

g = 9.81 #m/s
theta = 290 #K
dtheta = 0.005 #K/m
z_0 = 100 #m
w_0 = 0 
T_tot = 2000 #seconds

N = np.sqrt((g / theta) * dtheta)

def euler_forward(delta_t):
    nt = int(T_tot / delta_t) #error here idk ill come back (int)

    #figure out arrays
    time = np.linspace(0, T_tot, nt + 1)
    zp = np.zeros(nt + 1)
    z_exact = np.zeros(nt + 1)
    w = np.zeros(nt + 1)
    errors = np.zeros(nt + 1)

    #initial conditions
    w[0] = w_0
    zp[0] = z_0
    z_exact[0] = z_0 * np.cos(N * time[0])
    errors[0] = abs(z_exact[0] - zp[0])

    for t in range(nt): #an idea of sorts
        zp[t + 1] = zp[t] + delta_t * w[t]  
        w[t + 1] = w[t] + (delta_t * -N**2 * zp[t])
        z_exact[t + 1] = z_0 * np.cos(N * time[t + 1])
        errors[t + 1] = abs(z_exact[t + 1] - zp[t + 1])
        
    return time, zp, z_exact, w, errors
# save

#need to change plots so both dt show on one graph

time_10, zp_10, z_exact_10, w_10, errors_10 = euler_forward(10)
time_1, zp_1, z_exact_1, w_1, errors_1 = euler_forward(1)

# FOR MY FIRST PART!!!

plt.figure(1)
plt.plot(time_10, zp_10, label='∆t = 10', color = 'slateblue')
plt.plot(time_1, zp_1, label='∆t = 1', color = 'indigo')
plt.xlabel('time (s)')
plt.ylabel('vertical position (m)')
plt.legend()
plt.title('position vs time (euler forward)')
plt.grid(True)
plt.show()

plt.figure(2)
plt.plot(time_10, zp_10, label='numerical', color = 'slateblue')
plt.plot(time_10, z_exact_10, label='exact', color = 'firebrick')
plt.xlabel('time (s)')
plt.ylabel('vertical position (m)')
plt.legend()
plt.title('position vs time (euler forward ∆t = 10)')
plt.grid(True)
plt.show()

plt.figure(3)
plt.plot(time_1, zp_1, label='numerical', color = 'indigo')
plt.plot(time_1, z_exact_1, label='exact', color = 'firebrick')
plt.xlabel('time (s)')
plt.ylabel('vertical position (m)')
plt.legend()
plt.title('position vs time (euler forward ∆t = 1)')
plt.grid(True)
plt.show()

# PART NUMBA TWOOOOOO

#everything everywhere all at once
plt.figure(4)
plt.plot(zp_10, w_10, label='∆t = 10', color = 'slateblue')
plt.plot(zp_1, w_1, label = '∆t = 1', color = 'indigo')
plt.xlabel('vertical position (m)')
plt.ylabel('vertical velocity (m/s)')
plt.legend()
plt.title('exact position vs time (euler forward)')
plt.grid(True)
plt.show()

#just t=10
plt.figure(5)
plt.plot(zp_10, w_10, label='∆t = 10', color = 'slateblue')
plt.xlabel('vertical position (m)')
plt.ylabel('vertical velocity (m/s)')
plt.legend()
plt.title('position (z) vs velocity (w) [euler forward ∆t = 10]')
plt.grid(True)
plt.show()

#just t=1
plt.figure(6)
plt.plot(zp_1, w_1, label = '∆t = 1', color = 'indigo')
plt.xlabel('vertical position (m)')
plt.ylabel('vertical velocity (m/s)')
plt.legend()
plt.title('position (z) vs velocity (w) [euler forward ∆t = 1]')
plt.grid(True)
plt.show()

#PTHREE

# my errors (sadddd)
plt.figure(3)
plt.plot(time_10, errors_10, label = '∆t = 10', color = 'slateblue')
plt.plot(time_1, errors_1, label = '∆t = 1', color = 'indigo')
plt.xlabel('time (s)')
plt.ylabel('error')
plt.xscale('log')
plt.yscale('log')
plt.title('euler forward error')
plt.grid(True)
plt.show()