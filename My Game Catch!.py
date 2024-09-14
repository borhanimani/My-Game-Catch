from graphics import *
import time
import random

#Window-----------------

gameScreen = GraphWin("Catch",600,600)
gameScreen.setBackground("light green")

#Game Variables

highScore = 0
gameLife = 3
boxLocation = 1
shapeLocation = 1
shapeType = 1
mouseX = 50
mouseY = 50
myTime = 0.01
sub = 0.001


#Box Functions-------------------


def drawbox(Location):
    global box
    box.undraw()
    x = Location
    boxPoints=[Point(x,430),Point((x+5),430),Point((x+5),438),Point((x+65),438),Point((x+65),430),Point((x+70),430),Point((x+70),445),Point(x,445)]
    box = Polygon(boxPoints)
    box.draw(gameScreen)
    box.setFill("brown")

def setBoxLocation(event):
    global mouseX
    global mouseY
    global mouse
    global boxLocation
    mouseX = event.x
    mouseY = event.y
    if (50 <= mouseX <137.5) and (460<mouseY<550):
        boxLocation = 1
        drawbox(65)
    elif (137.5 <= mouseX <225) and (460<mouseY<550):
        boxLocation = 2
        drawbox(145)
    elif (225 <= mouseX <312.5) and (460<mouseY<550):
        boxLocation = 3
        drawbox(225)
    elif (312.5 <= mouseX <=400) and (460<mouseY<550):
        boxLocation = 4
        drawbox(310)

def checkMouseCor():
    mouse = gameScreen.bind('<Motion>',setBoxLocation)

#shapes-----------------

def drawSquare(position):
    checkMouseCor()
    x=position
    y=50
    squarePoints=[Point(x,y),Point((x+10),y),Point((x+10),(y + 10)),Point(x,(y + 10))]
    square=Polygon(squarePoints)
    square.draw(gameScreen)
    square.setFill("green")
    for i in range(0,350):
        checkMouseCor()
        time.sleep(myTime)
        y += 1
        square.undraw()
        squarePoints=[Point(x,y),Point((x+30),y),Point((x+30),(y + 30)),Point(x,(y + 30))]
        square=Polygon(squarePoints)
        square.draw(gameScreen)
        square.setFill("green")
    square.undraw()

def drawTriangle(position):
    checkMouseCor()
    x=position + 15
    y=50
    trianglePoints=[Point(x,y),Point((x+10),y),Point(x,(y + 10))]
    triangle=Polygon(trianglePoints)
    triangle.draw(gameScreen)
    triangle.setFill("blue")
    for i in range(0,350):
        checkMouseCor()
        time.sleep(myTime)
        y += 1
        triangle.undraw()
        trianglePoints=[Point(x,y),Point((x+15),(y+30)),Point((x-15),(y + 30))]
        triangle=Polygon(trianglePoints)
        triangle.draw(gameScreen)
        triangle.setFill("Blue")
    triangle.undraw()

def drawCircle(position):
    checkMouseCor()
    x=position + 15
    y=65
    cirle=Circle(Point(x,y),15)
    cirle.draw(gameScreen)
    cirle.setFill("orange")
    for i in range(0,350):
        checkMouseCor()
        time.sleep(myTime)
        y += 1
        cirle.undraw()
        cirle=Circle(Point(x,y),15)
        cirle.draw(gameScreen)
        cirle.setFill("orange")
    cirle.undraw()


def drawShape(location, shpType):
    if shpType == 1:
        drawSquare(location)
    elif shpType == 2:
        drawTriangle(location)
    else:
        drawCircle(location)

def drawIntendedShape(shpType):
    global square
    global triangle
    global circle
    circle.undraw() 
    square.undraw() 
    triangle.undraw()
    if shpType == 1:
        squarePoints=[Point(465,100),Point((465+40),100),Point((465+40),(100 + 40)),Point(465,(100 + 40))]
        square=Polygon(squarePoints)
        square.draw(gameScreen)
        square.setFill("green")
    elif shpType == 2:
        trianglePoints=[Point(485,100),Point((485+20),(100+40)),Point((485-20),(100 + 40))]
        triangle=Polygon(trianglePoints)
        triangle.draw(gameScreen)
        triangle.setFill("Blue")
    else:
        circle=Circle(Point(485,120),20)
        circle.draw(gameScreen)
        circle.setFill("orange")
       

#Game Screen-----------------

gameBoardPoints=[Point(50,50),Point(400,50),Point(400,450),Point(50,450)]
boardPolygon=Polygon(gameBoardPoints)
boardPolygon.draw(gameScreen)
boardPolygon.setFill("white")

shapeBoardPoints=[Point(420,50),Point(550,50),Point(550,170),Point(420,170)]
shapeBoardPolygon=Polygon(shapeBoardPoints)
shapeBoardPolygon.draw(gameScreen)
shapeBoardPolygon.setFill("light yellow")

lifePrinterBoardPoints=[Point(420,190),Point(550,190),Point(550,310),Point(420,310)]
lifeboardPolygon=Polygon(lifePrinterBoardPoints)
lifeboardPolygon.draw(gameScreen) 
lifeboardPolygon.setFill("light yellow")

