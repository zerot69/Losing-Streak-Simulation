# Losing-Streak-Simulation
A simple Python simulation of the occurrence of losing streaks in a 50/50 game

The code simulates a 50/50 gamble and export the total amount of each losing streak in 'gameTotal' games, which is inputted from the user. In each game, a number is randomized, it can be 0 or 1. If the number is 0, the player lost and a losing streak is recorded. Until the number 1 is randomized, which means the player wins, the streak will stop and its value is stored into a list, which stores all the number of each losing streak. When 'gameTotal' games are finished, a sublist of the list from losing streak of 0 to the highest losing streak is returned.
