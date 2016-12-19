from larlib import *
import csv

def builder_2D(fileName):
	with open("lines/"+fileName +  ".lines", "rb") as file:
		reader = csv.reader(file, delimiter=",")
		wall = []
		for row in reader:
			wall.append(POLYLINE([[float(row[0]), float(row[1])],[float(row[2]), float(row[3])]]))
	wall = STRUCT(wall)

	return wall

def hole_builder(fileName):
	with open("lines/"+fileName + ".lines", "rb") as file:
		reader = csv.reader(file, delimiter=",")
		holes = []
		basePol = []
		cont = 0
		for line in reader:
			cont +=1
			#creating polygon base using vertices
			basePol.append([float(line[0]),float(line[1])])
			#create a cube with 4 vertices and restart finding
			if(cont == 4):
				holes.append(MKPOL([basePol,[[1,2,3,4]],None]))
				basePol = []
				cont = 0
	holes = STRUCT(holes)
	return holes

def house_builder():

	ext_wall_2D = builder_2D("ext_wall")
	floor = SOLIDIFY(ext_wall_2D)
	floor = TEXTURE("texture/parquet.jpg")(floor)


	extwalls = OFFSET([12,12])(ext_wall_2D)
	extwalls = PROD([extwalls, Q(150)])
	
	int_wall_2D = builder_2D("int_wall")

	intwalls = OFFSET([12,12])(int_wall_2D)
	intwalls = PROD([intwalls, Q(150)])

	door = hole_builder("doors")
	door = PROD([door, Q(130)])

	window = hole_builder("window")
	window = PROD([window, Q(80)])
	window = T(3)(35)(window)

	walls = STRUCT([extwalls,intwalls])

	house = DIFFERENCE([walls,door,window])
	house = TEXTURE("texture/ext_wall.jpg")(house)

	return STRUCT([house,floor])


if __name__=='__main__':
	VIEW(house_builder())
	
