from myro import *
import imageParse
import fileParse
import sendMail_avecImage

colourResults = []

def analyzeColours(colourResults, pictureString):
    
    print(colourResults)
    
    dictionary = fileParse.getInfo()

    uniqueColours = []
    countColours = []
    
    for x in colourResults:
	if(not(x in uniqueColours) and x != False):
	    uniqueColours.append(x)
    
    maxColourCount = 0
    maxColour = [0,0,0]
    
    for y in uniqueColours:
	colourCount = colourResults.count(y)
	if(colourCount > maxColourCount):
	    maxColour = y
    
    print(maxColour)
    
    for n, c in dictionary.iteritems():
	print(n)
	print(c)
	newColour = c[1:len(c)-1]
	newColours = newColour.split(", ")
	print(newColours)
	if(newColours == maxColour):
	     sendMail_avecImage.sendEmail(n, pictureString)
	     break;
    
    return

def follow():
    
    colours = fileParse.getArray()
    
    formattedColours = []
    
    for x in colours:
	newColour = x[1:len(x)-1]
	formattedColours.append(newColour.split(", "))

    noTargetCount = 0
    pictureCount = 0
    
    while(noTargetCount <= 10):
	
	 leftMotor = (6400 - getObstacle()[2])/10000.0
	 rightMotor = (6400 - getObstacle()[0])/10000.0
	 
	 motors(leftMotor, rightMotor)
	 	 
	 if((getObstacle()[0] < 100) and (getObstacle()[1] < 100) and (getObstacle()[2] < 100)):
	     noTargetCount += 1
	 elif (noTargetCount != 0):
	     noTargetCount = 0
		
	 pictureCount += 1

	 if (pictureCount % 10 == 0 and leftMotor == 0 and rightMotor == 0):
	     picture = takePicture()
	     colourResults.append(imageParse.parseImage(picture, formattedColours, 20))
		    
    
    pictureString = "burglarImage.jpg"
    savePicture(picture, pictureString)
    
    analyzeColours(colourResults, pictureString)
    print("done")

    return
    
def search():

     while (True):
	motors(-0.2, 0.2) #spin
       
	if (getObstacle()[1] >  100):
	    follow() #follow once blocked
	    break;

     stop()
     return