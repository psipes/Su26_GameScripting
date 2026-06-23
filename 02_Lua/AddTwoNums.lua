--Author: Pat Sipes
-- Add Two user numbers together

--variables
local num1 = nil
local num2 = nil
local sum = 0

-- Get first number 
while (num1 == nil or num1 == "" or not tonumber(num1)) do
    print("What is the first number: ")
    num1 = io.read()
end
--Get Second number 
while (num2 == nil or num2 == "" or not tonumber(num2)) do
    print("What is the second number: ")
    num2 = io.read()
end

--Add numbers together
sum = num1 + num2

-- Print total
print(num1.." + "..num2.." = "..sum)