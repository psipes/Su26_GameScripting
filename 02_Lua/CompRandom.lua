-- Author: Pat Sipes
-- Get user defined high,
-- have comp give random num between 0 and user high
-- **ALLOW TO CONTINUE PLAY

function printRandomNum()
    --variables
    maxNum = nil
    playAgain = "Y"
    
    --Set up random 
    math.randomseed(os.time()) --gives us basis
    math.random() ; math.random() ; math.random() --clear out old values

    --While Still Playing
    while playAgain == "Y" do
        --Ask user for max 
        while (maxNum == nil or maxNum == "" or not tonumber(maxNum)) do
            print ("Give me the high number: ")
            maxNum = io.read()
        end

        --print out random number
        print("The computer picked: "..math.random(1, maxNum))

        --ask user if wants to play again
        print("Press /'Y/' for another number, or any other key to quit: ")
        playAgain = io.read()
        if string.upper(playAgain) ~= "Y" then
            break
        else
            playAgain = "Y"
            maxNum = nil
        end
    end
        
    print ("Thank you for playing :) Goodbye.")
end

printRandomNum()