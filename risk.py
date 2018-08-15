import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
from random import randint
from random import random
import math
import seaborn as sns

np.random.seed(60)


# offenisve and defensive rolls, always sorted in ascending order

offensiveRoll = np.sort(np.floor(6*np.random.random(size = 3)+1))
defensiveRoll = np.sort(np.floor(6*np.random.random(size = 2)+1))

# number of deaths for offensive and defensive players

deathTally = np.array([0,0])

# roll function. input death tally, roll, and update death tally

def roll(offUnits, defUnits, offRollNum = 3, defRollNum = 2):


	
	offRoll = np.sort(np.floor(6*np.random.random(size = offRollNum)+1))
	defRoll = np.sort(np.floor(6*np.random.random(size = defRollNum)+1))
	offRemainingDie = offRollNum 
	defRemainingDie = defRollNum
	print('roll is ' + str(offRoll) + str(defRoll))
	i =0 
	while (offRemainingDie > 0) & (defRemainingDie > 0):
	
		if offRoll[offRemainingDie-1] > defRoll[defRemainingDie-1]:
			deathTally[1] += 1
			defUnits -= 1
			offRemainingDie -= 1
			defRemainingDie -= 1
			"""print('death tally is ' + str(deathTally))
			print('remaining die are ' + str([offRemainingDie,defRemainingDie]))
			print('remaining units are ' + str([offUnits,defUnits]))"""
		else:
			deathTally[0] += 1	
			offUnits -= 1
			defRemainingDie -= 1
			offRemainingDie -= 1
			"""print('death tally is ' + str(deathTally))
			print('remaining die are ' + str([offRemainingDie,defRemainingDie]))
			print('remaining units are ' + str([offUnits,defUnits]))"""
	return [offUnits,defUnits]
	




# define the map state and structure
ColoursInGame = ['Red','Blue']

mapState = pd.DataFrame(columns = ['Controlled By','Number of Armies',],index = ['territory1','territory2','territory3'])
mapStructure = pd.DataFrame(columns = ['territory1','territory2','territory3'],index = ['territory1','territory2','territory3'])

mapState['Controlled By'] = ['Red','Blue','Blue']
mapState['Number of Armies'] = [10,6,6]

# dictionary defining the map structure, territory:list of neighbours

mapDict = {'territory1':[1,1,1],'territory2':[1,1,0],'territory3':[1,0,1]}

# defines the map in a data frame. Warning, for visualization purposes only...use dictionary in code

mapStructure['territory1'] = [1,1,1]
mapStructure['territory2'] = [1,1,0]
mapStructure['territory3'] = [1,0,1]



# battle functions. input tuples, country attacking and country being attacked.
# roll strategy to go in the while conditional



def Battle(offensive,defensive,attackTerr,defendTerr):
	
	offUnits = mapState['Number of Armies'][attackTerr] 
	defUnits = mapState['Number of Armies'][defendTerr]


	
	while((offUnits > 1) & (defUnits >0)):	
		offRollNum = min(offUnits -1, 3)
		defRollNum = min(defUnits,2)
		offUnits,defUnits = roll(offUnits,defUnits,offRollNum,defRollNum)	
	
	# move units step

	if defUnits > 0:
		mapState.loc[mapState.index == attackTerr, 'Number of Armies'] = offUnits
		mapState.loc[mapState.index == defendTerr, 'Number of Armies'] = defUnits
		print('No units moved')
	else:
		mapState.loc[mapState.index == attackTerr, 'Number of Armies'] = min(2,offUnits-1)
		mapState.loc[mapState.index == defendTerr, 'Number of Armies'] = max(offUnits-2, 1)
		mapState.loc[mapState.index == defendTerr, 'Controlled By'] = offensive
		print(str(max(offUnits-2, 1)) + ' units moved from ' + attackTerr + ' to ' + defendTerr)

	print(mapState)	
	return mapState

#print(Battle('Red','Blue','territory1','territory2'))



# a dictionary defining the neighbours

neighbours = {'territory1':['territory2','territory3'], 'territory2':['territory1'], 'territory3':['territory1']}

# returns a list of potential territories to attack, and from which controlled territory, should include a ranking of potential attacks

def PotentialAttacks(color):
	results = []
	for index,info in mapState.iterrows():
		if info[0] == color:
			currentNeighbours = neighbours[index]	
			hostileBorders =[(index,neighbour) for neighbour in currentNeighbours if mapState.loc[neighbour][0] != color]
			results=results + hostileBorders
	return results				

# a color chooses whether or not to attack a hostile neighbour in the list of potential attacks
def Turn(color):
	print(color + ' turn:')

	for attackTerr,defendTerr in PotentialAttacks(color):
		print(PotentialAttacks(color))
		if color == mapState['Controlled By'][defendTerr]:
					break
		if mapState['Number of Armies'][attackTerr] > 1:
			if (mapState['Number of Armies'][attackTerr] >= mapState['Number of Armies'][defendTerr]):
						print(color + ' attacks ' + mapState['Controlled By'][defendTerr] + ' from ' + attackTerr + ' to ' + defendTerr)
						Battle(color, mapState['Controlled By'][defendTerr], attackTerr, defendTerr)								
	EliminationCheck()		
def EliminationCheck():
	for color in ColoursInGame:
		if sum(mapState.loc[mapState['Controlled By'] == color,'Number of Armies']) == 0:
			print(color + ' has been eliminated')
			ColoursInGame.remove(color)
		if len(ColoursInGame) == 1:
			print('Game over: Winner is ' + ColoursInGame[0])		
			return True
numberOfRounds = 3
	
for i in range(numberOfRounds):
	if EliminationCheck() == True:
		break
	Turn('Red')
	if EliminationCheck() == True:
		break
	Turn('Blue')


