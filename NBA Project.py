#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:25:49 2020

@author: bryce
"""

import pandas as pd

df = pd.read_excel(r'/Users/bryce/Documents/Python/NBA_PROJECT/nba odds 2018-19.xlsx', sheet_name='WARRIORS')
wager = int(input(f'How much money would you like to wager on the Golden State Warriors for the whole season to see the amount you made or lost?  '))

def games_won():
    result = df["W/L"].to_list()        #puts the wins and losses into a list and corresponds correctly with the money_line list
    losses = df['W/L'].value_counts()   #shows the user the amount of wins and losses on the season
    print()
    print(f'The Warriors won {losses[0]} games and lost {losses[1]} games in the playoffs and regular season')
    money_line = df["ML"].to_list()          
    count = 0       #to be able to index the correct moneyline by keeping a count in the for loop  
    total = 0       #tracks the amount of money made/loss  
    for ans in result:
        count += 1
        x = money_line[count-1]         #has to have -1 for the count to account for the first index in the money_line list. Used 'x' to make it easy to write in future commands
        if ans == 'W':
            if x > 0:           #returns games the Warriors are favored in
                return_rate = x/100         #turns into a rate for favored games
            else:
                return_rate = (100/x) * -1   #returns correct rate by making it positive because it is orginal negative from Warriors being favored                    
            amt = wager * return_rate     #takes the correct rate of return and multiplys it by the wagered amount(has to be outside the second if statement to recognize both rates)
            total += amt        #running total    
        else:
            total += (wager * -1)    #this accounts for the losses thats why the wager is multiplied by negative one to correctly add the total
    print()
    print(f'This is how much you would owe or make, ${total:.2f}')
    
games_won()




