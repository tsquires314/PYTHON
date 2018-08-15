import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from random import random
import math
import seaborn as sns
import itertools as it

def choose(n,k):
	return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, 1+n) / n

    return x, y

data = 100*(np.random.random(size = 1000))

test = np.random.normal(0,1, size=10)

def Pois(k,r):
	return np.exp(-1*r)*(r**k/math.factorial(k))

def Binom(k,n,p):
	return choose(n,k)*(p**k)*((1-p)**(n-k))


total = 0
for k in range(20):
	total += Pois(k,6)


sampleP = np.random.poisson(6,100000)
sampleP.sort()




sampleB = np.random.binomial(60,0.1,100000)
sampleB.sort()

 


