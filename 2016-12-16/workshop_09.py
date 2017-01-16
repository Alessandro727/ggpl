import csv
import math
import numpy as np
from itertools import *
from pyplasm import *

def builder_roof(fileName):
	j=0
	s=0
	t=0
	first_shape = []
	falde = []
	top_shape = []
	pol= []
	pol2 = []
	with open("polygon/"+fileName +  ".lines", "rb") as file:
		reader = csv.reader(file, delimiter=",")
		polylineList = []
		reader2 = reader
		row1=next(reader2)
		px = row1[0]
		py = row1[1]
	with open("polygon/"+fileName +  ".lines", "rb") as file:
		reader = csv.reader(file, delimiter=",")
		for row in reader:
			first_shape.append([float(row[0])-float(px),float(row[1])-float(py)])
			first_shape.append([float(row[2])-float(px),float(row[3])-float(py)])
	centroid = centroid_of_polygon(first_shape)
	[x,y] = centroid
	centroid = [x,y]
	for f in range(len(first_shape)):
		first_shape[f][0]=first_shape[f][0]-centroid[0]
		first_shape[f][1]=first_shape[f][1]-centroid[1]
	while j<len(first_shape):
		pol.append(POLYLINE([first_shape[j],first_shape[j+1]]))
		j=j+2
	pol = STRUCT(pol)

	
	for i in range(len(first_shape)):
		top_shape.append([first_shape[i][0]/2.0,first_shape[i][1]/2.0])

	first_shape = make_unique(first_shape)

	top_shape = make_unique(top_shape)
	top_shape= clockwise_order(top_shape)
	first_shape = clockwise_order(first_shape)
	top_shape = top_shape + [top_shape[0]]
	while t<len(top_shape)-1:
		pol2.append(POLYLINE([top_shape[t],top_shape[t+1]]))
		t=t+1

	piano = SOLIDIFY(STRUCT(pol2))
	piano = T(3)(4)(piano)
	first_shape = first_shape+ [first_shape[0]]
	for p in range(len(first_shape)):
		first_shape[p]=first_shape[p]+[float(0)]
	for k in range(len(top_shape)):
		top_shape[k]=top_shape[k]+[float(4)]

	while s<len(make_unique(first_shape)):
		falde.append(MKPOL([[first_shape[s],first_shape[s+1],top_shape[s],top_shape[s+1]],[[1,2,3,4]],None]))
		s = s+1
	falde = STRUCT(falde)
	return STRUCT([falde,piano])


def make_unique(original_list):
    unique_list = []
    [unique_list.append(obj) for obj in original_list if obj not in unique_list]
    return unique_list

def area_of_polygon(x, y):
    """Calculates the signed area of an arbitrary polygon given its verticies """
    area = 0.0
    for i in xrange(-1, len(x) - 1):
        area += x[i] * (y[i + 1] - y[i - 1])
    return area / 2.0

def centroid_of_polygon(points):

    area = area_of_polygon(*zip(*points))
    result_x = 0
    result_y = 0
    N = len(points)
    points = cycle(points)
    x1, y1 = next(points)
    for i in range(N):
        x0, y0 = x1, y1
        x1, y1 = next(points)
        cross = (x0 * y1) - (x1 * y0)
        result_x += (x0 + x1) * cross
        result_y += (y0 + y1) * cross
    result_x /= (area * 6.0)
    result_y /= (area * 6.0)
    return (result_x, result_y)

def clockwise_order(points):
	firstPoint = points[0]
	centroid = [firstPoint[0],firstPoint[1]+0.0000001]
	print centroid
	firstLength = distance(centroid,firstPoint)
	new_points = []

	while len(points)>0:
		cos = 400
		for j in range(len(points)):
			cos2 = find_angle(points[j],centroid)
			
			if cos2 < cos:
				cos = cos2
				new_add = points[j]
		new_points.append(new_add)
		for t in range(len(points)):
			if points[t]==new_add:
				el = t
		
		points.pop(el)
		

	return new_points 

def distance(p1,p2):

	return float(math.sqrt(math.pow((p1[0] - p2[0]), 2)+math.pow((p1[1] - p2[1]), 2)))

def find_angle(p1,p2):
	return math.atan2(p1[1]-p2[1],p1[0]-p2[0])

def main():
	VIEW(builder_roof("tequ"))

if __name__=='__main__':
	main()
