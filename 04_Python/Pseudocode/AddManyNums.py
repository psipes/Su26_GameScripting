#Author: Pat Sipes
#Add numbers to running sum until user says no more
#print("Hello from Many Nums")

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

def AddNewNum(total):
    newNum = "a"
    newNum = input("next Number to Add: ")
    newNum = TryAgain(newNum)
    total = float(total) + float(newNum)
    return total

sum = 0
sum = AddNewNum(sum)
print(sum)
while CheckContinue():
    sum = AddNewNum(sum)
    print(sum)