from math import sqrt
from random import randint
from backend import drawRoundedRectangle
######################### COUNTERS ##############################

# Button built basing upon the button presented in Mini-Lecture Advanced Tkinter
class Counter():
    def __init__(self, magnitude, initValue, textColour, fill, app, magnifier, unit):
        self.value = initValue
        self.magnitude = magnitude
        self.textColour = textColour
        self.fill = fill
        self.magnifier = magnifier
        self.unit = unit

        
    def setSize(self, topLeftX, topLeftY, bottomRightX, bottomRightY):  
        # corner point coordinates
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.bottomRightX = bottomRightX
        self.bottomRightY = bottomRightY

        # center points
        self.centerCounterX = int((self.topLeftX + self.bottomRightX)/2)
        self.centerCounterY = int((self.topLeftY + self.bottomRightY)/2)


        # font
        self.fontSize = int(0.55*self.magnifier*(self.centerCounterX/5))


           
        
    def draw(self, canvas):            
        # Draw rectangle
        canvas.create_rectangle(self.topLeftX, self.topLeftY,
                                self.bottomRightX, self.bottomRightY,
                                fill = self.fill)
        # Draw text
        canvas.create_text(self.centerCounterX, self.centerCounterY,
                           text = self.magnitude + f'{self.value} {self.unit}',
                           fill = self.textColour,
                           font = ("Comic Sans MS", self.fontSize, "bold"))

#######################################################################






######################### BUTTONS ####################################

# Button built basing upon the button presented in Mini-Lecture Advanced Tkinter
class Button():
    def __init__(self, name, buttonNum, app, textColour, fill,
                 outlineColor):
        self.name = name
        self.buttonNum = buttonNum
        self.text = name
        self.pressed = False
        self.fill = fill
        self.textColour = textColour
        self.outline = outlineColor

        
    def setSize(self, topLeftX, topLeftY, bottomRightX, bottomRightY):  
        # corner point coordinates
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.bottomRightX = bottomRightX
        self.bottomRightY = bottomRightY

        # center points
        self.centerButtonX = int((self.topLeftX + self.bottomRightX)/2)
        self.centerButtonY = int((self.topLeftY + self.bottomRightY)/2)


        # font
        self.fontSize = int(0.76*self.buttonNum*(self.centerButtonX/5))


    def isPressed(self, event, app):
        # Button Changing State
        if (self.topLeftX < event.x < self.bottomRightX and
            self.topLeftY < event.y < self.bottomRightY):
            self.pressed = True
            # self.fill = 'gray'

        else:
            self.pressed = False
            # self.fill = self.fill

           
    # Citation: geometric intuition to round rectangle: https://mathworld.wolfram.com/RoundedRectangle.html     
    def draw(self, canvas):            

        r = 10

        # Inner rectangle
        canvas.create_rectangle(self.topLeftX, self.topLeftY,
                                self.bottomRightX, self.bottomRightY,
                                fill = self.fill, outline = self.outline,
                                width = 0)

        # Vertical outer rectangle
        canvas.create_rectangle(self.topLeftX, self.topLeftY - r,
                                self.bottomRightX, self.bottomRightY + (r+1),
                                fill = self.fill, outline = self.outline,
                                width = 0)

        # Horizontal outer rectangle
        canvas.create_rectangle(self.topLeftX - r, self.topLeftY,
                                self.bottomRightX + (r+1), self.bottomRightY,
                                fill = self.fill, outline = self.outline,
                                width = 0)
        
        
        # Draw round corners to smoothen out
        # Top left oval
        canvas.create_oval(self.topLeftX + r, self.topLeftY + r,
                           self.topLeftX - r, self.topLeftY - r,
                           fill = 'blue', outline = 'blue')

        # Bottom right oval
        canvas.create_oval(self.bottomRightX + r, self.bottomRightY + r,
                           self.bottomRightX - r, self.bottomRightY - r,
                           fill = 'blue', outline = 'blue')
        # Bottom left oval
        canvas.create_oval(self.topLeftX + r, self.bottomRightY + r,
                           self.topLeftX - r, self.bottomRightY - r,
                           fill = 'blue', outline = 'blue')
        
        # Top right oval
        canvas.create_oval(self.bottomRightX + r, self.topLeftY + r,
                           self.bottomRightX - r, self.topLeftY - r,
                           fill = 'blue', outline = 'blue')        

        
        # Draw text
        canvas.create_text(self.centerButtonX, self.centerButtonY,
                           text = self.text,
                           fill = self.textColour,
                           font = ("Comic Sans MS", self.fontSize, "bold"))


