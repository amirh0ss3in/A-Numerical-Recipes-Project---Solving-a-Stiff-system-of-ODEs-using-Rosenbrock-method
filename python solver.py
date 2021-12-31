import numpy as np 
import matplotlib.pyplot as plt 
import time
import scipy.integrate as inte 

def system_of_ode(x,U):
    u , v = U
    du = v
    dv = 2*v/(1-x) - u/((1-x)**4)
    return np.array([du , dv])

# f(x)
def exact(x):
    y = np.sin(1/(1-x))
    return y

def main():

    # u(0) , v(0)
    u0 , v0 = np.sin(1) , np.cos(1)
    system_of_ode_0 = [u0 , v0]

    # LSODA method is an implicit method. Note that although it is a faster method, advanced explicit methods such as 'DOP853' are generally more precise.
    method = 'LSODA'

    start_time = time.clock()
    s = inte.solve_ivp(fun=system_of_ode,t_span=(0,0.99),y0=system_of_ode_0,method=method,rtol=2.3e-14,atol=1e-20)
    end_time = round(time.clock() - start_time, 3)
    
    # u(x) , v(x)
    u , v  = s.y
    x = s.t
    exact_f = exact(x)

    print('Method:', method)
    print('Number of data points:', len(u))
    print('Execution time:', end_time, 'seconds')

    # Difference of u(x) and f(x) ( Difference of numerical solution and exact solution; computed in the origianl c++ program )
    difference = exact_f-u

    # Plot of u(x)
    plt.plot(x, u,'b')
    plt.xlabel(r'$x$',fontsize=16)
    plt.ylabel(r'$u(x)$',fontsize=16)
    plt.tight_layout()
    plt.show()

    # Plot of v(x)
    plt.plot(x, v,'g')
    plt.xlabel(r'$x$',fontsize=16)
    plt.ylabel(r'$v(x)$',fontsize=16)
    plt.tight_layout()
    plt.show()

    # Plot of difference, using symmetric log
    plt.plot(x, difference,'.-r')
    plt.yscale('symlog',linthresh=1e-15)
    plt.xlabel(r'$x$',fontsize=16)
    plt.ylabel(r'$difference$',fontsize=16)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()