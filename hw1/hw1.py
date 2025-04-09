
# organize and declare all variables

def error(z_exact, z_approx):
    err = abs(z_exact - z_approx)
    return err

# initialize all constants and parameters

g = 9.81 #m/s
theta = 290 #K
dtheta = 5 #K/km
z_0 = 100 #m
w_0 = #idk lmao


# set up initial conditions. w = w0, zp = z0

w = w0
zp = z_0
t_0 = 0
# figure out arrays and files
# main loop (marching in time) 

# loop : 1, nt 
# t_total 
T_tot = 2000 #seconds
delta_t = 10

nt = T_tot / delta_t


for t in range(nt): #this is not right but i have my idea. ill think abt iterations later
    t = t_0 + delta_t #current time
# advance solution in time 
    # each t (recursive eq)
# update variables
    t_0 = t
# calculate exact soultion
    z_exact =
    
# calculate error 
    err_t = error(z_exact, z_approx)
# save