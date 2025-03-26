import random

def player():
    #player plays
    print('player is playing')
    global player_score
    player_score=0
    while True:
        choices=[1,2,3,4,5,6]
        computer=random.choice(choices)
        player=int(input('enter your number:'))
        print('computer bowls',computer)
        if player not in choices:
            print("enter from 1 to 6")
            continue

        
        if computer==player:
            print('you are output')
            break
            
        else:
            player_score=player_score+player
    print('the player score is',player_score)

def computer():
    print('now computer is playing')
    #computer plays 
    global computer_score  
    computer_score=0
    while True:
        choices=[1,2,3,4,5,6]
        computer=random.choice(choices)
        player=int(input('enter your number:'))
        print('computer run',computer)

        
        if computer==player:
            print('computer  is output')
            break
            
        else:
            computer_score=computer_score+player
    print('the computer score is',computer_score)

toss=input('enter your choice (bat or bowl)?:')
if toss=='bat':
    player()
    computer()
else:
    computer()
    player()

if computer_score>player_score:
    print('computer won')
else:
    print('you won')