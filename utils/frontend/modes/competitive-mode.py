# * COMPETITIVE MODE
# ** Drawing
def competitiveMode_redrawAll(app, canvas):
    # Colors for background: very cool rgbString(0, 0, 100), rgbString(app.r,app.g,app.b)
    drawBackground(app, canvas, rgbString(app.r,app.g,app.b))
    app.road.draw(app, canvas)

    # Draw sky
    canvas.create_image(app.imageX, app.imageY, image=ImageTk.PhotoImage(app.skyImage))



    # Draw all buildings
    app.leftBuildings.draw(app, canvas)
    app.rightBuildings.draw(app, canvas)


    # Draw coin
    app.currentCoin.draw(app, canvas)
    
    # Draw appropiate arms
    app.currentRightArm.draw(app, canvas)
    app.currentLeftArm.draw(app, canvas)
    
    # Draw buttons and counters
    app.backButton.draw(canvas)
    app.paceCounter.draw(canvas)
    app.distanceCounter.draw(canvas)
    app.timeCounter.draw(canvas)
    app.scoreCounter.draw(canvas)

    # Draw message
    if app.showingMessage: drawUserMessage(app, canvas)

# ** Helpers
def competitiveMode_mousePressed(app, event):    
    # If back button pressed:
    app.backButton.isPressed(event, app)
    if app.backButton.pressed:
        time.sleep(0.1) # delay used to simulate button friction
        app.mode = 'startMode'
        app.timerDelay = 20

        # stop playing
        app.playlist[app.c].stop()



def competitiveMode_keyPressed(app, event):
    if event.key == 'Space':            
        # Move surroinding objects faster if running faster
        # Move buildings: we simulate distance of further objects by moving them slower than the closer ones
        for building in app.leftBuildings.buildings:
            if building.y0 < app.height/2: building.move(app, 1)
            else: building.move(app, 1)

        for building in app.rightBuildings.buildings:
            if building.y0 < app.height/2: building.move(app, 1)
            else: building.move(app, 1)

                
        # HEAD BOBBING DOWN
        # Road perspective
        app.road.bottomLeftX -= 3
        app.road.bottomRightX += 3

        # Background image perspective
        app.imageY += 1


    # Movement of player's arms
    if event.key == 'Left':
        if app.leftArmDown.xi[2] > (app.road.bottomLeftX + 200) and app.leftArmUp.xi[2] > (app.road.bottomLeftX + 200):
            # Only move if don't go out frame
            for i in range(len(app.rightArmUp.xi)):
                app.rightArmUp.xi[i] -= 25

            for i in range(len(app.leftArmUp.xi)):
                app.leftArmUp.xi[i] -= 25
            
            for i in range(len(app.rightArmDown.xi)):
                app.rightArmDown.xi[i] -= 25
                
            for i in range(len(app.leftArmDown.xi)):
                app.leftArmDown.xi[i] -= 25

                
                    
    elif event.key == 'Right':
        # Only move if don't go out frame
        if app.rightArmDown.xi[2] < (app.road.bottomRightX - 200) and app.rightArmUp.xi[2] < (app.road.bottomRightX - 200):
            for i in range(len(app.rightArmUp.xi)):
                app.rightArmUp.xi[i] += 25

            for i in range(len(app.leftArmUp.xi)):
                app.leftArmUp.xi[i] += 25
            
            for i in range(len(app.rightArmDown.xi)):
                app.rightArmDown.xi[i] += 25
                
            for i in range(len(app.leftArmDown.xi)):
                app.leftArmDown.xi[i] += 25
            
                    


def competitiveMode_keyReleased(app, event):
    if event.key == 'Space':
        # HEAD BOBBING UP
# When your heads goes up, you go faster, so buildings and dashes approach the user faster than they would usually. So we add more movement to them.

        # If already in process of moving, reset counter
        if app.spacePressed == True: app.counter = 0
        else: app.spacePressed = True

        # Road perspective
        app.road.bottomLeftX += 3
        app.road.bottomRightX -= 3

        # Background image perspective
        app.imageY -= 1

        
        # Buildings        
        for building in app.leftBuildings.buildings:
            if building.y0 < app.height/2: building.move(app, 4)
            else: building.move(app, 7)

        for building in app.rightBuildings.buildings:
            if building.y0 < app.height/2: building.move(app, 4)
            else: building.move(app, 7)


        # Switching arm up
        app.isRightArmUp = not app.isRightArmUp

        if app.isRightArmUp == True:
            app.currentRightArm = app.rightArmUp
            app.currentLeftArm = app.leftArmDown
        else:
            app.currentRightArm = app.rightArmDown
            app.currentLeftArm = app.leftArmUp
        

        # ADD STEP INTO DISTANCE RUN
        # Convert back to float
        app.distanceCounter.value = float(app.distanceCounter.value)
        
        # Increase distance by whatever calculation
        app.distanceCounter.value += app.strideMeters
        
        # Make sure only displays two decimals        
        app.distanceCounter.value = reduceDecimals(app.distanceCounter.value)
    
        
            
