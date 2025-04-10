import numpy as np
import matplotlib.pyplot as plt

#constants and parameters

g = 9.81 #m/s
theta = 290 #K
dtheta = 0.005 #K/m
z_0 = 100 #m
w_0 = 0 
T_tot = 2000 #seconds

N = np.sqrt((g / theta) * dtheta)

def leapfroggy(delta_t):
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

    zp[1] = zp[0] + delta_t * w[0]
    w[1] = w[0] + (delta_t * -N**2 * zp[0])

    for t in range(1, nt): #an idea of sorts
        zp[t + 1] = zp[t - 1] + 2 * delta_t * w[t]  
        w[t + 1] = w[t - 1] + 2 * (delta_t * -N**2 * zp[t])
        z_exact[t + 1] = z_0 * np.cos(N * time[t + 1])
        errors[t + 1] = abs(z_exact[t + 1] - zp[t + 1])
        
    return time, zp, z_exact, w, errors

time, zp, z_exact, w, errors = leapfroggy(10)

print(zp)

plt.figure(1)
plt.plot(time, zp, label='numerical')
plt.xlabel('time (s)')
plt.ylabel('vertical position (m)')
plt.legend()
plt.title('position vs time (leapfrog, delta t =')
plt.grid(True)
plt.show()
# save