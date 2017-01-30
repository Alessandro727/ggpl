import csv
import math
import numpy as np
from itertools import *
from pyplasm import *

def builder_roof(fileName):
	j=0
	s=0
	t=0
	firstShape = []
	falde = []
	topShape = []
	pol= []
	pol2 = []
	with open("polygons/"+fileName +  ".lines", "rb") as file:
		reader = csv.reader(file, delimiter=",")
		polylineList = []
		reader2 = reader
		row1=next(reader2)
		px = row1[0]
		py = row1[1]
	with open("polygons/"+fileName +  ".lines", "rb") as file:
		reader = csv.reader(file, delimiter=",")
		for row in reader:
			firstShape.append([float(row[0])-float(px),float(row[1])-float(py)])
			firstShape.append([float(row[2])-float(px),float(row[3])-float(py)])
	centroid = centroid_of_polygon(firstShape)
	[x,y] = centroid
	centroid = [x,y]
	for f in range(len(firstShape)):
		firstShape[f][0]=firstShape[f][0]-centroid[0]
		firstShape[f][1]=firstShape[f][1]-centroid[1]
	while j<len(firstShape):
		pol.append(POLYLINE([firstShape[j],firstShape[j+1]]))
		j=j+2
	pol = STRUCT(pol)

	firstShape = make_unique(firstShape)
	for i in range(len(firstShape)):
		topShape.append([firstShape[i][0]/2.0,firstShape[i][1]/2.0])
	
	
	topShape = topShape + [topShape[0]]
	while t<len(topShape)-1:
		pol2.append(POLYLINE([topShape[t],topShape[t+1]]))
		t=t+1

	piano = SOLIDIFY(STRUCT(pol2))
	piano = T(3)(200)(piano)
	firstShape = firstShape+ [firstShape[0]]
	for p in range(len(firstShape)):
		firstShape[p]=firstShape[p]+[float(0)]
	for k in range(len(topShape)):
		topShape[k]=topShape[k]+[float(200)]

	while s<len(make_unique(firstShape)):
		falde.append(MKPOL([[firstShape[s],firstShape[s+1],topShape[s],topShape[s+1]],[[1,2,3,4]],None]))
		s = s+1
	falde = STRUCT(falde)
	return STRUCT([falde,piano])


def make_unique(original_list):
    uniqueList = []
    [uniqueList.append(obj) for obj in original_list if obj not in uniqueList]
    return uniqueList

def area_of_polygon(x, y):
    """Calculates the signed area of an arbitrary polygon given its verticies """
    area = 0.0
    for i in xrange(-1, len(x) - 1):
        area += x[i] * (y[i + 1] - y[i - 1])
    return area / 2.0

def centroid_of_polygon(points):

    area = area_of_polygon(*zip(*points))
    resultX = 0
    resultY = 0
    N = len(points)
    points = cycle(points)
    x1, y1 = next(points)
    for i in range(N):
        x0, y0 = x1, y1
        x1, y1 = next(points)
        cross = (x0 * y1) - (x1 * y0)
        resultX += (x0 + x1) * cross
        resultY += (y0 + y1) * cross
    resultX /= (area * 6.0)
    resultY /= (area * 6.0)
    return (resultX, resultY)

def clockwise_order(points):
	firstPoint = points[0]
	centroid = [firstPoint[0],firstPoint[1]+0.0000001]
	firstLength = distance(centroid,firstPoint)
	newPoints = []

	while len(points)>0:
		cos = 400
		for j in range(len(points)):
			cos2 = find_angle(points[j],centroid)
			
			if cos2 < cos:
				cos = cos2
				newAdd = points[j]
		newPoints.append(newAdd)
		for t in range(len(points)):
			if points[t]==newAdd:
				el = t
		
		points.pop(el)
		

	return newPoints 

def distance(p1,p2):

	return float(math.sqrt(math.pow((p1[0] - p2[0]), 2)+math.pow((p1[1] - p2[1]), 2)))

def find_angle(p1,p2):
	return math.atan2(p1[1]-p2[1],p1[0]-p2[0])


def main():
	VIEW(builder_roof("roof"))

if __name__=='__main__':
	main()
