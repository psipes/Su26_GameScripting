-- Author: Pat Sipes
-- Add numbers from users until they say stop


function printUserSum()
--variables
local newNum = nil
local sum = 0
local mathDone = false
local userChoice = ""


--while the math isn't done/user wants more nums
while not mathDone do
    --Get new number 
    while (newNum == nil or newNum == "" or not tonumber(newNum)) do
        print("What number to add next: ")
        newNum = io.read()
    end
    --Add to total
    sum = sum + newNum

    --reset newNum
    newNum = nil


    --Ask user if they want another number 
    print ("Press \'Q\' to Quit, any other key to continue: ")
    userChoice = io.read()
    if string.upper(userChoice) == "Q" then
        --print total
        print("The sum is: "..sum)
        mathDone = true
        break
    end
    --reset userChoice
    userChoice = nil
end


end

printUserSum()