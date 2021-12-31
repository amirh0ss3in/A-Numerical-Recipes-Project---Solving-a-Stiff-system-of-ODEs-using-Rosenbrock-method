import numpy as np 
import matplotlib.pyplot as plt 
import time
import scipy.integrate as inte 

def o3(x,U):
    u , v = U
    du = v
    dv = 2*v/(1-x) - u/((1-x)**4)
    return np.array([du , dv])

def exact(x):
    y = np.sin(1/(1-x))
    return y


# y(0) , y'(0)
v0  , u0 = np.cos(1) , np.sin(1)
o3_0 = [u0 , v0]

start_time = time.clock()
method = 'DOP853'
s = inte.solve_ivp(fun=o3,t_span=(0,0.999),y0=o3_0,method=method,rtol=2.3e-14,atol=1e-20)
end_time = round(time.clock() - start_time, 3)
u , v  = s.y
x = s.t

exact_y = exact(x)

print('Method:', method)
print('Number of data points:', len(u))
print('Execution time:', end_time, 'seconds')

plt.plot(x,exact_y-u,'b')
# plt.plot(x,u,'.-b')

plt.yscale('symlog',linthresh=1e-15)
# plt.plot(x,exact_y,'r')
plt.show()
# x = np.linspace(0, 0.99,num=10000)

# plt.plot(x,o3(x))
# plt.show()

