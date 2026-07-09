import random
#Author: Pat Sipes
#get 10 random numbers,
# print how many are even (right)
# print how many are odd (left)
# how many zeroes

counter = 0
zeroCount = 0
evenCount = 0
oddCount = 0
compNum = 0

while counter < 10:
    #get a random num
    compNum = random.randint(0,100)
    print(compNum)
    if compNum == 0: #zero
        zeroCount  = zeroCount + 1
    elif compNum % 2 == 1: #odd
        oddCount = oddCount + 1
    else: #even
        evenCount = evenCount + 1
    counter = counter + 1

print ("Zeros: " + str(zeroCount))
print("Left Count: " + str(oddCount))
print("Right Count: " + str(evenCount))