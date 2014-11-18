from myro import *
from math import *
#intial globals
black=makeColor(0,0,0)
white=makeColor(255,255,255)
checkedPixel=[]
width=0
height=0
borderWidth=[-1,-1]
borderHeight=[-1,-1]
totalWhitePixels=0
#utility functions
def c_distance (color1,color2):
    r1=getRed(color1)
    r2=getRed(color2)
    g1=getGreen(color1)
    g2=getGreen(color2)
    b1=getBlue(color1)
    b2=getBlue(color2)
    return sqrt((r1-r2)**2+(g1-g2)**2+(b1-b2)**2)
    

#other functions
def dfs(row,col):
    global totalWhitePixels
    if (row<0) or (row>height):
        return
    if (col<0) or (col>width):
        return
    if (checkedPixel[row][col]!=0):
        return
    
    
def initializeFunction(originalPicture):
    
    global checkedPixel
    global width
    global height
    if (originalPicture==0):
        return
    width=getWidth(originalPicture)
    height=getHeight(originalPicture)
    #checkedPixel=zeros(2,2)
    checkedPixel=[[0 for i in xrange(width)]for i in xrange(height)]
    #checkedPixel=zeros((getHeight(originalPicture),getWidth(originalPicture))
    #depth first search for largest white blob with size at least 25-35% of picture area
    return
minRow=0
minCol=0

defaultPicture=makePicture("felix.jpg")
#show(defaultPicture, "FIRST")

initializeFunction(defaultPicture)
print("HEIGHT: ",height)
print("WIDTH: " , width)

pictureToEdit=makePicture("felix.jpg")
createBoundingBoxOption=0;
createBoundingBoxOption=input("Enter 1 if you wish to set a bounding box: ")
if (createBoundingBoxOption==1):
    minRow=input("Enter the first row of pixels to process: ")
    minCol=input("Enter the first column of pixels to process: ")
    height=input("Enter the last row of pixels to process: ")
    width=input("Enter the last column of pixels to process: ")
currentRow=minRow
while (currentRow<height):
   # print("CURRENT ROW: ", currentRow)
    currentCol=minCol
    while (currentCol<width):
        currentPixel=getPixel(pictureToEdit, currentCol, currentRow)
        if (c_distance(white,getColor(currentPixel))<c_distance(black,getColor(currentPixel))+70.0):
            setColor(currentPixel,white)
        else:
            setColor(currentPixel,black)
    #    print("CURRENT COL: ", currentCol)
        currentCol=currentCol+1
        
    currentRow=currentRow+1
show(pictureToEdit)
repaint(pictureToEdit)
show(pictureToEdit)
savePicture(pictureToEdit, "PICTURE_PARSER.jpg")


