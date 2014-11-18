import fileParse
from myro import *

def mainColour(colours, tolerance):
    
    totalR = 0
    totalG = 0
    totalB = 0
    
    for i in range(0, len(colours)):
        totalR += colours[i][0]
        totalG += colours[i][1] 
        totalB += colours[i][2]
    
    avgR = totalR / len(colours)
    avgG = totalG / len(colours)
    avgB = totalB / len(colours) #now, all avg values of R, G, B known

    mainR = 0
    mainG = 0
    mainB = 0

    colourCounter = 0

    for i in range(0, len(colours)):
        
        if(abs(colours[i][0] - avgR) <= tolerance and abs(colours[i][1] - avgG) <= tolerance and abs(colours[i][2] - avgB) <= tolerance):
        
            mainR += colours[i][0]
            mainG += colours[i][1]
            mainB += colours[i][2]
            
            colourCounter += 1                  #only consider colours if their averages are within the "tolerance"

    avgMainR = mainR / colourCounter
    avgMainG = mainG / colourCounter
    avgMainB = mainB / colourCounter            #find average RGB values of non-outlying pixels
    
    avgMainColours = [avgMainR, avgMainG, avgMainB]
    
    return avgMainColours                      #return average colours

def shoeRecord(name):
    
    picture = takePicture()
    tolerance = 20
    
    colours = []

    for x in range (500, 650, 10): #every 10 pixels from 500 to 650 pixels
        
        for y in range(200, 300, 10): #every 10 pixels from 200 to 300 pixels
        
            pixel = getPixel(picture, x, y) 
            pixelColour = getRGB(pixel)
            
            colours.append(pixelColour) #add pixel colour to list of colours


    fileParse.addShoe(name, str(mainColour(colours, tolerance))) #return the 'main' colour, which will be used to identify burglars
    
    return
    