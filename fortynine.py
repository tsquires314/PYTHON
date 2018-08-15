import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
from random import randint
from random import random
import math
import seaborn as sns


def digits(A): 
	# returns the digits of a 5 digit number
	return [int(np.floor(A/(10**i))) % 10 for i in range(5)]

def possibleDigits(A):
	# checks that digits 2 and 4 are the same and that the other digits are distinct
	return (digits(A)[1] == digits(A)[3]) & (len(digits(A)) == len(set(digits(A))) + 1)



# the list of all possible 5 digit numbers of the correct form and all 6 digit numbers that are 7 times this list and ending in 9

possibleSevens = [i for i in range(10000, 100000) if possibleDigits(i)]

results = [7*i for i in possibleSevens if (7*i > 100000) & (7*i % 10 == 9)]


def resultsDigits(A):
	# gives digits 2 through 6 of a 6 digit number (we do not need the initial 9)
	return [int(np.floor(A/(10**i))) % 10 for i in range(1,6)]

def intersectionEmpty(I,J):
	# checks if two lists have an empty intersection
	return sum([True if (I[i] in J) else False for i in range(len(I))]) == 0



solutions1 = [results[i]/7 for i in range(len(results)) if intersectionEmpty(digits(results[i]/7),resultsDigits(results[i]))]

def solutionsDigits(A):
	#returns the digits of a 6 digit number
	return [int(np.floor(A/(10**i))) % 10 for i in range(0,6)]

# filters out the members of solutions1 with repeated digits

solutions2 = [i for i in solutions1 if len(solutionsDigits(7*i)) == len(set(solutionsDigits(7*i)))]


print(solutions2)