###########################################################################





######################### TEXT BOX ######################################
class TextBox(Button):        
    def __init__(self, app, text, proportion, textColour, fill):
        self.text = text + ' '
        self.proportion = proportion
        self.textColour = textColour
        self.fill = fill
        self.pressed = False

        
    def setSize(self, topLeftX, topLeftY, bottomRightX, bottomRightY):  
        # corner point coordinates
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.bottomRightX = bottomRightX
        self.bottomRightY = bottomRightY

        # center points
        self.centerButtonX = int((self.topLeftX + self.bottomRightX)/2)
        self.centerButtonY = int((self.topLeftY + self.bottomRightY)/2)


        # font
        self.fontSize = int(self.proportion*(self.centerButtonX/5))


    def isPressed(self, event, app):
        # Button Changing State
        if (self.topLeftX < event.x < self.bottomRightX and
            self.topLeftY < event.y < self.bottomRightY):
            self.pressed = True                            

        else:
            self.pressed = False

                   
    def draw(self, canvas):        
        # Draw rounded rectangle
        drawRoundedRectangle(self.topLeftX + 10, self.topLeftY + 10,
                             self.bottomRightX + 10, self.bottomRightY + 10,
                             'green', 10, canvas)
    
        drawRoundedRectangle(self.topLeftX, self.topLeftY,
                             self.bottomRightX, self.bottomRightY,
                             'lightgreen', 10, canvas)


        
        # Draw text
        canvas.create_text(self.centerButtonX, self.centerButtonY,
                           text = self.text,
                           fill = self.textColour,
                           font = ("Comic Sans MS", self.fontSize, "bold"))


###########################################################################        



########################## GRAPHICS CLASSES ###############################
class Road(): #make a polygon, like triangle-like!!! Not two lines
    def __init__(self, app, fill, outlineColor):
        self.fill = fill
        self.outlineColor = outlineColor

        # Create road dashes
        
        dash1 = roadDash(app, 'white', 'black',
                         300, 20, 40)
        dash2 = roadDash(app, 'white', 'black',
                         399.6349161704311, 30.0, 60)


        dash3 = roadDash(app, 'white', 'black',
                         574.2940469106561, 39.0, 78)
                                 
        self.roadDashes = [dash1, dash2, dash3]


    def setSize(self, bottomLeftX, bottomLeftY, bottomRightX, bottomRightY):
        self.bottomLeftX = bottomLeftX
        self.bottomLeftY = bottomLeftY
        self.bottomRightX = bottomRightX
        self.bottomRightY = bottomRightY



        
    def draw(self, app, canvas):
        # Draw road itself
        canvas.create_polygon(self.bottomLeftX, self.bottomLeftY,
                              app.cx, app.cy,
                              self.bottomRightX, self.bottomRightY,
                              outline = self.outlineColor,
                              fill = self.fill,
                              width = 15)


        # Draw each road dash
        for dash in self.roadDashes:
            dash.draw(app, canvas)

        
class roadDash():
    def __init__(self, app,
                 fill, outlineColor,
                 y, width, depth):
    
        self.fill = fill
        self.outlineColor = outlineColor
        self.w = width
        self.depth = depth
        self.y = y

        #Symmetry through verical middle axis
        self.x0 =  (app.width/2) + 0.5*self.w
        self.x3 = (app.width/2) - 0.5*self.w
        self.y0 = y
        self.y3 = y

        # Calculate 1 point line equation
        self.cm = (app.cy-self.y0)/(app.cx-self.x0) # m = \delta y/ \delta x
        self.cb = app.cy - (self.cm * app.cx)# b = (y - mx)        

        # Calculate points x1 and x2
        self.x1 = self.x0 + (self.depth/sqrt(1+(self.cm**2)))  # x1 = x0 + d/ sqrt(1+m^2)        
        self.y1  = (self.cm * self.x1) + self.cb # y = mx + b
        

        self.x2 = (app.width/2) - (self.x1 - app.width/2)
        self.y2 = self.y1
        
    
        
    def draw(self, app, canvas):
        # draw lines connecting both points
        canvas.create_polygon(self.x0, self.y0,
                              self.x1, self.y1,
                              self.x2, self.y2,
                              self.x3, self.y3,
                              outline = self.outlineColor,
                              fill = self.fill,
                              width = 0)
        


    def move(self, app, displacement):
        # for i in range(displacement):
        #     self.individualMove(app, 1)
        self.individualMove(app, displacement)

    def individualMove(self, app, displacement):
        # Readjust all variables to project forwards (look at math of projection in folder)
        #  We are projecting forwards now, instead of backwards
        nx0 = self.x0 + (displacement/sqrt(1 + (self.cm**2)))
        ny0 = (self.cm * nx0) + self.cb

        # Readjust object
        self.__init__(app, 'white', 'black',
                      ny0, self.w + displacement/8,
                      self.depth + displacement/6)

        # Check if building is out of canvas through point nx5
        # nx5 = nx0 + (1.01*self.depthLower/sqrt(1+(self.cm**2)))
        # ny5 = (self.cm * nx5) + self.cb
        if ny0 > app.height :
            #reset the building
            self.__init__(app, 'white', 'black',
                         300, 20, 40)

        
