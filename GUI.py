from myro import *
import sys
import os
import time
import shoeRecord
import scan
#import barcodeUnlock

def getName():
	print "Person's Name:",
	name = raw_input()
	return name
	
#Felix's unlock method (not real one) returning an integer value
def barcodeUnlock():
	return 1
	
unlock=0
x=0
os.system('cls')
programContinue="No"
unlockQuestion=askQuestion("The robot has to unlock. Hold the bar code in front of the robot's camera. Ready?","Y")
if unlockQuestion=="Y":
	unlock=barcodeUnlock()
	if unlock==0:
		while unlock == 0:
			os.system('cls')
			unlockQuestion=askQuestion("The robot cannot unlock. The bar code was incorrect. Hold the correct bar code in front of the camera. Ready?","Y")
			unlock=barcodeUnlock()
	if unlock==1:
		os.system('cls')
		print "Bar code recognized. Robot unlocked."
		
		while programContinue=="No":
			if(x>0):
				os.system('cls')
				print("Main Menu")
				print "==================================="
			x+=1
			programContinue2=askQuestion("Enter the Mode of usage:","PAX")
			if programContinue2 == "P":
				os.system('cls')
				print "Patrol mode activated."
				scan.search()
				os.system('cls')
				print "Patrol mode exited."
			elif programContinue2 == "A":
				os.system('cls')
				print "Add shoe mode activated."
				file=open("data.txt","a")
				name=getName()
				takePic=askQuestion("Place the shoe sideways in front of the camera. Are you ready to take the picture?")
				if takePic == "No":
					while takePic == "No":
						takePic=askQuestion("Place the shoe sideways in front of the camera. Are you ready to take the picture?")
				elif takePic == "Yes":	
					os.system('cls')
					shoeRecord.shoeRecord(name)
				programContinue=askQuestion("Shoe information stored. Exit program?")
				if programContinue == "Yes":
					sys.exit(0)
			elif programContinue2 == "X":
				sys.exit(0)					
