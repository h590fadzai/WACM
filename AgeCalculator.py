import os
import platform
import time
import datetime

date = datetime.datetime.now()

def clearScreen():
	if str(platform.system()) == "Windows":
		os.system("cls")
	else:
		os.system("clear")

while True:
	clearScreen()
	dateOfBirth = input("What year were you born in? ")
	try:
		int(dateOfBirth)
		print("You are turning or already are", int(date.year) - int(dateOfBirth), "this year")
		input(" ")
	except ValueError:
		input("That is not a number, please write a number.\nPress enter to restart.")