class LeftBuildings():
    def __init__(self, app):
        building1 = LeftBuilding(app, 120, 250, 40,
                          450, 340,
                          'gray', 'gray')
        building2 = LeftBuilding(app, 155.43075779608873, 368.17738360489403, 51.81025259869626, 361.5413570822535, 435.26315391141947, 'gray', 'gray')

        building3 = LeftBuilding(app, 231.41521836673112, 667.8805515148457, 77.13840612224375, 225.45113720879763, 581.8218522366799, 'gray', 'gray')

        self.buildings = [building1, building2, building3]

        
    def draw(self, app, canvas):
        for building in self.buildings:
            building.draw(app, canvas)
    
    def move(self, app, displacement):
        for building in self.buildings:
            building.move(app, displacement)


            
class LeftBuilding():
    def __init__(self, app, width, height, depth,
                 x0, y0,
                 fill, outlineColor):
        
        self.fill = fill
        self.outlineColor = outlineColor
        self.w = width
        self.h = height
        
        self.depthLower = depth
        self.depthHigher = 1.1*(self.depthLower)


        self.x0 = x0
        self.y0 = y0  


        self.x1 = self.x0
        self.y1 = self.y0 - self.h
       
        
        # CALCULATING POINTS
        #FACE OF BUILDING
        self.x3 = x0 - self.w 
        self.y3 = self.y0
        
        
        self.x2 = self.x3
        self.y2 = self.y1
       

        # Line equation for center point: y = mx + b
        self.cm = (app.cy-self.y0)/(app.cx-self.x0) # m = \delta y/ \delta x
        self.cb = app.cy - (self.cm * app.cx)# b = (y - mx)
        
        # Line equation for lower point: y = mx + b
        self.lm = (app.ly-self.y1)/(app.lx-self.x1)
        self.lb = app.ly - (self.lm * app.lx)
        
        
        # RIGHT SIDE: create a function for this to make it neater
        self.x5 = self.x0 + (self.depthLower/sqrt(1+(self.cm**2)))  # x1 = x0 + d/ sqrt(1+m^2)        
        self.y5  = (self.cm * self.x5) + self.cb # y = mx + b

        
        self.x4 = self.x1 + (self.depthHigher/sqrt(1+(self.lm**2)))
        self.y4 = (self.lm * self.x4) + self.lb        


        
    def draw(self, app, canvas):
        
        canvas.create_polygon(self.x0, self.y0,
                              self.x3, self.y3,
                              self.x2, self.y2,
                              self.x1, self.y1,
                              outline = self.outlineColor,
                              fill = f'dark {self.fill}',
                              width = 0)

        
        canvas.create_polygon(self.x0, self.y0,
                              self.x1, self.y1,
                              self.x4, self.y4,
                              self.x5, self.y5,
                              outline = self.outlineColor,
                              fill = 'gray',
                              width = 0)



    def move(self, app, displacement):
        # Readjust all variables to project forwards (look at math of projection in folder)
        #  We are projecting forwards now, instead of backwards
        nx0 = self.x0 - (displacement/sqrt(1 + (self.cm**2)))
        ny0 = (self.cm * nx0) + self.cb

        # Account for closer objects
        self.__init__(app, self.w + 0.5,
                      self.h + 5, self.depthLower + 0.7,
                      nx0, ny0,
                      self.fill, self.outlineColor)

        # Check if building is out of canvas through point nx5
        nx5 = nx0 + (1.01*self.depthLower/sqrt(1+(self.cm**2))) 
        if nx5 < -30 :
            #reset the building
            self.__init__(app, 120, 250, 40,
                          450, 340,
                          'gray', 'gray')


