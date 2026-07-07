# Author: Pat Sipes
# take user string, print out capitalized version
#print ("hello from CapIT")

#check if number
#return true if number
#return false if NOT a number
def CheckIfNum(userInput):
    if userInput.isdigit():
        print("Numbers can't be capitalized.")
    return userInput.isdigit()

#check if spaces
#return true if spaces
#return false if not
def CheckIfSpaces(userInput):
    if userInput.isspace():
        print ("Spaces can't be capitalized.")
    return userInput.isspace()

#check if empty
#true if empty
#false if stuff
def CheckIfEmpty(userInput):
    if not userInput:
        print ("Empty entry cannot be capitalized.")
        return True
    else:
        return False

#check if capped
#true capped
#false mixed/lower
def CheckIfCapped(userInput):
    if userInput ==str.upper(userInput):
        print("This is already capitalized.")
        return True
    else:
        return False

#check all
def CheckAll(userInput):
    while CheckIfNum(userInput) or CheckIfSpaces(userInput) or CheckIfEmpty(userInput) or CheckIfCapped(userInput):
        userInput = input("Type Something Valid: ")
    return userInput

strToUpper = input("Write Something to Capitalize: ")
print(str.upper(CheckAll(strToUpper)))

# at most simple:
# print(str.upper(input("Write something to Capitalize: ")))