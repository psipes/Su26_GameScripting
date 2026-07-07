# Author: Pat Sipes
# Two nums from user
# Print sum
# print("Hello from Two Nums")

#if integer or float, return true
#else return false
def CheckIfNum(userInput):
    return bool(userInput.isdigit() or isinstance(userInput, float))


#keep asking for a number until valid number given
def TryAgain(userInput):
    while not CheckIfNum(userInput):
        userInput = input("That's not a valid number, try again: ")
    return userInput

num1 = input("Give me a number: ")
num1 = TryAgain(num1)

num2 = input("Give me another number: ")
num2 = TryAgain(num2)

print(num1 + " + " + num2 + " = " + (str((float(num1) + float(num2)))))