class RightBuildings():
    def __init__(self, app):
        building1 = RightBuilding(app, 120, 250, 40,
                          710, 340,
                          'gray', 'gray')


        building2 = RightBuilding(app, 146.0, 510, 76.4,
                                  803.2218006133187, 440.3927083528047, 
                                  'gray', 'gray')

        self.buildings = [building1, building2]

        
    def draw(self, app, canvas):
        for building in self.buildings:
            building.draw(app, canvas)
    
    def move(self, app, displacement):
        for building in self.buildings:
            building.move(app, displacement)


            

class RightBuilding():
    def __init__(self, app, width, height, depth,
                 x0, y0,
                 fill, outlineColor):
        
        self.fill = fill
        self.outlineColor = outlineColor
        self.w = width
        self.h = height
        
        self.depthLower = depth
        self.depthHigher = 1.1*(self.depthLower)


        self.x0 = x0
        self.y0 = y0  
        # print(f'x0: {self.x0}, y0: {self.y0}')

        self.x1 = self.x0
        self.y1 = self.y0 - self.h
       
        
        # CALCULATING POINTS
        #FACE OF BUILDING
        self.x3 = x0 + self.w 
        self.y3 = self.y0
        
        
        self.x2 = self.x3
        self.y2 = self.y1
       

        # Line equation for center point: y = mx + b
        self.cm = (app.cy-self.y0)/(app.cx-self.x0) # m = \delta y/ \delta x
        self.cb = app.cy - (self.cm * app.cx)# b = (y - mx)
        
        # Line equation for lower point: y = mx + b
        self.lm = (app.ly-self.y1)/(app.lx-self.x1)
        self.lb = app.ly - (self.lm * app.lx)
        
        
        # RIGHT SIDE: create a function for this to make it neater
        self.x5 = self.x0 - (self.depthLower/sqrt(1+(self.cm**2)))  # x1 = x0 + d/ sqrt(1+m^2)        
        self.y5  = (self.cm * self.x5) + self.cb # y = mx + b

        
        self.x4 = self.x1 - (self.depthHigher/sqrt(1+(self.lm**2)))
        self.y4 = (self.lm * self.x4) + self.lb


        
    def draw(self, app, canvas):
        
        canvas.create_polygon(self.x0, self.y0,
                              self.x3, self.y3,
                              self.x2, self.y2,
                              self.x1, self.y1,
                              outline = self.outlineColor,
                              fill = f'dark {self.fill}',
                              width = 0)

        
        canvas.create_polygon(self.x0, self.y0,
                              self.x1, self.y1,
                              self.x4, self.y4,
                              self.x5, self.y5,
                              outline = self.outlineColor,
                              fill = f'{self.fill}',
                              width = 0)

        


    def move(self, app, displacement):
        # Readjust all variables to project forwards (look at math of projection in folder)
        #  We are projecting forwards now, instead of backwards
        nx0 = self.x0 + (displacement/sqrt(1 + (self.cm**2)))
        ny0 = (self.cm * nx0) + self.cb

        # Account for closer objects
        self.__init__(app, self.w + 0.5,
                      self.h + 5, self.depthLower + 0.7,
                      nx0, ny0,
                      self.fill, self.outlineColor)

        # Check if building is out of canvas through point nx5
        nx5 = nx0 - (1.01*self.depthLower/sqrt(1+(self.cm**2))) 
        if nx5 > 1.05*app.width :
            #reset the building
            self.__init__(app, 120, 250, 40,
                          710, 340,
                          'gray', 'gray')

            
        
class Arm():
    def __init__(self, app,
                 x0,y0,
                 x1, y1,
                 x2, y2,
                 x3, y3,
                 x4, y4,
                 x5, y5):
        self.x0, self.y0 = x0, y0
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        self.x4, self.y4 = x4, y4
        self.x5, self.y5 = x5, y5

        self.xi = [self.x0, self.x1, self.x2, self.x3, self.x4, self.x5]

    def draw(self, app, canvas):                
        canvas.create_polygon(self.xi[0], self.y0,
                              self.xi[1], self.y1,
                              self.xi[2], self.y2,
                              self.xi[3], self.y3,
                              outline = 'dark blue',
                              fill = f'pink',
                              width = 0)

        
        canvas.create_polygon(self.xi[0], self.y0,
                              self.xi[3], self.y3,
                              self.xi[4], self.y4,
                              self.xi[5], self.y5,
                              outline = 'dark blue',
                              fill = f'pink',
                              width = 0)




######################### COIN CLASS ################################

