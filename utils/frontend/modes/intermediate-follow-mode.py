def intermediateFollowMode_redrawAll(app, canvas):
    # Background
    drawBackground(app, canvas, 'black')

    # TITLE

    # Title background
    drawRoundedRectangle(0.2*app.width + 20, 0.6*app.height + 20,
                         0.8*app.width + 20, 0.8*app.height + 20,
                         'yellow', 10, canvas)
    
    drawRoundedRectangle(0.3*app.width, 0.05*app.height,
                         0.7*app.width, 0.2*app.height,
                         'blue', 10, canvas)
    
    # Title text
    canvas.create_text(app.width/2, 0.117*app.height,
                       text = 'Adaptive',
                       font = ("Comic Sans MS", 75, "bold"),
                       fill = 'white')
    
    
    # Instructions
    canvas.create_text(app.width/2.5, 0.35*app.height,
                       text = '''
                       1) Begin running by clicking the space bar
                       2) Rhythm will calculate and display your current pace
                       3) Click 'Enter' when you have found a pace you are
                       comfortable with''',
                       font = ("Comic Sans MS", 30, "bold"),
                       fill = 'lightgreen')


    
    # Clicks per second
    drawRoundedRectangle(0.2*app.width + 20, 0.6*app.height + 20,
                         0.8*app.width + 20, 0.8*app.height + 20,
                         'yellow', 10, canvas)
    
    drawRoundedRectangle(0.2*app.width, 0.6*app.height,
                             0.8*app.width, 0.8*app.height,
                             'lightyellow', 10, canvas)


        
    try: text = f'Live pace: {app.bpm_Tempo}'
    except: text = f'Live pace: 0'
    
    canvas.create_text(app.width/2, 0.7*app.height,
                       text = text,
                       font = ("Comic Sans MS", 75, "bold"),
                       fill = 'green')



        

def intermediateFollowMode_keyPressed(app, event):
    # Register
    if event.key == 'Space': app.bpm_Tempo = estimateClicks()

    # Stop tracking and start running
    elif event.key == 'Enter' or event.key == 'Return':
        transitionToFollowMode(app)
