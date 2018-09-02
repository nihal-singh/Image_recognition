#Python Program for Image recognition (only numbers)

import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
from collections import Counter

def createExamples():
	createFile = open('exFile.txt','a')
	numberEx = range(0,10)
	numberVer = range(1,10)
	
	for eachNum in numberEx:
		for eachVer in numberVer:
			imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
			i = Image.open(imgFilePath)
			iar = np.array(i)
			iar = str(iar.tolist())

			lineToWrite = str(eachNum) +'::'+iar+'\n'
			createFile.write(lineToWrite)

#*************************************************************************

def threshold(imageArray):
	balAr = []
	newAr = imageArray
	from statistics import mean
	for eachRow in imageArray:
		for eachPix in eachRow:
			avg = mean(eachPix[:3])
			balAr.append(avg)
	balance = mean(balAr)

	for eachRow in newAr:
		for eachPix in eachRow:
			if mean(eachPix[:3]) > balance :
				eachPix[0] = 255
				eachPix[1] = 255
				eachPix[2] = 255
				#eachPix[3] = 255
			else:
				eachPix[0] = 0
				eachPix[1] = 0
				eachPix[2] = 0
				#eachPix[3] = 255 #this is alpha for opaque and transparent pixel.
	return newAr		

#*************************************************************************
#identify the number using the image.
def whatNumberIsThis(imgFilePath):
	matchedAr = []
	loadExmp = open('exFile.txt','r').read()
	loadExmp = loadExmp.split('\n')

	exImage = Image.open(imgFilePath)
	eIAr = np.array(exImage)
	eIArT = threshold(eIAr)
	eiArL = eIArT.tolist()
	
	imgToFind = str(eiArL)
	
	for eachExmp in loadExmp:
		if len(eachExmp) > 3 :
			eachExmp = eachExmp.split('::')
			numExmp = eachExmp[0]
			numAr = eachExmp[1]
			
			eachPix = numAr.split('],')
			eachPix_imgToFind = imgToFind.split('],')
			
			x=0;
			while(x < len(eachPix)):
				if eachPix[x] == eachPix_imgToFind[x]:
					matchedAr.append(int(numExmp))
				x += 1		
	c=Counter(matchedAr)
	#print(c)
#**************************************************************
#plot the result on graph
	graphX= []
	graphY= []
	
	for eachPair in c:
		graphX.append(eachPair)
		graphY.append(c[eachPair])

	fig = plt.figure()
	
	ax1 = plt.subplot2grid((4,4),(0,0),rowspan = 1 ,colspan = 4)
	ax2 = plt.subplot2grid((4,4),(1,0),rowspan = 3 ,colspan = 4)

	ax1.imshow(eIAr)
	ax2.bar(graphX, graphY, align='center')
	plt.ylim(400)


	plt.show()
#*******************************************************************



#createExamples() // used only one time to create example set (file exFile.txt)
whatNumberIsThis('images/test.png')

