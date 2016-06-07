import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def impliciteuler(F=None, inival=None, interval=[0, 1], Nts=100,
                  dFdx=None, dFdxdot=None):
    """
    Parameters:
    ---
    F: callable
        the problem in the form F(t,x,x')
    """
    t0, te = interval[0], interval[1]
    h = 1./Nts*(te-t0)
    N = inival.size

    sollist = [inival.reshape((1, N))]
    tlist = [t0]

    xk = inival
    for k in range(1, Nts+1):  # python starts counting with zero...
        tkk = t0 + k*h

        def impeuler_increment(xkkn):
            return F(tkk, xkkn, 1./h*(xkkn-xk)).flatten()

        xkk = fsolve(func=impeuler_increment, x0=xk)
        sollist.append(xkk.reshape((1, N)))
        tlist.append(tkk)
        xk = xkk

    sol = np.vstack(sollist)
    plt.plot(tlist, sol)

    return sol


def E(t):
    return np.array([[-t, t*t], [-1, t]])


def A(t):
    return np.array([[-1, 0], [0, -1]])


def f(t):
    return np.array([0, 0])


def F(t, x, xdot):
    return E(t).dot(xdot) - A(t).dot(x) - f(t)

inival = np.array([0, 1])
interval = [0, 10]

sol = impliciteuler(F=F, inival=inival, interval=interval, Nts=1000)