HighScorePrinterBoardPoints=[Point(420,330),Point(550,330),Point(550,450),Point(420,450)]
HighScoreboardPolygon=Polygon(HighScorePrinterBoardPoints)
HighScoreboardPolygon.draw(gameScreen)
HighScoreboardPolygon.setFill("light yellow")

catchShapeLabel=Text(Point(485,75),"Catch!")
catchShapeLabel.draw(gameScreen)
shapeBoardLine=Polygon(Point(425,90),Point(545,90))
shapeBoardLine.draw(gameScreen)

lifeLabel=Text(Point(485,215),"Life")
lifeLabel.draw(gameScreen)
lifeText=Text(Point(485,270),gameLife)
lifeText.draw(gameScreen)
LifeBoardLine=Polygon(Point(425,230),Point(545,230))
LifeBoardLine.draw(gameScreen)

HighScoreLabel=Text(Point(485,355),"Score")
HighScoreLabel.draw(gameScreen)
highScoreText=Text(Point(485,400),highScore)
highScoreText.draw(gameScreen)
HighScoreLine=Polygon(Point(425,370),Point(545,370))
HighScoreLine.draw(gameScreen)

controlPadPoints=[Point(50,460),Point(400,460),Point(400,550),Point(50,550)]
controlPad=Polygon(controlPadPoints)
controlPad.draw(gameScreen)
controlPad.setFill("light grey")

controlPadLine1Points = [Point(137,470),Point(137,540)]
controlPadLine1=Polygon(controlPadLine1Points)
controlPadLine1.draw(gameScreen)

controlPadLine2Points =[Point(225,470),Point(225,540)]
controlPadLine2=Polygon(controlPadLine2Points)
controlPadLine2.draw(gameScreen)

controlPadLine3Points =[Point(312,470),Point(312,540)]
controlPadLine3=Polygon(controlPadLine3Points)
controlPadLine3.draw(gameScreen)

x = 65
boxPoints=[Point(x,430),Point((x+5),430),Point((x+5),438),Point((x+65),438),Point((x+65),430),Point((x+70),430),Point((x+70),445),Point(x,445)]
box = Polygon(boxPoints)
box.draw(gameScreen)
box.setFill("brown")

circle=Circle(Point(485,120),20)
circle.draw(gameScreen)

squarePoints=[Point(465,100),Point((465+40),100),Point((465+40),(100 + 40)),Point(465,(100 + 40))]
square=Polygon(squarePoints)
square.draw(gameScreen)

trianglePoints=[Point(485,100),Point((485+20),(100+40)),Point((485-20),(100 + 40))]
triangle=Polygon(trianglePoints)
triangle.draw(gameScreen)

#Game Functions----------------------------------------------------

def getRandomNumber(x,y):
    return int(random.randrange(x,y))

def timeMangament(i):
    global myTime
    global sub
    if i == 36:
        sub = 0.00005
    if myTime <= 0.0008:
        myTime = 0.0008
    elif (i % 4 == 0):
        myTime -= sub
    
def setLife():
    global lifeText
    lifeText.undraw()
    lifeText=Text(Point(485,270),gameLife)
    lifeText.draw(gameScreen)

def setHighScore():
    global highScoreText
    highScoreText.undraw()
    highScoreText=Text(Point(485,400),highScore)
    highScoreText.draw(gameScreen)
    
#Game------------------
    
i=0
while gameLife > 0:
    i+=1
    shapeLocation = getRandomNumber(1,5)
    shapeType = getRandomNumber(1,4)
    intendedShapeType = getRandomNumber(1,4)
    drawIntendedShape(intendedShapeType)
    if shapeLocation == 1:
        drawShape(85,shapeType)
    elif shapeLocation == 2:
        drawShape(166,shapeType)
    elif shapeLocation == 3:
        drawShape(247,shapeType)
    else:
        drawShape(333,shapeType)
        
    if (intendedShapeType == shapeType) and (shapeLocation == boxLocation):
        highScore += 5
    elif(intendedShapeType == shapeType) and (shapeLocation != boxLocation):
        gameLife -= 1
    elif(intendedShapeType != shapeType) and (shapeLocation == boxLocation):
        gameLife -= 1
    timeMangament(i)
    setLife()
    setHighScore()

box.undraw()
highScoreText.undraw()
lifeText.undraw()
motivationalMessage=""
if highScore <= 10:
    motivationalMessage="You can try better!"
elif highScore <= 40:
    motivationalMessage="Good!"
elif highScore <= 80:
    motivationalMessage="Great!"
elif highScore <= 120:
    motivationalMessage="Ausome!"
elif highScore <= 170 :
    motivationalMessage="You'r star!"
elif highScore > 170 :
    motivationalMessage="You'r genius!"
highScoreText=Text(Point(225,250),motivationalMessage+"\n \n your score: "+str(highScore))
highScoreText.draw(gameScreen)
gameScreen.mainloop()

