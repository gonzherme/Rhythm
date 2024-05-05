from cmu_112_graphics import *
from tkinter import *
from backend import *
from random import randint, shuffle
from PIL import Image, ImageTk, ImageSequence
from objects import *
import time

# * BACKGROUND
def drawBackground(app, canvas, fill):
    canvas.create_rectangle(app.margin, app.margin,
                            app.width - app.margin,
                            app.height - app.margin,
                            fill = fill, outline = 'black',
                            width = 25)




# * DRAW USER MESSAGE
def drawUserMessage(app, canvas):               
    if app.on_track:
        canvas.create_text(app.width/2, app.height/3,
                           text = app.currentOnTrackMessage,
                           font = ("Comic Sans MS", 80, "bold"),
                           fill = 'lightgreen')

    elif not app.on_track:
        canvas.create_text(app.width/2, app.height/3,
                           text = app.currentOffTrackMessage,
                           font = ("Comic Sans MS", 90, "bold"),
                           fill = 'red') 
        
            
        



# * DRAW RECTANGLE
def drawRoundedRectangle(x0, y0, x1, y1, fill, r, canvas):
        # Inner rectangle
        canvas.create_rectangle(x0, y0,
                                x1, y1,
                                fill = fill, outline = fill,
                                width = 0)

        # Vertical outer rectangle
        canvas.create_rectangle(x0, y0 - r,
                                x1, y1 + (r+1),
                                fill = fill, outline = fill,
                                width = 0)

        # Horizontal outer rectangle
        canvas.create_rectangle(x0 - r, y0,
                                x1 + (r+1), y1,
                                fill = fill, outline = fill,
                                width = 0)
        
        
        # Draw round corners to smoothen out
        # Top left oval
        canvas.create_oval(x0 + r, y0 + r,
                           x0 - r, y0 - r,
                           fill = fill, outline = fill)

        # Bottom right oval
        canvas.create_oval(x1 + r, y1 + r,
                           x1 - r, y1 - r,
                           fill = fill, outline = fill)
        # Bottom left oval
        canvas.create_oval(x0 + r, y1 + r,
                           x0 - r, y1 - r,
                           fill = fill, outline = fill)
        
        # Top right oval
        canvas.create_oval(x1 + r, y0 + r,
                           x1 - r, y0 - r,
                           fill = fill, outline = fill)

    
