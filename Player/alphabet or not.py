while True:
	print("Enter '0' for exit.")
	x = input("Enter any character: ")
	if x == '0':
		break
	else:
		if((x>='a' and x<='z') or (x>='A' and x<='Z')):
			print(x, "is an alphabet.\n")
		else:
			print(x, "is not an alphabet.\n")
