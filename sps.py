import random

while True:
	comp_list=["Rock","Paper","Scissor"]
	user = input("Please choose an option:").capitalize()
	if user in comp_list:
		pass
	else:
		print("Wrong Input")
		continue  #when the code reaches here, it will ignore all the lines below and go back to the beginning.


	comp = random.choice(comp_list)

	print(f"You choose : {user}")
	print(f"Computer choose : {comp}\n")

	if user == "Rock" and comp == "Scissor":
		print("You Win!!!\n")
	elif user == "Rock" and comp == "Paper":
		print("Computer Wins!!!\n")
	elif user == "Rock" and comp == "Rock":
		print("Draw!!!\n")
	elif user == "Paper" and comp == "Scissor":
		print("Computer Wins!!!\n");
	elif user == "Paper" and comp == "Paper":
		print("Draw!!!\n")
	elif user == "Paper" and comp == "Rock":
	 	print("You Win!!!")
	elif user == "Scissor" and comp == "Scissor":
		print("Draw!!!\n");
	elif user == "Scissor" and comp == "Paper":
		print("You Win!!!\n")
	elif user == "Scissor" and comp == "Rock":
	 	print("Computer Win!!!\n")
	
	repeat = input("Do you want to continue? (Y/N)\n").capitalize()

	if "Y" in repeat:
		continue
	else :
		exit()	