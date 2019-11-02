import random
a = random.randint(1,9)
n = 0
while(True):
	vnos = raw_input("Guess a number between 1 and 9 or type 'exit' to stop: ")
	n+=1	
	if(vnos == "exit"):
		break
	else:
		stevilo = int(vnos)
		if a == stevilo:
			print("You won in " + str(n) + " steps!")
			n = 0
			a = random.randint(1,9)
		elif a > stevilo:
			print("Try higher")
		else :
			print("Try lower")

