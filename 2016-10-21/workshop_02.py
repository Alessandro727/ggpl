from larlib import * 

import csv
import sys

def ggpl_bone_structure(file_name):
	
	lengthPerpendicularBeams = []
	""" open csv file """
	with open(file_name, 'rb') as csvFile:
		reader = csv.reader(csvFile)
		i=0
		for row in reader:
			if i%2==1:
				lengthPerpendicularBeams = lengthPerpendicularBeams + [float(row[0])]
				i=i+1
			elif i%2==0:
				(px,py)=(float(row[0]),float(row[1]))
				pillarDistances = []
				j=3
				while row[j]!="]":
					pillarDistances.append(float(row[j]))
					j=j+1
				(by,bz)= (float(row[j+1]),float(row[j+2]))
				j= j+4
				beamInterstoryHeights = []
				while row[j]!="]":
					beamInterstoryHeights.append(float(row[j]))
					j=j+1	
				i=i+1

	return makeStruct((px,py), pillarDistances, (by,bz), beamInterstoryHeights, lengthPerpendicularBeams)

def makeStruct((px,py),pillarDistances,(by,bz), beamInterstoryHeights, lengthPerpendicularBeams):

	""" array for the pillar foundations """
	pillarArray = [px]
	for value in pillarDistances:
		pillarArray = pillarArray+[-value]+[px]
	
	""" x-axis of the pillar """
	xBasePillar = QUOTE(pillarArray)
	
	""" y-axis of the pillar """
	yBasePillar = QUOTE([py])

	xyBasePillar = PROD([xBasePillar, yBasePillar])

	""" array for the z-axis of the pillar """
	heightsPillar = []
	for value in beamInterstoryHeights:
		heightsPillar = heightsPillar+[value+bz]
	
	""" z-axis of the pillar """
	zBasePillar = QUOTE(heightsPillar)

	pillars = PROD([xyBasePillar, zBasePillar])

	""" array for the realization of the beams """
	beamStruct = [ -x for x in pillarArray]
	
	""" x-axis of the beams """
	xBaseBeam = QUOTE(beamStruct)

	""" y-axis of the beams """
	yBaseBeam = QUOTE([by])

	xyBaseBeam = PROD([xBaseBeam, yBaseBeam])

	""" array for distance between the beams """
	beamsDistance = []
	for value in beamInterstoryHeights:
		beamsDistance = beamsDistance+[-value]+[bz]

	beams = PROD([xyBaseBeam, QUOTE(beamsDistance)])

	""" frame """
	struct = STRUCT([pillars, beams])
	
	""" distance between frames """
	framesDistance = []
	for value in lengthPerpendicularBeams:
		framesDistance = framesDistance + [-py] + [value]

	""" creating beams between frames """
	yBasePerpendicularBeams = QUOTE(framesDistance)

	xBasePerpendicularBeams = QUOTE([by])

	xyBasePerpendicularBeams = PROD([xBasePerpendicularBeams, yBasePerpendicularBeams])

	xyzBasePerpendicularBeams = PROD([xyBasePerpendicularBeams, QUOTE(beamsDistance)])

	xyzStruct = STRUCT([xyzBasePerpendicularBeams])

	VIEW(xyzStruct)
	
	""" creating arrays for the function T() """
	accumulator=0
	arrayBeams = []

	for value in lengthPerpendicularBeams:
		accumulator = accumulator+value
		arrayBeams=arrayBeams+[accumulator]

	accumulator = 0
	arrayPillar = []
	for value in pillarDistances:
		accumulator = accumulator+value
		arrayPillar=arrayPillar+[accumulator]

	""" duplication frames and perpendicular beams """
	dist=py
	structFrames=struct
	for value in arrayBeams:
		structFrames = STRUCT([structFrames, T(2)(value+dist), struct])
		dist+=py

	dist=px
	structBeams= xyzStruct
	for value in arrayPillar:
		structBeams = STRUCT([structBeams, T(1)(value+dist), xyzStruct])
		dist+=px

	VIEW(STRUCT([structBeams]))
	VIEW(STRUCT([structFrames]))
	""" merge duplicate structures """
	finalStruct =  STRUCT([structFrames, structBeams])

	return finalStruct

def main():
	
	VIEW(ggpl_bone_structure('frame_data_456893.csv'))

if __name__=='__main__':
	
	main()