class AllCoins():
    def __init__(self, app):
        coinLeft = CoinLeft(app, 530, 300, 40)
        coinRight = CoinRight(app, 630, 300, 40)
        # coinRight = CoinRight(
        self.coins = [coinLeft, coinRight]
        
    
    def move(self, app, displacement):
        for coin in self.coins:
            coin.move(app, displacement)


    def resetCoins(self, app):
        if app.coinIndex == 0:
            app.currentCoin = self.coins[1]
            app.coinIndex = 1
        else:
            app.currentCoin = self.coins[0]
            app.coinIndex = 0

        # randomize color of coin        
        app.currentColor = app.colors[randint(0,len(app.colors)-1)]

        # reset coordinates of coins
        self.coins[0].__init__(app, 530, 300, 50)
        self.coins[1].__init__(app, 630, 300, 50)



class CoinLeft():
    def __init__(self, app, x0, y0, radius):
        self.x0 = x0
        self.y0 = y0  
        self.r = radius

        app.starting_x0 =  530
        app.starting_y0 = 300
        app.starting_r = 40
        
        self.fill = app.currentColor
        self.outlineColor = 'black'       

        # Line equation for center point: y = mx + b
        self.cm = (app.cy - self.y0)/(app.cx-self.x0) # m = \delta y/ \delta x
        self.cb = app.cy - (self.cm * app.cx)# b = (y - mx)    


            
    def draw(self, app, canvas):        
        canvas.create_oval(self.x0 + self.r, self.y0 + self.r,
                              self.x0 - self.r, self.y0 - self.r,
                              outline = self.outlineColor,
                              fill = self.fill,
                              width = 1)

            
    def move(self, app, displacement):
        # Readjust all variables to project forwards (look at math of projection in TP folder)
        #  We are projecting forwards the coin
        nx0 = self.x0 - (displacement/sqrt(1 + (self.cm**2)))
        ny0 = (self.cm * nx0) + self.cb

        # Account for coin being closer
        self.__init__(app, nx0, ny0, 1.01*self.r)

        # Check if coin is out of canvas through point nxy 
        if ny0 + 200 > app.height :
            # random coin
            self.__init__(app, 530, 300, 50)



    def inContact(self, arm):
        # if any two top points of arm within coin bounds 
        if ( (self.x0 - self.r) <= arm.x0 <= (self.x0 + self.r)  and  (self.y0 - self.r) < arm.y0 < (self.y0 + self.r) ):
            return True        
        else:
            return False
        


class CoinRight():
    def __init__(self, app, x0, y0, radius):
        self.x0 = x0
        self.y0 = y0  
        self.r = radius

        
        self.fill = app.currentColor
        self.outlineColor = 'black'       

        # Line equation for center point: y = mx + b
        self.cm = (app.cy - self.y0)/(app.cx-self.x0) # m = \delta y/ \delta x
        self.cb = app.cy - (self.cm * app.cx)# b = (y - mx)    


            
    def draw(self, app, canvas):        
        canvas.create_oval(self.x0 + self.r, self.y0 + self.r,
                              self.x0 - self.r, self.y0 - self.r,
                              outline = self.outlineColor,
                              fill = self.fill,
                              width = 1)

            
    def move(self, app, displacement):
        # Readjust all variables to project forwards (look at math of projection in TP folder)
        #  We are projecting forwards the coin
        nx0 = self.x0 + (displacement/sqrt(1 + (self.cm**2)))
        ny0 = (self.cm * nx0) + self.cb

        # Account for coin being closer
        self.__init__(app, nx0, ny0, 1.01*self.r)

        # Check if building is out of canvas through point nxy 
        if ny0 + 200 > app.height :
            # reset
            self.__init__(app, 630, 300, 40)



    def inContact(self, arm):
        # if any two top points of arm within coin bounds
        if ( (self.x0 - self.r) <= arm.xi[0] <= (self.x0 + self.r)
             and  (self.y0 - self.r) < arm.y0 < (self.y0 + self.r)
             or
            (self.x0 - self.r) <= arm.xi[1] <= (self.x0 + self.r)
             and  (self.y0 - self.r) < arm.y1 < (self.y0 + self.r)):
            return True
        
        else:
            return False




class CoinCenter(CoinLeft): # we only need to change 'move' function to move with respect to different line
    def __init__(self, app, x0, y0, radius):
        super().__init__(app, x0, y0, radius)

        # Line equation for center point: y = mx + b
        self.cm = (app.cy-self.y0)/(app.cx-self.x0) # m = \delta y/ \delta x
        self.cb = app.cy - (self.cm * app.cx)# b = (y - mx)    
                  

            
#####################################################################

