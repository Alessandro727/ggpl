from pyplasm import *
from src import workshop_03 as stairs
from src import workshop_07 as doorwindow 
from src import workshop_08 as house
from src import workshop_09 as roof
import csv
import math

xWindow=[.05,.4,.05,.4,.05,.4,.05,.4,.05]
yWindow=[.05,.4,.05,.4,.05,.4,.05,.4,.05]
occurrencyWindow=[[1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1]]

xDoor=[.05,.003,.3,.8,.3,.003,.05,.25,.05]
yDoor=[.1,.45,.15,.15,.15,.15,.15,.15,.15,.15,.15,.4,.1,.05]
occurrencyDoor=[[1,0,1,1,1,0,1,1,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1]]

def fullHouseBuilder(storeys):
	def singleStoreyBuilder(extWalls,intWalls,doors,windows,doors2):
		def houseFloor(hFloor):
			def houseWindows(xWindow,yWindow,occurrencyWindow):
				def houseDoors(xDoor,yDoor,occurrencyDoor):
					def houseStair(stair):
						def houseRoof(roofPol):
							def garden(garden):
								ground_floor = house.house_builder(extWalls,intWalls,doors,windows)
								ground_floor_2 = house.house_builder(extWalls,intWalls,doors2,windows)
								ground_floor = TEXTURE("texture/mura2.jpg")(ground_floor)
								ground_floor_2 = TEXTURE("texture/mura2.jpg")(ground_floor_2)
								floor = house.builder_2D(hFloor)
								floor = SOLIDIFY(floor)
								stairFloor = house.builder_2D(stair)
								stairFloor = SOLIDIFY(stairFloor)
								floor = DIFFERENCE([floor,stairFloor])
								f = floor
								floor = T([1,2])([0.5,0.5])(floor)
								floor = TEXTURE("texture/pavimento.jpg")(floor)
								floor2 = T([1,2,3])([6,6,150])(floor)

								ground_floor = STRUCT([ground_floor,floor])
								ground_floor = STRUCT([ground_floor,floor2])
								ground_floor_2 = STRUCT([ground_floor_2,floor2])


								with open("lines/"+windows + ".lines", "rb") as file:
									reader = csv.reader(file, delimiter=",")
									winPol = []
									cont = 0
									for line in reader:
										cont +=1
										#creating polygon base using vertices
										winPol.append([float(line[0]),float(line[1])])
										#create a cube with 4 vertices and restart finding
										if(cont == 4):
											xDist = math.fabs(winPol[0][0]-winPol[1][0])
											yDist = math.fabs(winPol[1][1]-winPol[2][1])
											if (xDist<yDist):
												yWin = 15.5
												xWin = yDist
											else:
												yWin = yDist
												xWin = 15.5
											
											w1 = doorwindow.ggplWindow(xWindow,yWindow,occurrencyWindow)(xWin,yWin,80)
											w1 = R([1,2])(-PI/2)(w1)
											w1 = T([1,2,3])([((winPol[0][0]+winPol[1][0])/2)-2,((winPol[1][1]+winPol[2][1])/2)+yDist/2,35])(w1)
											ground_floor = STRUCT([ground_floor,w1])
											ground_floor_2 = STRUCT([ground_floor_2,w1])
											winPol = []
											cont = 0 

								with open("lines/"+doors + ".lines", "rb") as file:
									reader = csv.reader(file, delimiter=",")
									basePol = []
									cont = 0
									for line in reader:
										cont +=1
										#creating polygon base using vertices
										basePol.append([float(line[0]),float(line[1])])
										#create a cube with 4 vertices and restart finding
										if(cont == 4):
											xDist = math.fabs(basePol[0][0]-basePol[1][0])
											yDist = math.fabs(basePol[1][1]-basePol[2][1])
											if (xDist<yDist):
												yDo = 12
												xDo = yDist
												d1 = doorwindow.ggplDoor(xDoor,yDoor,occurrencyDoor)(xDo,yDo,130)
												d1 = R([1,2])(-PI/2)(d1)
												d1 = T([1,2,3])([((basePol[0][0]+basePol[1][0])/2)-1,((basePol[1][1]+basePol[2][1])/2)+yDist/2,0])(d1)
											else:
												yDo = xDist
												xDo = 12
												d1 = doorwindow.ggplDoor(xDoor,yDoor,occurrencyDoor)(yDo,xDo,130)
												d1 = R([1,2])(PI)(d1)
												d1 = T([1,2,3])([((basePol[0][0]+basePol[1][0])/2)+xDist/2,((basePol[1][1]+basePol[2][1])/2)+12,0])(d1)
											

											ground_floor = STRUCT([ground_floor,d1])
											
											basePol = []
											cont = 0

								with open("lines/"+doors2 + ".lines", "rb") as file:
									reader = csv.reader(file, delimiter=",")
									basePol = []
									cont = 0
									for line in reader:
										cont +=1
										#creating polygon base using vertices
										basePol.append([float(line[0]),float(line[1])])
										#create a cube with 4 vertices and restart finding
										if(cont == 4):
											xDist = math.fabs(basePol[0][0]-basePol[1][0])
											yDist = math.fabs(basePol[1][1]-basePol[2][1])
											if (xDist<yDist):
												yDo = 12
												xDo = yDist
												d1 = doorwindow.ggplDoor(xDoor,yDoor,occurrencyDoor)(xDo,yDo,130)
												d1 = R([1,2])(-PI/2)(d1)
												d1 = T([1,2,3])([((basePol[0][0]+basePol[1][0])/2)-1,((basePol[1][1]+basePol[2][1])/2)+yDist/2,0])(d1)
											else:
												yDo = xDist
												xDo = 12
												d1 = doorwindow.ggplDoor(xDoor,yDoor,occurrencyDoor)(yDo,xDo,130)
												d1 = R([1,2])(PI)(d1)
												d1 = T([1,2,3])([((basePol[0][0]+basePol[1][0])/2)+xDist/2,((basePol[1][1]+basePol[2][1])/2)+12,0])(d1)
											

											
											ground_floor_2 = STRUCT([ground_floor_2,d1])
											basePol = []
											cont = 0

								with open("lines/"+stair + ".lines", "rb") as file:
									reader = csv.reader(file, delimiter=",")
									stairPol = []
									for line in reader:
										stairPol.append([float(line[0]),float(line[1])])
								xStair =  math.fabs(stairPol[0][0]-stairPol[1][0])
								yStair =  math.fabs(stairPol[1][1]-stairPol[2][1])
								if xStair ==0 or yStair ==0:
									xStair =  math.fabs(stairPol[0][0]-stairPol[2][0])-6
									yStair =  math.fabs(stairPol[0][1]-stairPol[1][1])-6
								zStair = storeys*150/2
								#houseStair = stairs.ggpl_spiral_staircase(xStair*0.015,yStair*0.015,4*zStair*0.025)
								houseStair = stairs.ggpl_spiral_staircase(xStair*0.015,yStair*0.015,150*0.0195*storeys*2)
								houseStair = S(3)(0.5)(houseStair)
								houseStair = R([1,2])(PI)(houseStair)
								houseStair = T([1,2])([stairPol[2][0]*0.015+6*0.015,stairPol[2][1]*0.015+6*0.015])(houseStair)

								with open("lines/"+roofPol + ".lines", "rb") as file:
									reader = csv.reader(file, delimiter=",")
									roofArray = []
									for line in reader:
										roofArray.append([float(line[0]),float(line[1])])
								
								ground_floor = S([1,2,3])([0.015,0.015,0.01875])(ground_floor)
								ground_floor_2 = S([1,2,3])([0.015,0.015,0.01875])(ground_floor_2)
								
								g = ground_floor_2
								for i in range(storeys-1):
									otherFloor = T(3)((i+1)*150*0.01875)(g)
									ground_floor = STRUCT([ground_floor,otherFloor])

								houseRoof = roof.builder_roof(roofPol)
								houseRoof = S([1,2,3])([0.015,0.015,0.01875])(houseRoof)
								finalHouse = STRUCT([ground_floor,houseStair])
								#finalHouse = STRUCT([ground_floor])
								
								centroid = roof.centroid_of_polygon(roofArray)
								houseRoof= T([1,2,3])([centroid[0]*0.015+27*0.015,centroid[1]*0.015+9*0.015,zStair*0.01875*4])(houseRoof)
								houseRoof = TEXTURE("texture/tetto3.jpg")(houseRoof)
								houseRoof = S([1,2,3])([1.15,1.15,0.5])(houseRoof)
								#houseRoof = T([1,2])([-SIZE([1])(houseRoof)[0]*0.095,-SIZE([2])(houseRoof)[0]*0.095]) (houseRoof)
								houseRoof = T([1,2])([-SIZE([1])(houseRoof)[0]*0.245,-SIZE([2])(houseRoof)[0]*0.075]) (houseRoof)
								houseGarden = house.builder_2D(garden)
								houseGarden = SOLIDIFY(houseGarden)
								houseGarden = DIFFERENCE([houseGarden,f])
								houseGarden = S([1,2])([0.015,0.015])(houseGarden)
								houseGarden = TEXTURE("texture/grass3.jpg")(houseGarden)
								finalHouse = STRUCT([finalHouse,houseGarden])
								finalHouse = STRUCT([finalHouse,houseRoof])
								finalHouse = S([1,2,3])([10,10,4])(finalHouse)
								return finalHouse
							return garden
						return houseRoof
					return houseStair
				return houseDoors
			return houseWindows
		return houseFloor
	return singleStoreyBuilder


if __name__=='__main__':
	VIEW(fullHouseBuilder(4)("muri_esterni","muri_interni","doors","windows","doors2")("muri_esterni")(xWindow,yWindow,occurrencyWindow)(xDoor,yDoor,occurrencyDoor)("stair")("muri_esterni")("garden"))




