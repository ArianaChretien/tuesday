ellipsesize = 50
xCoordinate = random(400)
yCoordinate = random(400)
leftboundary = ellipsesize/2
rightboundary = 400-ellipsesize/2
top 
speed = 3
yspeed = 3

def setup():
    size(400, 400)
    background(0, 0, 0)
def draw():
    global xCoordinate, speed, yCoordinate, yspeed
    background(0)
    
    fill(0, 153, 220)
    xCoordinate += speed
    yCoordinate += yspeed

    
    if xCoordinate >= 385 or xCoordinate <= 15:
        speed= -speed
    if yCoordinate >= 385 or yCoordinate <= 15:
        yspeed= -yspeed
    ellipse(xCoordinate, yCoordinate, ellipsesize, ellipsesize)
