from myro import *
import functions

def printSensorVals():
    print(getObstacle())

def noObstacle():
    
    tolerance = 700
    
    if(getObstacle()[0] < tolerance and getObstacle()[1] < tolerance and getObstacle()[2] < tolerance):
        return True
    else:
        return False

setName("OG_Loc")

print("Started")

functions.moveUntilBlocked(1, 800)
blocked = True

stepTime = 0.5
timeOffCourse = 0;

while(blocked == True):
    functions.turn(90)
    functions.moveForward(1, stepTime)
    functions.turn(-90)
    
    timeOffCourse += stepTime
    
    printSensorVals()
    
    if(noObstacle()):
        functions.turn(-45)
        printSensorVals()
        if(noObstacle()):
            blocked = False
        functions.turn(45)

functions.moveForward(1, 2)
functions.turn(-90)

blocked = True

while(blocked == True):
    functions.turn(90)
    functions.moveForward(1, stepTime)
    functions.turn(-90)
    
    if(noObstacle()):
        functions.turn(-45)
        if(noObstacle()):
            blocked = False
        functions.turn(45)

functions.moveForward(1, timeOffCourse)
functions.turn(90)

functions.moveForward(1, 1)
stop()

print("Finished")