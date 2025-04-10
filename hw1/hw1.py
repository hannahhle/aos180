import numpy as np
import  matplotlib.pyplot as plt



# organize and declare all variables

# initialize all constants and parameters

g = 9.81 #m/s
theta = 290 #K
dtheta = 0.005 #K/m
z_0 = 100 #m
w_0 = 0 

N = np.sqrt((g / theta) * dtheta)

# loop : 1, nt 
# t_total 
T_tot = 2000 #seconds
delta_t = 10

nt = T_tot / delta_t

time = np.linspace(0, T_tot, nt + 1)

# figure out arrays and files
zp = np.zeros(nt + 1)
z_exact = np.zeros(nt + 1)
w = np.zeros(nt + 1)
errors = np.zeros(nt + 1)

w[0] = w_0
zp[0] = z_0
z_exact[0] = z_0 * np.cos(N * time[0])
errors[0] = abs(z_exact[0] - zp[0])

for t in range(nt): #this is not right but i have my idea. ill think abt iterations later
    t = t_0 + delta_t #current time
# advance solution in time 
    # each t (recursive eq)
# update variables
    t_0 = t
# calculate exact soultion
    z_exact
    
# calculate error 
    err_t = 
# save