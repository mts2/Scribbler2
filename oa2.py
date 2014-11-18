from myro import *
import functions

print("Started")

def blocked():
       return (getObstacle()[0] > 1000)

functions.moveUntilBlocked(0.4, 1000)

r = 87

functions.turn(88)

slopeUp = False

if(blocked() == True):
       slopeUp = True

turnTolerance = 900

max = 20
sidesTraversed = 0
actions = 0

while(sidesTraversed != 3):
       
       if(sidesTraversed != 2):
       
              if(slopeUp == True):
                  clearanceTest = functions.limitedMoveUntilBlocked(0.4, turnTolerance, 20)
                  if(clearanceTest == False):
                      functions.turn(r)
                      functions.moveForward(0.5, 0.5)
                      functions.turn(-90)
                      if(sidesTraversed == 0):
                            actions+=1
                  else:
                      functions.turn(-90)
                      sidesTraversed += 1
                  
              else: 
                  functions.turn(-90)
                  clearanceTest = functions.limitedMoveUntilBlocked(0.4, turnTolerance, 20)
                  if(clearanceTest == False):
                      functions.turn(r)
                      functions.moveForward(0.5, 0.5)
                      if(sidesTraversed == 0):
                            actions+=1
                  else:
                      sidesTraversed += 1
                      
       else:
              
              actions2 = 0
              
              while(actions2 < actions/4.0):
                     
                     if(slopeUp == True):
                            
                            functions.limitedMoveUntilBlocked(0.4, turnTolerance, 20)
                            functions.turn(r)
                            functions.moveForward(0.5, 0.5)
                            functions.turn(-90)
                            actions2+=1
                            
                     else:
                            
                            functions.turn(-90)
                            functions.limitedMoveUntilBlocked(0.4, turnTolerance, 20)
                            functions.turn(r)
                            functions.moveForward(0.5, 0.5)
                            actions2+=1
            
              sidesTraversed+=1

functions.turn(r)
functions.moveForward(1, 1)

print("Finished")