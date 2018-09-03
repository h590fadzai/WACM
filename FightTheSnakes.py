import random
import os
import platform

def clearScreen():
	if str(platform.system()) == "Windows":
		os.system("cls")
	else:
		os.system("clear")

# Fight function that call each time an attack occurs
def fight(pHealth, pAttack, sHealth, sAttack):
	while True:
		if pHealth <= 0:
			return "snake"
		elif sHealth <= 0:
			return "player"

		print("                  __              ,,, ")
		print("      _______    /*_>-<          (0|  ")
		print("  ___/ _____ \__/ /        ----+_/|\  ")
		print(" <____/     \____/               / \  ")
		print("")
		print("Health:", sHealth, 20*" ","Health:", pHealth)
		print("Attack:", sAttack, 20*" ","Attack:", pAttack)

		print("\nWould you like to [attack] or [defend]?")
		playerAtkDef 	= input("> ").lower()
		snakeAtkDefStp 	= random.randint(1,3)

		if playerAtkDef == "attack" or playerAtkDef == "a":
			# Player Attacks
			if snakeAtkDefStp == 1:
				# Snake Attacks
				pHealth = pHealth - sAttack
				sHealth = sHealth - pAttack
			elif snakeAtkDefStp == 2:
				# Snake Defends
				sHealth = sHealth - pAttack/2
			else:
				# Snake Stops
				sHealth = sHealth - pAttack
		elif playerAtkDef == "defend" or playerAtkDef == "d":
			# Player Defends
			if snakeAtkDefStp == 1:
				# Snake Attacks
				pHealth = pHealth - sAttack/2
		clearScreen()

# Set starting variables
begining = True

# Game loop
while True:
	clearScreen()
	# This if statement only runs once for the -
	# - beginning of the game 
	if begining == True:
		# Welcome print
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("||    Welcome to the Python Arena    ||")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

		# Set variables
		playerHealth 	= 10
		playerAttack 	= 2
		begining = False

	print("Mr Sparkly, You're next in the arena!!!")

	# Randomly assign snake stats
	snakeHealth 	= random.randint(1,10)
	snakeAttack 	= random.randint(2,5)

	winner = fight(playerHealth, playerAttack, snakeHealth, snakeAttack)
	
	if winner == "snake":
		print(12*" ","  _____")
		print(12*" "," /     \\")
		print(12*" ","| () () |")
		print(12*" "," \  ^  /")
		print(12*" ","  |||||")
		print(12*" ","  |||||")
		print("\nOh No, Mr Sparkly has feinted!!")
	else:
		print(12*" ","  .__.")
		print(12*" "," (|  |)")
		print(12*" ","  (  )")
		print(12*" ","  _)(_")
		print("\nCongrats you killed the python!!")
		
	restart = input("Would you like to play again? [yes] or [no]")

	if restart == "y" or restart == "yes":
		begining = True
	else:
		break