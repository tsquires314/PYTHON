import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
from random import randint
from random import random
import math
import seaborn as sns
import itertools as it

board = pd.DataFrame(columns = [0,1,2,3,4])
board[0] = ['','B','','W','']
board[1] = ['','','','','']
board[2] = ['B','','','','']
board[3] = ['','','','','W']
board[4] = ['','','','','']


def LegalMove(board,positionStart,positionEnd):
	if positionStart[0] == positionEnd[0]:
		print(str(positionStart) + ' to ' +  str(positionEnd) + ' is a legal horizontal move')
		if positionStart[1] < positionEnd[1]:
			path  = [(positionStart[0],j) for j in range(positionStart[1],positionEnd[1]+1)]
		else:	
			path  = [(positionStart[0],j) for j in range(positionEnd[1],positionStart[1]+1)]
		return (path,True) 
	
	elif positionStart[1] == positionEnd[1]:
		print(str(positionStart) + ' to ' + str(positionEnd) + ' is a legal vertical move')
		if positionStart[0] < positionEnd[0]:
			path  = [(j,positionStart[1]) for j in range(positionStart[0],positionEnd[0]+1)]
		else:	
			path  = [(j,positionStart[1]) for j in range(positionEnd[0],positionStart[0]+1)]
		return (path,True)
	
	elif abs((positionStart[0] - positionEnd[0])) == abs((positionStart[1] - positionEnd[1])):
		print(str(positionStart) + ' to ' + str(positionEnd) + ' is a legal diagonal move')
		if positionStart[0] < positionEnd[0]:
			if positionStart[1] < positionEnd[1]:
				path = [(positionStart[0]+j,positionStart[1]+j) for j in range(positionEnd[0]-positionStart[0]+1)]	
			else:	
				path = [(positionStart[0]+j,positionStart[1]-j) for j in range(positionEnd[0]-positionStart[0]+1)]	
		else:	
			if positionStart[1] > positionEnd[1]:
				path = [(positionStart[0]-j,positionStart[1]-j) for j in range(positionStart[0]-positionEnd[0]+1)]
			else:
				path = [(positionStart[0]-j,positionStart[1]+j) for j in range(positionStart[0]-positionEnd[0]+1)]
		return (path,True)
	
	else:
		print(str(positionStart) + ' to ' + str(positionEnd) + ' is not a legal move')
		return ([],False) 	


#def CanAttack(board,position1,position2):




def Dist(positionStart,positionEnd):
	return np.sqrt((positionStart[0] - positionEnd[0])**2 + (positionStart[1] - positionEnd[1])**2)





positions = [i for i in it.product([0,1,2,3,4],[0,1,2,3,4])]
teamPositionsIterrator = it.combinations(positions,5)




teamPositions = [i for i in teamPositionsIterrator]


def moves(setup):
	visited = []
	for p in setup:
		visited += [(x-p[0]+p[1],x) for x in range(5) if x-p[0]+p[1] in range(5)] + [(-x+p[0]+p[1],x) for x in range(5) if -x+p[0]+p[1] in range(5)] + [(y,p[0]) for y in range(5)] + [(p[1],x) for x in range(5)]
	print(set(visited))	 
	return(len(set(visited)))

coverSize = [moves(teamPositions[i]) for i in range(len(teamPositions))]
solutions = [True if coverSize[i] == 22 else False for i in range(len(teamPositions))]
print(solutions.index(True))
print(coverSize[solutions.index(True)])
print(teamPositions[solutions.index(True)])
print(moves(teamPositions[solutions.index(True)]))
print(sum(solutions))





