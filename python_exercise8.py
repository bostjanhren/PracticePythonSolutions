new = True
while(new):
	input1 = raw_input("Enter (rock/paper/scissors): ")
	while (input1 != "rock" and input1 != "paper" and input1 != "scissors"):
		input1 = raw_input("Oopsie! Try again (rock/paper/scissors): ")
	input2 = raw_input("Enter (rock/paper/scissors): ")
	while (input2 != "rock" and input2 != "paper" and input2 != "scissors"):
		input2 = raw_input("Oopsie! Try again (rock/paper/scissors): ")
	
	if input1 == input2 :
		print("Tie")
	elif input1 == "rock":
		if input2 == "paper":
			print("Player 2 wins")
		else :
			print("Player 1 wins")
	elif input1 == "paper":
		if input2 == "rock":
			print("Player 1 wins")
		else: 
			print("Player 2 wins")
	else: #input1 = scissors
		if input2 == "rock":
			print("Player 2 wins")
		else:
			print("Player 1 wins")
	
	newgame = raw_input("print 'quit' to stop or Enter to play a new game.\n")
	if newgame == "quit":
		new = False
		

