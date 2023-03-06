from random import random,uniform
from minima import sphere,minimize


if __name__=="__main__":
    x0y0=[5,5]
    bounds=[(-10,10),(-10,10)]
    minimize(sphere, x0y0, bounds, pnos=15, maxiter=30, verbose=True)
