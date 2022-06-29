import random

while True:

    choices = ['rock', 'paper', 'scissor']
    computer = random.choice(choices)

    player = input("enter rock,paper or scissor:").lower()
    if player not in choices:
        print("enter either rock,paper or scissor")


    if computer == player:
        print(computer)
        print(player)
        print('a tie')
    if computer == 'rock' and player == 'paper':
        print(computer)
        print(player)
        print('player won')

    if player == 'rock' and computer == 'paper':
        print(computer)
        print(player)
        print('computer won')
    if computer == 'paper' and player == 'scisscor':
        print(computer)
        print(player)
        print('player won')
    if player == 'paper' and computer == 'scisscor':
        print(computer)
        print(player)
        print('computer won')
    if computer == 'rock' and player == 'scisscor':
        print(computer)
        print(player)
        print('computer won')
    if player == 'rock' and computer == 'scisscor':
        print(computer)
        print(player)
        print('player won')

    play_again = input("play again? (y/n)").lower()
    if play_again == 'n':
        break
print('good bye')
