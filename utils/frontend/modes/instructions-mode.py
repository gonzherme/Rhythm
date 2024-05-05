def instructionsMode_redrawAll(app, canvas):
    # Main
    drawBackground(app, canvas, 'black')
    app.instructionsToStart.draw(canvas)


    
    # Draw Title:
    canvas.create_text(app.width/2, 0.1*app.height,
                       text = 'Welcome to Rhythm!',
                       font = ("Comic Sans MS", 80, "bold"),
                       fill = 'lightgreen')



    # Draw instructions background
    drawRoundedRectangle(0.1*app.width + 30, 0.21*app.height + 10,
                         0.92*app.width + 10, 0.85*app.height + 10,
                         'darkblue', 10, canvas)

    drawRoundedRectangle(0.1*app.width +20, 0.21*app.height - 10,
                         0.92*app.width - 10, 0.85*app.height - 10,
                         'blue', 10, canvas)
    
    # Draw instructions
    canvas.create_text(app.width/2, app.height/2,
                       text = app.instructions,
                       font = ("Comic Sans MS", 30, "bold"),
                       fill = 'lightgreen')




def instructionsMode_mousePressed(app, event):        
    # If back button pressed:
    app.instructionsToStart.isPressed(event, app)
    if app.instructionsToStart.pressed:
        time.sleep(0.1) # delay used to simulate button friction
        app.mode = 'startMode'
        app.timerDelay = 20
