xCoordinate = random(400)
yCoordinate = random(400)
speed = 3
yspeed = 3

def setup():
    size(400, 400)
    background(0, 0, 0)
def draw():
    global xCoordinate, speed, yCoordinate, yspeed
    background(0)
    
    fill(255)
    xCoordinate += speed
    yCoordinate += yspeed

    
    if xCoordinate >= 385 or xCoordinate <= 15:
        speed= -speed
    if yCoordinate >= 385 or yCoordinate <= 15:
        yspeed= -yspeed
    ellipse(xCoordinate, yCoordinate, 30, 30)
