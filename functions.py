from myro import *

def turn(degrees):
    
    if (degrees >= 0):
        motors(1, -1)
    elif (degrees < 0):
        motors(-1, 1)
    
    wait(abs(degrees/112.5))
    stop()

def moveUntilBlocked(speed, tolerance):

    while (getObstacle()[0] < tolerance):
        motors(speed, speed)

    stop()
    
def limitedMoveUntilBlocked(speed, tolerance, max):
    
    i = 0
    
    while (getObstacle()[0] < tolerance and i < max):
        motors(speed, speed)
        i+=1

    stop()

    if(i < max):
        return False
    else:
        return True

def moveForward(speed, time):
    
    motors(speed, speed)
    wait(time)
    
    stop()