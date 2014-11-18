from myro import *
import functions

tolerance = 300

def blocked():
    return (getObstacle()[0] >= tolerance)

print("Started")

functions.moveUntilBlocked(0.2, 500) #move forward until an obstacle sensor reaches 500

while(blocked()):
    functions.turn(10)            #the robot will keep turning right until it becomes parallel with the box
    
functions.turn(50)                 #an additional little turn to avoid collisions with the box; now the robot should be parallel with the box's side 

timeOffCourse = 0
i = 0

for i in range(0, 2):             #go through the 'turn left when safe to do so' process twice

    turnBlocked = True            #assume turn is blocked

    while(turnBlocked):
        
        if(i == 0):
            timeOffCourse += 1      #if going laterally, add time spent going the other way later
        
        functions.moveForward(0.7, 1)   #move forward slightly
        functions.turn(-90)             #turn left  
        
        if(not(blocked())):
            functions.turn(-45)         #if unblocked, turn left to face the box more
            
            if(not(blocked())):         
                turnBlocked = False  
                functions.turn(45)      #if still unblocked, undo 45 degree turn and move forward
            else:
                functions.turn(135)     #if blocked, undo 90 and 45 degree turn
            
        else:
            functions.turn(90)          #if blocked, undo 90 degree turn
    

functions.moveForward(0.7, timeOffCourse)  #move amount displaced laterally

functions.turn(90)                          #turn right

functions.moveForward(1, 1)                  #robot has avoided obstacle, and can now celebrate by moving forward

print("Done")

