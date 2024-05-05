# * START MODE
# ** Drawing
def startMode_redrawAll(app, canvas):

    drawBackground(app, canvas, 'black')
    # Title
    canvas.create_text(app.width/2, app.height/8,
                       text = 'rhythm',
                       font = ("Comic Sans MS", 130, "bold"),
                       fill = 'lightblue')


    # Draw competitive button background
    drawRoundedRectangle(1.5*app.width/8 + 15, app.height/1.3 + 10,
                         3.6*app.width/8 + 15, 1.2*app.height/1.3 + 10,
                         'lightblue', 10, canvas)

    
    # Draw to competitive button
    app.buttonToCompetitive.draw(canvas)


    # Draw to follow button background
    drawRoundedRectangle(4.5*app.width/8 + 15, app.height/1.3 + 10,
                         6.5*app.width/8 + 15, 1.2*app.height/1.3 + 10,
                         'lightblue', 10, canvas)
    
    # Draw to follow button
    app.buttonToFollow.draw(canvas)


    # Draw NCS gif
    photoImage = app.spritePhotoImages[app.spriteCounter]
    # photoImage = app.scaleImage(photoImage, 0.5)
    canvas.create_image(app.width/2, 1.015*app.height/2, image=photoImage)

# ** Helpers
def startMode_mousePressed(app, event):
    # Go to competitive mode
    app.buttonToCompetitive.isPressed(event, app)
    if app.buttonToCompetitive.pressed:
        time.sleep(0.1) # delay used to simulate button friction
        # play /images/buttonClicked.wav
        app.mode = 'intermediateMode'
        app.timerDelay = 1000

    # Go to followMode
    app.buttonToFollow.isPressed(event, app)
    if app.buttonToFollow.pressed:
        time.sleep(0.1) # delay used to simulate button friction

        # reset values
        app.scoreCounter.value = 0
        app.mode = 'intermediateFollowMode'


        

def startMode_timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.spritePhotoImages)
