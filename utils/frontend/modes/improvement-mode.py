def improvementMode_redrawAll(app, canvas):
    # Main
    drawBackground(app, canvas, 'black')
    app.backButton.draw(canvas)


    # Draw improvement background
    drawRoundedRectangle(0.1*app.width + 30, 0.21*app.height + 10,
                         0.86*app.width + 10, 0.8*app.height + 10,
                         'red', 10, canvas)

    drawRoundedRectangle(0.1*app.width +20, 0.21*app.height - 10,
                         0.86*app.width - 10, 0.8*app.height - 10,
                         'orange', 10, canvas)

    
    # Draw Title:
    canvas.create_text(app.width/2, app.height/2,
                       text = "You didn't make your goal! \n    But don't give up! \n   Keep working at it!",
                       font = ("Comic Sans MS", 60, "bold"),
                       fill = 'white')



def improvementMode_mousePressed(app, event):        
    # If back button pressed:
    app.backButton.isPressed(event, app)
    if app.backButton.pressed:
        time.sleep(0.1) # delay used to simulate button friction
        app.mode = 'startMode'
        app.timerDelay = 20

        # stop playing
        app.playlist[app.c].stop()
