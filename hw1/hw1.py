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

def lolforgot(delta_t):
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

#I BROKE THIS!!!!!!!!!!!!!!!!!!!!!!!

delta_t_list = [10, 1]

for t in delta_t_list:
    time, zp, z_exact, w, errors = lolforgot(t)

    plt.figure()
    plt.plot(time, zp, label='numerical')
    plt.xlabel('time (s)')
    plt.ylabel('vertical position (m)')
    plt.legend()
    plt.title('position vs time (euler forward, delta t = {}', format(t))
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.plot(time, z_exact, '--', label='analytical')
    plt.xlabel('time (s)')
    plt.ylabel('vertical position (m)')
    plt.legend()
    plt.title('position vs time (euler forward, delta t = {}', format(t))
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.plot(time, errors)
    plt.xlabel('time (s)')
    plt.ylabel('error')
    #plt.xscale('log')
    plt.yscale('log')
    plt.title('euler forward error (delta t = {}', format(t))
    plt.grid(True)
    plt.show()