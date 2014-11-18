def addShoe(name, colour):
    file = open("OGdata.txt", "a")
    file.write(name)
    file.write("??")
    file.write(colour)
    file.write("||")
    file.close()
    return

def getInfo():
    file=open("OGdata.txt","r")
    text = file.read()
    elements = text.split("||")
    
    info = {}
    
    for x in elements:
        if(x != ""):
            parts = x.split("??")
            name = parts[0]
            colour = parts[1]
            info[name] = colour
    
    return info
    
    
def getArray():
    
    file=open("OGdata.txt","r")
    text = file.read()
    elements = text.split("||")
    
    array = []
    
    for x in elements:
        if(x != ""):
            parts = x.split("??")
            colour = parts[1]
            array.append(colour)
            
    return array