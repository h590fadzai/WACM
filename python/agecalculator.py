# Importing required functions
import datetime

# Set a variable called date to the present date
date = datetime.datetime.now()

# Print a lovely welcome
print("Welcome to my age calculator")

# Ask the user for their birth year
birthYear 	= input("What is your birth year?\n> ")
birthMonth 	= input("What is your birth month?\n> ")
birthDay	= input("what is your birth day?\n> ")

# Subtract users birth year from current year
birthYear = date.year - int(birthYear)

if int(birthMonth) >= date.month:
	if int(birthDay) >= date.day:
		birthYear = birthYear - 1

# Print input to the screen
print("You are", birthYear, "years old")
