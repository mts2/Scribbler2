from myro import *
import fileParse

def compare(pixel, colour, tolerance):
    
    comparedR = colour[0]
    comparedG = colour[1]
    comparedB = colour[2]
    
    realColours = getRGB(pixel)
    
    realR = realColours[0]
    realG = realColours[1]
    realB = realColours[2]
    
    return (abs(realR - int(comparedR)) < tolerance and abs(realG - int(comparedG)) < tolerance and abs(realB - int(comparedB)) < tolerance)   
    
def checkForShoe(picture, origX, origY, colour, tolerance):
    
    notShoePixels = 0   #to add up number of non-matching pixels
    badPixelTolerance = 100 #total non-matching pixels allowed
    
    comparisonR = colour[0]
    comparisonG = colour[1]
    comparisonB = colour[2]
    
    for x in range(origX, origX+100, 5):
         
        for y in range(origY, origY+100, 5):                 #check 20x20 pixel square
            
            pixel = getPixel(picture, x, y)
            
            pictureColour = getRGB(pixel)
            
            pictureR = pictureColour[0]
            pictureG = pictureColour[1]
            pictureB = pictureColour[2]
            
            if(abs(int(comparisonR) - int(pictureR)) > tolerance or abs(int(comparisonG) - int(pictureG)) > tolerance or abs(int(comparisonB) - int(pictureB)) > tolerance):
                #if pixel colour does not match shoe, increment the counter for non-matching pixels
                notShoePixels+=1
    
            if(notShoePixels > badPixelTolerance): #if tolerance exceeded, no shoe
                return False
    
    return True  #if tolerance not exceeded by end, shoe exists
    

def parseImage(picture, colours, increment):
    
    matchingColour = False #default matching colour to false
    
    shoeFound = False #assume no shoe found
    
    for x in range(500, 800, increment):
        
        if(shoeFound == True):
            break                 #break out of loop if shoe priorly found
        
        for y in range(200, 400, increment):
            
            pixel = getPixel(picture, x, y) #take pixel
            
            for i in range (0, len(colours)): #compare pixel colours for each colour
                
                colour = colours[i]
                tolerance = 100
                
                if(compare(pixel, colour, tolerance) == True):
                    
                    tolerance = 50
                    
                    if(checkForShoe(picture, x, y, colour, tolerance) == True):
                        shoeFound = True                                         #allows for loop to be broken
                        matchingColour = colour                                   #colour to return
                    
                
            if(shoeFound == True):
                break                                                           #break out of loop if shoe has been found (and then break again to exit parent loop)
                
    return matchingColour #returns colour match, or otherwise returns false