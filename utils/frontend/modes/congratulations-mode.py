def congratulationsMode_redrawAll(app, canvas):
    # Main
    drawBackground(app, canvas, 'black')
    app.backButton.draw(canvas)


    # Draw congratulations background
    drawRoundedRectangle(0.1*app.width + 30, 0.21*app.height + 10,
                         0.86*app.width + 10, 0.8*app.height + 10,
                         'darkblue', 10, canvas)

    drawRoundedRectangle(0.1*app.width +20, 0.21*app.height - 10,
                         0.86*app.width - 10, 0.8*app.height - 10,
                         'blue', 10, canvas)
    
    # Draw Title:
    canvas.create_text(app.width/2, app.height/2,
                       text = 'Congratulations!!! \n  You achieved \n    your goal!',
                       font = ("Comic Sans MS", 70, "bold"),
                       fill = 'white')


def congratulationsMode_mousePressed(app, event):        
    # If back button pressed:
    app.backButton.isPressed(event, app)
    if app.backButton.pressed:
        time.sleep(0.1) # delay used to simulate button friction
        app.mode = 'startMode'
        app.timerDelay = 20

        # stop playing song
        app.playlist[app.c].stop()
