# This Python adventure experience was made by Adam Brickhill
# ----------------------------------------------------
# 			Welcome to Escape the Python
# ----------------------------------------------------

# Imports
import time
import random
import os
import platform

# Variable
noCheck = ['No', 'no', 'n', 'NO', 'N']
yesCheck = ['Yes', 'yes', 'ye', 'y', 'YES', 'N']

# title takes one string variable that centers inside a border
# Use the title function to show information
def title(text):
	width = len(text) + 10
	print("=" * width)
	print("|" + text.center(width-2) + "|")
	print("=" * width)

# Clears the screen depending on your operating system
def clearScreen():
	if str(platform.system()) == "Windows":
		os.system("cls")
	else:
		os.system("clear")

def levelOne():
	global yesCheck

	clearScreen()
	title("Level One")

	lvlOneCh1 = input("You awake... You see only darkness. You feel a backpack on your back.\nWould you like to check it?")
	
	if lvlOneCh1 in yesCheck:
		return True
	else:
		input("You sit in darkness expecting something to happen... but it doesn't")
		return False

def gameLoop():
	cLevelOne = False

	title("Welcome to Escape the Python")
	time.sleep(3)

	while cLevelOne == False:
		cLevelOne = levelOne()

	title("You completed the game")
	input()

complete = gameLoop()