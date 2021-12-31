import numpy as np 
import matplotlib.pyplot as plt 
import os

def main():
    path = os.path.dirname(os.path.abspath(__file__))+'\data_ode.txt'
    ode_results = np.loadtxt(path,dtype=np.float64)

    # x
    x = ode_results[:,0]

    # u(x)
    u = ode_results[:,1]

    # v(x)
    v = ode_results[:,2]

    # Difference of u(x) and f(x) ( Difference of numerical solution and exact solution; computed in the origianl c++ program )
    difference = ode_results[:,3]

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