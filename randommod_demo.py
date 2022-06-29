import random
# values=random.random()
# print(values)

# values=random.randint(0,1) #both 1 and 4 will come
# print(values)

# values=random.uniform(1,4) #both 1 and 4 will come
# print(values)

# l=['1','2','3','4']
# print(random.choices(l,weights=[10,10,0,0],k=10))

# deck=list(range(1,20))
# random.shuffle(deck)
# print(deck)


# deck=list(range(1,50))
# hand=random.sample(deck,k=5)
# print(hand)


import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")













