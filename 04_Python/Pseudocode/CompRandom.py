import random
#Author: Pat Sipes
#user defined max
#Give user random number
#Ask user if want another random number
#keep looping until user no longer wants more
#print("Hello from CompRandom")

def CheckContinue():
    playAgain = "a"
    while playAgain != "Y" or playAgain != "N":
        playAgain = str.upper(input("Would you like to add another number (Y/N?)"))
        if playAgain == "Y":
            return True
        if playAgain == "N":
            return False
        
#check if letter
# letters = true
# else, false
def InputIsLetter(userInput):
    if userInput.isalpha():
        return True
    else:
        return False
    

#check if space
# spaces, true
# stuff, false
def InputIsSpace(userInput):
    if userInput.isspace():
        return True
    else:
        return False
    

#check if enter/empty
# length less than 1, true
# 1 or more, false
def InputIsEnter(userInput):
    if len(userInput) < 1:
        return True
    else:
        return False

#master error check
def TryAgain(userInput):
    while InputIsLetter(userInput) or InputIsSpace(userInput) or InputIsEnter(userInput):
        userInput = input("Please give a valid number: ")
    return userInput
        

userMax = "a"
compNum = "a"

userMax = input("Give me the maximum whole number: ")
userMax = TryAgain(userMax)
compNum = random.randint(0, int(userMax))
print(compNum)

while CheckContinue():
    userMax = input("Give me the maximum whole number: ")
    userMax = TryAgain(userMax)
    compNum = random.randint(0, int(userMax))
    print("Random Number: " + str(compNum))
