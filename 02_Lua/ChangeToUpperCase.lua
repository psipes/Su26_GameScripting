--Author: Pat Sipes
--Convert user input to upper case

function capitalizeIt()
    --variables
    userInput = nil
    inputCapped = nil

    --while can't be capitalized loop
    while (userInput == nil or userInput == "" or userInput == tonumber(userInput) or userInput == string.upper(userInput)) do
        --Prompt user
        print("What phrase do you want to capitalize? ")
        --get user Input to capitalize 
        userInput = io.read()
    end

    --capitalize it
    inputCapped = string.upper(userInput)
    return inputCapped

end

--print capitalized version
print(capitalizeIt())