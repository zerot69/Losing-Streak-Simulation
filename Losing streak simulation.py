#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Title: Martingale’s Strategy in Gambling: Does “Double the bet” really work?
# Author: Vo-Hoang-Tuan Ngo (26839)
# Rhein-Waal University of Applied Sciences
# Date 08.01.2021

import random
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Function to run the simulation 'gameTotal' times
def simulation(gameTotal):
    
    # Initialize variables    
    lostStreak = 0
    sumLost = 0
    sumWon = 0
    array = [0 for x in range(gameTotal+1)]
    highestLostStreak = 0

    for game in range (0,gameTotal):
        x = random.randint(0,1)
        # if the randomized number is 0 => lose    
        if (x == 0):
            lostStreak += 1
            sumLost += 1
        else:
            sumWon += 1
            array[lostStreak] += 1
            if (highestLostStreak < lostStreak):
                highestLostStreak = lostStreak
            lostStreak = 0
            
        # Check losing streak of the last game
        if ((game == gameTotal-1) and (x == 0)):
            lostStreak += 1
            array[lostStreak] += 1
            if (highestLostStreak < lostStreak):
                highestLostStreak = lostStreak

    print("\nW/L:", sumWon, "-", sumLost)
    print("Highest Losing Streak:", highestLostStreak)
    print("")
    
    # Making a list of all losing streak possible    
    for i in range(len(array)):         
        if (array[i] != 0):
            print ("Total losing streak of", i, "games :", array[i])
            
    # Making the sublist from the list (from 0 to the highest losing streak)            
    subArray = [0 for x in range(highestLostStreak+1)]            
    for i in range(len(subArray)):
        subArray[i] = array[i]
        
    # Return the sublist
    return subArray
        
# Run the simulation() function
game = int(input("Number of games: "))
list = simulation(game)

print("")
print(list)

# In[2]:

x_pos = [x for x in range(len(list))]

plt.subplots(figsize=(len(list)-2.5,10))

barplot = plt.bar(x_pos, list, align = 'center')
for bar in barplot:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), int(bar.get_height()), ha='center', va='bottom')
    
plt.yticks([])
plt.xticks(x_pos)
plt.ylabel('Total losing streaks')
plt.xlabel('Losing streak of')
plt.title('Distributing of the losing streaks of %i games' %game)
plt.show()
plt.savefig("losingstreak-plot.png", dpi=200)

