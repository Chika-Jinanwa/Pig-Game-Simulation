#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:38:07 2020

@author: jinanwachikafavour
"""
import random
from matplotlib import pyplot as plt
def dice_face(dice_value):
    print(' -------')
    if dice_value==1:
        print('|       |') #graphical representation of dice faces
        print('|   *   |')
        print('|       |')
    elif dice_value==2:
        print('|*      |')
        print('|       |')
        print('|      *|')
    elif dice_value==3:
        print('|      *|')
        print('|   *   |')
        print('|*      |')
    elif dice_value==4:
        print('|*     *|')
        print('|       |')
        print('|*     *|')
    elif dice_value==5:
        print('|*     *|')
        print('|   *   |')
        print('|*     *|')
    elif dice_value==6:
        print('|*  *  *|')
        print('|       |')
        print('|*  *  *|')
    print(' -------')
dice_face(2)
def pig_game(players):
    """This function accepts  the number of players(min of 2 and max of 4) as parameters and simulates the two dice pig game. It accounts for all possiblities for 2 players, 3 players and 4 players """
    if players not in range(2,5): #returns a string message to caller if the parameter is out of range
        return('Parameter you passed to this function is out of range. Pls input an integer between 2 and 4 inclusive')
    else: #simulates the game
        if players==2: #simulates for 2 players
            player1score=0 #initializes player1 score as 0
            player2score=0 #initializes player2 score as 0
            noofturns=1 #initializes number of turns as 1
            lst_player1 = [0] #contains progression of player1 scores for creating a line plot
            lst_player2 = [0]
            lst_turns = [1]
            print('This is Turn 1')
            while player1score<=23 and player2score<=23:#condition for loop to terminate is when either of the players' scores reaches 23 in that particular turn
                dicevalue1=random.randint(1,6) 
                print('This is the face of the first die roll for player1')
                dice_face(dicevalue1)
                dicevalue2=random.randint(1,6) 
                print(' This is the face of the second die for player1')
                dice_face(dicevalue2)
                if dicevalue1!=1 and dicevalue2!=1: #if neither shows a 1,add the dice values
                    player1score+=(dicevalue1+dicevalue2)
                elif (dicevalue1==1 or dicevalue2==1) and (dicevalue1!=1 or dicevalue2!=1): #if a single 1 shows, player's score becomes zero. 
                    player1score=player1score
                elif dicevalue1==1 and dicevalue2==1:
                    player1score=0
                print("Player1's score is",player1score)
                lst_player1 +=[player1score]
                dicevalue3=random.randint(1,6)
                print('This is the face of the first die roll for player2')
                dice_face(dicevalue3)
                dicevalue4=random.randint(1,6)
                print(' This is the face of the second die roll for player2')
                dice_face(dicevalue4)
                if dicevalue3!=1 and dicevalue4!=1:
                    player2score+=(dicevalue3+dicevalue4)
                elif (dicevalue3==1 or dicevalue4==1) and (dicevalue3!=1 or dicevalue4!=1):
                    player2score=player2score
                elif dicevalue3==1 and dicevalue4==1:
                    player2score=0
                print("Player2's score is",player2score)
                lst_player2+=[player2score]
                noofturns+=1 #increments the number of turns by 1 at the end of each loop
                lst_turns+=[noofturns]
                if player1score>=23 and player2score<=23: # if player1 reaches 23 and player2's score is less than 23, player1 wins
                    return('Player1 wins')
                elif player2score>=23 and player1score<=23: #if player2 reaches 23 and player1's score is less than 23,player2 wins
                    return('Player2 wins')
                elif player1score>=23 and player2score>=23: # if both player1 and player2 reach 23 in the same turn, game ends in tie and both players are declared winners
                    return('Tie!Player1 and Player2 both win')
            print('This is Turn',noofturns)
            plt.plot(lst_player1,lst_turns,'-',color="blue",label="Player 1") #plots player1score against total number of turns. Plots a blue colored line graph and labels it as Player1
            plt.plot(lst_player2,lst_turns,'-',color="orange",label="Player 2")#plots player2score against total number of turns. Plots a orange colored line graph and labels it as Player2
            plt.legend(loc="upper left") #adds a legend to the upper left corner of the graph
            plt.title("Graph Showing Players' Running Scores After Each Turn",fontsize=16,fontweight='bold') #adds the title of the graph
            plt.xlabel("Turns") #labels the x axis as Turns
            plt.ylabel("Points") #labels the y axis as Points
            plt.show() #displays the plotted graph 
            #Pls note that the commented steps taken for 2 players are the same steps taken for 3 players and 4 players simulations. If you are confused about any subsequent steps, pls refer to the labelled steps for the 2 player simulation
        elif players==3:
            player1score=0
            player2score=0
            player3score=0
            noofturns=1
            print('This is Turn 1')
            while player1score<=23 and player2score<=23 and player3score<=23:
                dicevalue1=random.randint(1,6)
                print('This is the face of the first die roll for player1')
                dice_face(dicevalue1)
                dicevalue2=random.randint(1,6)
                print(' This is the face of the second die for player1')
                dice_face(dicevalue2)
                if dicevalue1!=1 and dicevalue2!=1:
                    player1score+=(dicevalue1+dicevalue2)
                elif (dicevalue1==1 or dicevalue2==1) and (dicevalue1!=1 or dicevalue2!=1) :
                    player1score=player1score
                elif dicevalue1==1 and dicevalue2==1:
                    player1score=0
                print("Player1's score is",player1score)
                dicevalue3=random.randint(1,6)
                print('This is the face of the first die roll for player2')
                dice_face(dicevalue3)
                dicevalue4=random.randint(1,6)
                print(' This is the face of the second die roll for player2')
                dice_face(dicevalue4)
                if dicevalue3!=1 and dicevalue4!=1:
                    player2score+=(dicevalue3+dicevalue4)
                elif (dicevalue3==1 or dicevalue4==1) and(dicevalue3!=1 or dicevalue4!=1):
                    player2score=player2score
                elif dicevalue3==1 and dicevalue4==1:
                    player2score=0
                print("Player2's score is",player2score)
                dicevalue5=random.randint(1,6)
                print('This is the face of the first die roll for player3')
                dice_face(dicevalue5)
                dicevalue6=random.randint(1,6)
                print(' This is the face of the second die for player3')
                dice_face(dicevalue6)
                if dicevalue5!=1 and dicevalue6!=1:
                    player3score+=(dicevalue5+dicevalue6)
                elif (dicevalue5==1 or dicevalue6==1) and (dicevalue5!=1 or dicevalue6!=1):
                    player3score=player3score
                elif dicevalue5==1 and dicevalue6==1:
                    player3score=0
                print("Player3's score is",player3score)
                if player1score>=23 and player2score<=23 and player3score<=23:
                    return('Player1 wins')
                elif player2score>=23 and player1score<=23 and player3score<=23:
                    return('Player2 wins')
                elif player3score>=23 and player1score<=23 and player2score<=23:
                    return('Player3 wins')
                elif (player1score>=23 and player2score>=23 and player3score<=23):
                    return('Tie!Player1 and Player2 both win')
                elif (player2score>=23 and player3score>=23 and player1score<=23):
                    return('Tie! Player2 and Player3 both win')
                elif (player1score>=23 and player3score>=23 and player2score<=23):
                    return('Tie! Player1 and Player3 both win')
                elif (player1score>=23 and player2score>=23 and player3score>=23):
                    return('Tie! Player1,Player2 and Player3 all win')
                print('This is Turn',noofturns)
                noofturns+=1
            plt.plot(player1score,noofturns,'-',color="blue",label="Player 1")
            plt.plot(player2score,noofturns,'-',color="orange",label="Player 2")
            plt.plot(player3score,noofturns,'-',color="green",label="Player 3")
            plt.legend(loc="upper left")
            plt.title("Graph Showing Players' Running Scores After Each Turn",fontsize=16,fontweight='bold')
            plt.xlabel("Turns")
            plt.ylabel("Points")
            plt.show()
        elif players==4:
            player1score=0
            player2score=0
            player3score=0
            player4score=0
            noofturns=1
            print('This is Turn 1')
            while player1score<=23 and player2score<=23 and player3score<=23 and player4score<=23:
                dicevalue1=random.randint(1,6)
                print('This is the face of the first die roll for player1')
                dice_face(dicevalue1)
                dicevalue2=random.randint(1,6)
                print(' This is the face of the second die for player1')
                dice_face(dicevalue2)
                if dicevalue1!=1 and dicevalue2!=1:
                    player1score+=(dicevalue1+dicevalue2)
                elif (dicevalue1==1 or dicevalue2==1) and (dicevalue1!=1 or dicevalue2!=1):
                    player1score=player1score
                elif dicevalue1==1 and dicevalue2==1:
                    player1score=0
                print("Player1's score is",player1score)
                dicevalue3=random.randint(1,6)
                print('This is the face of the first die roll for player2')
                dice_face(dicevalue3)
                dicevalue4=random.randint(1,6)
                print(' This is the face of the second die roll for player2')
                dice_face(dicevalue4)
                if dicevalue3!=1 and dicevalue4!=1:
                    player2score+=(dicevalue3+dicevalue4)
                elif (dicevalue3==1 or dicevalue4==1) and (dicevalue3!=1 or dicevalue4!=1):
                    player2score=player2score
                elif dicevalue3==1 and dicevalue4==1:
                    player2score=0
                print("Player2's score is",player2score)
                dicevalue5=random.randint(1,6)
                print('This is the face of the first die roll for player3')
                dice_face(dicevalue5)
                dicevalue6=random.randint(1,6)
                print(' This is the face of the second die for player3')
                dice_face(dicevalue6)
                if dicevalue5!=1 and dicevalue6!=1:
                    player3score+=(dicevalue5+dicevalue6)
                elif (dicevalue5==1 or dicevalue6==1) and (dicevalue5!=1 or dicevalue6!=1):
                    player3score=player3score
                elif dicevalue5==1 and dicevalue6==1:
                    player3score=0
                print("Player3's score is",player3score)
                dicevalue7=random.randint(1,6)
                print('This is the face of the first die roll for player4')
                dice_face(dicevalue7)
                dicevalue8=random.randint(1,6)
                print(' This is the face of the second die for player4')
                dice_face(dicevalue8)
                if dicevalue7!=1 and dicevalue8!=1:
                    player4score+=(dicevalue7+dicevalue8)
                elif (dicevalue7==1 or dicevalue8==1) and (dicevalue7!=1 or dicevalue8!=1):
                    player4score=player4score
                elif dicevalue7==1 and dicevalue8==1:
                    player4score=0
                print("Player4's score is",player4score)
                if player1score>=23 and player2score<=23 and player3score<=23 and player4score<=23:
                    return('Player1 wins')
                elif player2score>=23 and player1score<=23 and player3score<=23 and player4score<=23:
                    return('Player2 wins')
                elif player3score>=23 and player1score<=23 and player2score<=23 and player4score<=23:
                    return('Player3 wins')
                elif player4score>=23 and player3score<=23 and player2score<=23 and player1score<=23:
                    return('Player4 wins')
                elif (player1score>=23 and player2score>=23 and player4score<=23 and player3score<=23):
                    return('Tie!Player1 and Player2 both win')
                elif (player2score>=23 and player3score>=23) and player4score<=23 and player3score<=23:
                    return('Tie! Player2 and Player3 both win')
                elif (player1score>=23 and player3score>=23 and player4score<=23 and player2score<=23):
                    return('Tie! Player1 and Player3 both win')
                elif player1score>=23 and player4score>=23 and player2score<=23 and player3score<=23:
                    return('Tie! Player1 and Player4 both win')
                elif player2score>=23 and player4score>=23 and player3score<=23 and player2score<=23:
                    return('Tie! Player2 and Player4 both win')
                elif player3score>=23 and player4score>=23 and player1score<=23 and player2score<=23:
                    return('Tie! Player3 and Player4 both win')
                elif (player1score>=23 and player2score>=23 and player3score>=23 and player4score<=23):
                    return('Tie! Player1,Player2 and Player3 all win')
                elif (player1score>=23 and player2score>=23 and player4score>=23 and player3score<=23):
                    return('Tie! Player1,Player2 and Player4 all win')
                elif (player2score>=23 and player3score>=23 and player4score>=23 and player1score<=23):
                    return ('Tie! Player 2, Player3 and Player4 all win')
                elif (player1score>=23 and player3score>=23 and player4score>=23 and player2score<=23):
                    return('Tie! Player 1,Player3 and Player4 all win')
                elif (player1score>=23 and player2score>=23 and player3score>=23 and player4score>=23):
                    return('Tie! Player 1, Player 2, Player3 and Player4 all win')
                print('This is turn',noofturns)
                noofturns+=1
            plt.plot(player1score,noofturns,'-',color="blue",label="Player 1")
            plt.plot(player2score,noofturns,'-',color="orange",label="Player 2")
            plt.plot(player3score,noofturns,'-',color="green",label="Player 3")
            plt.plot(player4score,noofturns,'-',color="red",label="Player 4")
            plt.legend(loc="upper left")
            plt.title("Graph Showing Players' Running Scores After Each Turn",fontsize=16,fontweight='bold')
            plt.xlabel("Turns")
            plt.ylabel("Points")
            plt.show()
pig_game(2)