def competitiveMode_timerFired(app):
    app.miliseconds += 1

    if app.start == True:
        # Since timerFired is set at 100, but only want every second, we compensate by substracting 0.1s
        app.timeCounter.value -= 0.03
        app.timeCounter.value = float(reduceDecimals(app.timeCounter.value))

    # Gif
    app.spriteCounter = (1 + app.spriteCounter) % len(app.spritePhotoImages)

    # MAKE ALL MOVEMENTS SURROUNDINGS
    # Move buildings: we simulate distance of further objects by moving them slower than the closer ones
    for building in app.leftBuildings.buildings:
        if building.y0 < app.height/2: building.move(app, 1.4)
        else: building.move(app, 3)

    for building in app.rightBuildings.buildings:
        if building.y0 < app.height/2: building.move(app, 1.4)
        else: building.move(app, 3)


    # Move dashes on road:
    for dash in app.road.roadDashes:
        if dash.y0 < app.height/2.2: dash.move(app, 1)
        else: dash.move(app, 1.5)



    if app.spacePressed == True:
        if app.counter <= 10:
            app.counter += 1
            
            for dash in app.road.roadDashes:
                if dash.y0 < app.height/2.2: dash.move(app, 2)
                else: dash.move(app, 4)

        else:
            app.counter = 0
            app.spacePressed = False        
        

    # MOVE CURRENT COIN
    app.currentCoin.move(app, app.coinDisplacement)
    # app.currentCoin.move(app, 16)

    # check in contact right arm
    if app.currentCoin.inContact(app.rightArmUp):
        print('seeing')
        if app.currentRightArm == app.rightArmDown:
            # decrease score
            app.scoreCounter.value -= 1
            # reset coins
            app.COINS.resetCoins(app)

        else:
            # increase score
            app.scoreCounter.value += 1
            # reset coins
            app.COINS.resetCoins(app)


    # check in contact left arm
    elif app.currentCoin.inContact(app.leftArmUp):
        if app.currentLeftArm == app.leftArmDown:
            # decrease score
            app.scoreCounter.value -= 1
            # reset coins
            app.COINS.resetCoins(app)


        else:
            # increase score
            app.scoreCounter.value += 1
            # reset coins
            app.COINS.resetCoins(app)


    # SONGS
    # Play next song if music stops playing
    if not app.playlist[app.c].isPlaying():
        # change counter value (not commiting error of passing index)
        if app.c <= len(app.playlist)-1:
            app.c += 1
            app.playlist[app.c].start()

        else:
            app.c = 0
            app.playlist[app.c].start()



    

    # Determine if player is on track or off track
    if float(app.distanceCounter.value) + 5 >= float(onTrackDistance(app)):
        app.on_track = True    
    else: app.on_track = False
        

    # Check if runner made the objective
    checkRunnerFinished(app)



    # On / Off track MESSAGES
    # Only draw every 10 seconds with app.timeRunning % 10 == 0

    if app.showingMessage == True:
        if app.messageTimeCounter < 75: app.messageTimeCounter += 1
        else:
            app.showingMessage = False
            app.messageTimeCounter = 0

            # we set the current message to a random value
            app.currentOnTrackMessage = app.onTrackMessages[randint(0, len(app.onTrackMessages)-1)]
            app.currentOffTrackMessage = app.offTrackMessages[randint(0, len(app.offTrackMessages)-1)]

    
    
    try:
        if ( int(app.timeRunning) % 10 == 0 and
             int(app.timeRunning) != app.lastInt ):
            app.showingMessage = True
            app.lastInt = int(app.timeRunning)
            print(app.lastInt)
            
    except: pass
    
# ** Transition
def transitionToCompetitive(app):
    
    # Reset distance from previous session
    if app.distanceCounter.value != 0: app.distanceCounter.value = 0
        
    # Setup all the required data
    setRequiredParameters(app)
    
    time.sleep(0.1) # delay used to simulate button friction
    app.mode = 'competitiveMode'
    app.timerDelay = 1


    # Set the speed for our rhythm marking coins
    x1, x0, y1, y0 = 734, 630, 513, 300
    distanceOneCoinRun = sqrt((x1-x0)**2 + (y1-y0)**2) # point (x0,y0) to (x1,y1)
    print(f'Distance: {distanceOneCoinRun}')
    timePerStep = 60/app.paceCounter.value # seconds
    # print(f'Time: {timePerStep}')
    app.miliseconds = 0
    speedCoin = distanceOneCoinRun / timePerStep
    app.coinDisplacement = 0.0422*speedCoin
    print(app.coinDisplacement)

    
    # Changing songs to set pace
    for song in app.playlist: song.changeTempo(app.stepsPerMinute)

    app.playlist =  getAlteredSongs()

    # START PLAYING SONGS
    # We start to play the songs, as well as start the countdown
    app.start = True

    # Play our playlist
    # Shuffle the playlist
    shuffle(app.playlist)
    app.playlist[app.c].start()
