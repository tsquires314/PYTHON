import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from random import random
import math
import seaborn as sns
import itertools as it
import ecdf as ecdf

testData = [3,4,6,7,8,9,2,3,6,5,3,2,4,6,7,8,9,6,4,2,1,3,4,5,7,8,6,7,8,9,9,8,7,6,6,7,8,9]


means = [np.mean(testData)]
trials = 1000
for i in range(trials):
	
	resample = np.random.choice(testData,len(testData))
	resampleMean = np.mean(resample)
	means.append(resampleMean)
print(means)	
x,y = ecdf.ecdf(means)
plt.plot(x,y,marker='.',linestyle='none')
plt.show()
