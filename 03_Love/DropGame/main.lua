-- start debugger (special to vsCode extension)
-- f5 to run WITH debugger
-- shift f5 for NO debug 
if arg[2] == "debug" then
    require("lldebugger").start()
end

--Author: Pat Sipes
--Project: Drop Game
--Objects fall from ceiling. If hit ground, end game.


---------------------------------------------
--LOAD ALL THE THINGS------------------------
---------------------------------------------
function titleLoad()
  titleText = "Frog Plop"
end

function titleDraw()
  --create text 100 pt stretches across the screen at 200 y and centered
  love.graphics.setFont(love.graphics.newFont(100))
  love.graphics.printf(titleText, 0, 200, 800, "center")


  --create a button
  love.graphics.setColor(1,1,1)
  love.graphics.rectangle("fill", 50, 450, 250, 100, 10, 10, 6)
  love.graphics.setColor(1,0,0)
  love.graphics.setFont(love.graphics.newFont(75))
  love.graphics.printf("PLAY", 50, 450, 250, "center")

  love.graphics.setColor(1,1,1)

end
function love.load()

    winWidth = 1024
    winHeight = 768
    --set window size
    success = love.window.updateMode(winWidth, winHeight)
    love.window.setTitle("Frog Plop")
    titleLoad()
    -- 0 = title screen
    -- 1 = game time
    -- 2 = game over
    scene = 0

    ----------------------------------------
    --Randomization
    math.randomseed(os.time())
    math.random(); math.random(); math.random()


    ----------------------------------------
    -- Frog Stuff
    --graphic with bounding box
    frog = love.graphics.newImage("frog.png")
    --how many spawn
    frogNum = 5
    --location
    frogX = {}
    frogY = {}
    --speed
    frogSpeed = {}
    minSpeed = 10
    maxSpeed = 20
    speedMod = 1

    count = frogNum

    --For each frog, start where and how fast?
    while count > 0 do
        --give random x value to each frog 
        frogX[#frogX+1] = math.random(0, love.graphics.getWidth() - frog:getWidth())
        --give random y value to each frog 
        frogY[#frogY+1] = 0
        --decrease count
        count = count - 1
        --Assign speeds
        frogSpeed[#frogSpeed + 1] = math.random(minSpeed, maxSpeed)
    end
end

---------------------------------------------
--CLICK ALL THE THINGS------------------------
---------------------------------------------
function love.mousepressed(x, y, button, istouch)
    if button == 1 then
        if scene == 0 then
            if x >= 50 and x <= 300 and y >=450 and y <= 550 then
                scene = 1 --go to play area
            end
        end
        if scene == 1 then
            --check each image if they've been touched
            for i, value in ipairs (frogX) do
                if x >= frogX[i] and x <= frogX[i] + frog:getWidth() and y >= frogY[i] and y <= frogY[i] + frog:getHeight() then
                    --print ("hit it!") 
                    --Randomization
                    math.randomseed(os.time())
                    math.random(); math.random(); math.random()

                    --Send the frog back to top, razzle dazzle
                    speedMod = speedMod + 1
                    maxSpeed = maxSpeed + speedMod
                    frogX[i] = math.random(0, love.graphics.getWidth() - frog:getWidth())
                    frogY[i] = 0 - (math.random(frog:getHeight(), frog:getHeight()*2))
                    frogSpeed[i] = math.random(frogSpeed[i], maxSpeed)

                    break --so it only clicks something once
                end
            end
        end
    end
end


---------------------------------------------
--UPDATE ALL THE THINGS----------------------
---------------------------------------------
function love.update(dt)
   if scene == 1 then
        for i, value in ipairs(frogX) do
            --check and see if they've gone over the edge
            if frogY[i] + frog:getHeight() >= love.graphics.getHeight() then
                --Over the Edge
                --transition to gameover screen
                love.event.quit() --love.event.quit("restart") will restart everything
            end
            --move the objects
            frogY[i] = frogY[i] + frogSpeed[i] * dt
        end
   end
end


---------------------------------------------
--DRAW ALL THE THINGS------------------------
---------------------------------------------
function love.draw()
    if scene == 0 then
        titleDraw()
    end
    if scene == 1 then
        for i, value in ipairs (frogX) do
            love.graphics.draw(frog, frogX[i],frogY[i])
        end
    end
end






--this is our debugger code
local love_errorhandler = love.errorhandler

function love.errorhandler(msg)
    if lldebugger then
        error(msg, 2)
    else
        return love_errorhandler(msg)
    end
end



