# * FOLLOW MODE

followMode_redrawAll = competitiveMode_redrawAll

followMode_mousePressed = competitiveMode_mousePressed

followMode_keyPressed = competitiveMode_keyPressed

followMode_keyReleased = competitiveMode_keyReleased
        
def followMode_timerFired(app):
    
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

    # check in contact right arm
    if app.currentCoin.inContact(app.rightArmUp):
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



def transitionToFollowMode(app):
        # Reset distance from previous session
        if app.distanceCounter.value != 0: app.distanceCounter.value = 0
        
        # Setup all the required data
        app.distanceMeters = 100000000
        app.timeMinutes = 1000000
        app.timeSeconds = app.timeMinutes*60
        app.timeCounter.value = 10000
        app.heightMeters = 1.83
        app.strideMeters = app.heightMeters * 1.17
        app.paceCounter.value = app.bpm_Tempo

        time.sleep(0.1) # delay used to simulate button friction
        app.mode = 'followMode'
        app.timerDelay = 1


        # Setup coin sped
        # Set the speed for our rhythm marking coins
        x1, x0, y1, y0 = 734, 630, 513, 300
        distanceOneCoinRun = sqrt((x1-x0)**2 + (y1-y0)**2) # point (x0,y0) to (x1,y1)
        timePerStep = 60/app.paceCounter.value # seconds
        app.miliseconds = 0
        speedCoin = distanceOneCoinRun / timePerStep
        app.coinDisplacement = 0.0422*speedCoin

        # Changing songs to set pace
        for song in app.playlist: song.changeTempo(app.paceCounter.value)

        app.playlist =  getAlteredSongs()

        # START PLAYING SONGS
        # We start to play the songs, as well as start the countdown
        app.start = True

        # Play our playlist
        # Shuffle the playlist
        shuffle(app.playlist)
        app.playlist[app.c].start()
