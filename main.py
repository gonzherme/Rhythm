




# * Main: Run Program
def appStarted(app):
    app.TESTX = app.width/4
    app.mode = 'instructionsMode'
    setupInstructions(app)

    # MESSAGES
    app.showingMessage = False
    app.messageTimeCounter = 0

    # Set messages to user
    app.onTrackMessages = ['Good Work!', 'Keep it going!', 'Nice pace!']
    app.offTrackMessages = ["You're falling behind!", 'Try a bit harder!']

    # Set current message
    app.currentOnTrackMessage = app.onTrackMessages[randint(0, len(app.onTrackMessages)-1)]
    app.currentOffTrackMessage = app.offTrackMessages[randint(0, len(app.offTrackMessages)-1)]

    ##################
    
    app.imageX = app.width/2
    # app.imageY = 0.01*app.height
    app.imageY = 0.15*app.height

    
    app.start = False
    app.isRightArmUp = False # boolean for movement of arms in 3D
    app.margin = 0
    app.colors = ['green', 'purple', 'pink', 'red',
                  'yellow', 'blue', 'orange']
    app.currentColor = app.colors[randint(0,len(app.colors)-1)]

    app.c = 0 # index of the song playlist 
    
    app.cx = app.width/2 # x of point 3D graphics point to
    app.cy = (app.height/4) # y of point 3D graphics point to

    app.lx = app.width/2 # second 3D point
    app.ly = (1.2*app.height/4)

    app.playlist = getOriginalSongs()

    app.lastInt = 0
    
    # Loading gif
    app.spritePhotoImages = loadAnimatedGif('images/blue_ncs.gif')
    app.spriteCounter = 0


    ######## EDITS TESTING COUNTER
    app.timerDelay = 0
    app.counter = 0
    app.spacePressed = False

    # Loading image of sky
    app.skyImage = app.loadImage('images/sky2 copy.png')
    app.skyImage = app.scaleImage(app.skyImage, 0.73) # rescale

    
    
    ########### CREATING ALL THE BUTTONS WE NEED #####################
      # Button to competitive
    app.buttonToCompetitive = Button('Set Goal', 0.85, app,
                                     'white', 'blue', 'blue')
    app.buttonToCompetitive.setSize(1.5*app.width/8, app.height/1.3,
                                    3.6*app.width/8, 1.2*app.height/1.3)

      # Button to follow
    app.buttonToFollow = Button('Adaptive', 0.4, app,
                                'white', 'blue', 'blue')
    app.buttonToFollow.setSize(4.5*app.width/8, app.height/1.3,
                               6.5*app.width/8, 1.2*app.height/1.3)
    
      # Button to back
    app.backButton = Button('BACK', 0.2, app, 'white', 'blue', 'blue')
    app.backButton.setSize(0.87*app.width, 0.90*app.height,
                           0.97*app.width, 0.96*app.height)
      # Button intermediate to competitive
    app.intermediateToCompetitive = Button('NEXT', 0.2, app, 'white', 'blue', 'blue')
    app.intermediateToCompetitive.setSize(0.87*app.width, 0.90*app.height,
                                          0.97*app.width, 0.96*app.height)

    # Button instructions to start
    app.instructionsToStart = Button('NEXT', 0.2, app, 'white', 'blue', 'blue')
    app.instructionsToStart.setSize(0.88*app.width, 0.91*app.height,
                                    0.98*app.width, 0.97*app.height)

      
    ##################################################################

    
    
    ########### CREATING ALL THE COUNTERS WE NEED #####################
      # Pace Counter
    app.paceCounter = Counter('Pace: ', 1, 'black', 'lightblue', app, 0.42, '')
    app.paceCounter.setSize((app.width/2) - 100, 0.5*app.height/20,
                            (app.width/2) + 100, 0.5*1.5*app.height/12)    

      # Distance Counter
    app.distanceCounter = Counter('Distance: ', 0, 'lightblue', rgbString(0, 0, 100), app, 0.34, 'm')
    app.distanceCounter.setSize(6.5*app.width/20, 1.4*app.height/18,
                                10*app.width/20, 2*app.height/18)    

      # Time Counter
    app.timeCounter = Counter('Time: ', 100, 'lightblue', rgbString(0, 0, 100), app, 0.23, 's')
    app.timeCounter.setSize(10.3*app.width/20, 1.4*app.height/18,
                            12.8*app.width/20, 2*app.height/18)

    # Score Counter
    app.scoreCounter = Counter('Score: ', 0, 'lightblue', rgbString(0, 0, 100), app, 0.27, '')
    app.scoreCounter.setSize(9*app.width/20, 2.2*app.height/18,
                            11*app.width/20, 2.8*app.height/18)
    
    ##################################################################


    ################### CREATING ALL THE TEXTBOXES ##################
    app.distanceTextBox = TextBox(app, "Distance goal (meters) : ", 0.45, 'blue', 'black')
    app.distanceTextBox.setSize(0.1*app.width, 0.28*app.height,
                                0.9*app.width, 0.38*app.height)

    
    app.timeTextBox = TextBox(app, "Time goal (minutes) : ", 0.45, 'blue', 'black')
    app.timeTextBox.setSize(0.1*app.width, 0.48*app.height,
                            0.9*app.width, 0.58*app.height)

    app.heightTextBox = TextBox(app, "Height (meters) : ", 0.5, 'blue', 'black')
    app.heightTextBox.setSize(0.1*app.width, 0.68*app.height,
                              0.9*app.width, 0.78*app.height)

    ################################################################



    # CREATING 3D GRAPHICS
    # Creating road
    app.road = Road(app, 'gray', 'yellow')
    app.road.setSize(-0.05*app.width, 1.2*app.height,
                     1.05*app.width, 1.2*app.height)

    # Creating building class
    app.leftBuildings = LeftBuildings(app)
    app.rightBuildings = RightBuildings(app)

    # Setting up color for floor of floor next to road
    # Citation: getpixel code obtained from 112 notes
    app.rgbForm = app.skyImage.convert('RGB')
    # app.r, app.g, app.b = app.rgbForm.getpixel((550, 580))
    app.r, app.g, app.b = app.rgbForm.getpixel((900, 380))


    # Create Arms
    # Creating right Arm
    # ORIGINAL ARM
    app.rightArmUp = Arm(app,
                   700, 600,
                   790, 620,
                   850, app.height,                       
                   750, app.height,
                       
                   700, app.height,
                   670, 650)

    app.rightArmDown = Arm(app,
                   700, 700,
                   790, 720,
                   850, app.height,                       
                   750, app.height,
                       
                   700, app.height,
                   670, 750)

    # creating symmetry with right arm
    app.leftArmUp = Arm(app,
                   (app.width/2)-(700-(app.width/2)), 600,
                   (app.width/2)-(790-(app.width/2)), 620,
                   (app.width/2)-(850-(app.width/2)), app.height,                       
                   (app.width/2)-(750-(app.width/2)), app.height,
                       
                   (app.width/2)-(700-(app.width/2)), app.height,
                   (app.width/2)-(670-(app.width/2)), 650)


    app.leftArmDown = Arm(app,
                   (app.width/2)-(700-(app.width/2)), 700,
                   (app.width/2)-(790-(app.width/2)), 720,
                   (app.width/2)-(850-(app.width/2)), app.height,                       
                   (app.width/2)-(750-(app.width/2)), app.height,
                       
                   (app.width/2)-(700-(app.width/2)), app.height,
                   (app.width/2)-(670-(app.width/2)), 750)

    # By default, we set right arm to be up and left arm down
    app.currentRightArm = app.rightArmUp
    app.currentLeftArm = app.leftArmDown
    

    # # Creating coins
    app.COINS = AllCoins(app)
    app.coinIndex = 0
    app.currentCoin = app.COINS.coins[app.coinIndex]

                
    
runApp(width = 1160, height = 800)
