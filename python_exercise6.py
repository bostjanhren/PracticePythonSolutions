word = raw_input("Input string: ")
palindrom = True

for i in range(len(word)) :
	if(word[i] !=  word[len(word)-1-i]) :
		palindrom = False
		break

if palindrom :
	print("Palindrom")
else :
	print("Ni palindrom")
