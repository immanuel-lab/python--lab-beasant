import random


while True:
	computer=0
	player=0
	choices=['rock','paper','scisscor']
	computer=random.choice(choices)
	player=input("enter rock,paper or scisscor:").lower()

	if computer==player:
		print(computer)
		print(player)
		print('a tie')
	if computer=='rock':
	 	if player=='paper':
	 		print(computer)
	 		print(player)
	 		print('player won')


	if player=='rock':
	 	if computer=='paper':
		 	print(computer)
			print(player)
			print('computer won')
	if computer=='paper':
	 	if player=='scisscor':
		 	print(computer)
			print(player)
			print('player won')
	if player=='paper':
	 	if computer=='scisscor':
		 	print(computer)
			print(player)
			print('computer won')
	if computer=='rock':
	 	if player=='scisscor':
		 	print(computer)
			print(player)
			print('computer won')
	if player=='rock':
	 	if computer='scisscor':
	 		print(computer)
			print(player)
			print('player won')
	play_again=input("play again? (y/n)")
	if play_again==n:
	break


print('good bye')


