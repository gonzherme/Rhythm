def intermediateMode_redrawAll(app, canvas):
    # Main
    drawBackground(app, canvas, 'black')

    
    # Draw next button
    app.intermediateToCompetitive.draw(canvas)
    

    # Draw Title:
    canvas.create_text(app.width/2, app.height/10,
                       text = "Today's goals",
                       font = ("Comic Sans MS", 70, "bold"),
                       fill = 'lightgreen')

    canvas.create_text(app.width/2, 1.8*app.height/10,
                       text = "(Click on each category to type your info)",
                       font = ("Comic Sans MS", 30, "bold"),
                       fill = 'lightyellow')
    
    # Draw textBox for Goal Distance
    app.timeTextBox.draw(canvas)
    app.distanceTextBox.draw(canvas)
    app.heightTextBox.draw(canvas)




def intermediateMode_mousePressed(app, event):        
    # Go to competitive mode:
    app.intermediateToCompetitive.isPressed(event, app)

    if app.intermediateToCompetitive.pressed:
        transitionToCompetitive(app)

        
        
    # Input text if any of the text boxes are clicked
    app.distanceTextBox.isPressed(event, app)
    if app.distanceTextBox.pressed:
        time.sleep(0.1) # delay used to simulate button friction
        app.currentTextBox = app.distanceTextBox # creating an alias on purpose
        

    app.timeTextBox.isPressed(event, app)
    if app.timeTextBox.pressed:
        time.sleep(0.1) # delay used to simulate button friction
        app.currentTextBox = app.timeTextBox # creating an alias on purpose
        
    app.heightTextBox.isPressed(event, app)
    if app.heightTextBox.pressed:
        time.sleep(0.1) # delay used to simulate button friction
        app.currentTextBox = app.heightTextBox # creating an alias on purpose\



        
def intermediateMode_keyPressed(app, event):
    if event.key != 'Enter' and hasattr(app, 'currentTextBox'): # making sure app has currentTextBox attribute

        # Only allow digits: making sure user can't delete full text box
        if ( ( event.key in {'0','1','2','3','4','5','6','7','8','9'} 
               or event.key == '.' )
             and len(app.currentTextBox.text) < 31 ):
            app.currentTextBox.text += event.key

        # Delete
        elif ( (event.key == 'Delete' or event.key == 'BackSpace')
            and app.currentTextBox.text[-1] != ' ' ): 
            app.currentTextBox.text = app.currentTextBox.text[:-1]
