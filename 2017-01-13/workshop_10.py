from pyplasm import *
from random import randint
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

def fullHouseBuilder(storeys,flag):
	def singleStoreyBuilder(extWalls,intWalls,doors,windows,secondFloor):
		def houseFloor(hFloor):
			def houseWindows(xWindow,yWindow,occurrencyWindow):
				def houseDoors(xDoor,yDoor,occurrencyDoor):
					def houseStair(stair):
						def houseRoof(roofPol):
							def garden(garden):

								""" Realizzazione mura interne ed esterne primo piano """
								groundFloor = house.house_builder(extWalls,intWalls,doors,windows)
								""" Realizzazione mura interne ed esterne piani successivi """
								if flag!= 1:
									groundFloor2 = house.house_builder(extWalls,intWalls,secondFloor,windows)
								else:
									groundFloor2 = house.house_builder(secondFloor,intWalls,doors,windows)
								groundFloor = TEXTURE("texture/mura2.jpg")(groundFloor)
								groundFloor2 = TEXTURE("texture/mura2.jpg")(groundFloor2)
								""" Realizzazione pavimento """
								floor = house.builder_2D(hFloor)
								floor = SOLIDIFY(floor)
								stairFloor = house.builder_2D(stair)
								stairFloor = SOLIDIFY(stairFloor)
								floor = DIFFERENCE([floor,stairFloor])
								f = floor
								floor = T([1,2])([0.5,0.5])(floor)
								floor = TEXTURE("texture/pavimento.jpg")(floor)
								floor2 = T([1,2,3])([6,6,150])(floor)

								groundFloor = STRUCT([groundFloor,floor])
								groundFloor = STRUCT([groundFloor,floor2])
								groundFloor2 = STRUCT([groundFloor2,floor2])

								""" Inserimento finestre all'interno dei piani dell'abitazione """

								with open("lines/"+windows + ".lines", "rb") as file:
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

											""" Condizioni per il tipo di casa da realizzare e per la diversa dimensione delle tracce 
												per realizzare le finestre nei file svg """
											if (flag != 1):
												if (xDist<yDist):
													yWin = 15.5
													xWin = yDist
												else:
													yWin = yDist
													xWin = 15.5
											else:
												if (xDist>yDist):
													yWin = 15.5
													xWin = yDist
												else:
													yWin = yDist
													xWin = 15.5
											firstWindow = doorwindow.ggplWindow(xWindow,yWindow,occurrencyWindow)(xWin,yWin,80)
											firstWindow = R([1,2])(-PI/2)(firstWindow)
											firstWindow = T([1,2,3])([((basePol[0][0]+basePol[1][0])/2)-2,((basePol[1][1]+basePol[2][1])/2)+yDist/2,35])(firstWindow)
											
											
											groundFloor = STRUCT([groundFloor,firstWindow])
											groundFloor2 = STRUCT([groundFloor2,firstWindow])
											basePol = []
											cont = 0 

								""" Inserimento porte all'interno dei piani dell'abitazione """

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

											""" Condizioni per il tipo di casa da realizzare e per la diversa dimensione delle tracce 
												per realizzare le porte nei file svg """
											if flag != 1:
												if (xDist<yDist):
													yDo = 12
													xDo = yDist
													firstDoor = doorwindow.ggplDoor(xDoor,yDoor,occurrencyDoor)(xDo,yDo,130)
													firstDoor = R([1,2])(-PI/2)(firstDoor)
													firstDoor = T([1,2,3])([((basePol[0][0]+basePol[1][0])/2)-1,((basePol[1][1]+basePol[2][1])/2)+yDist/2,0])(firstDoor)
												else:
													yDo = xDist
													xDo = 12
													firstDoor = doorwindow.ggplDoor(xDoor,yDoor,occurrencyDoor)(yDo,xDo,130)
													firstDoor = R([1,2])(PI)(firstDoor)
													firstDoor = T([1,2,3])([((basePol[0][0]+basePol[1][0])/2)+xDist/2,((basePol[1][1]+basePol[2][1])/2)+12,0])(firstDoor)
											else:
												if (xDist>yDist):
													yDo = 12
													xDo = yDist
													firstDoor = doorwindow.ggplDoor(xDoor,yDoor,occurrencyDoor)(xDo,yDo,130)
													firstDoor = R([1,2])(-PI/2)(firstDoor)
													firstDoor = T([1,2,3])([((basePol[0][0]+basePol[1][0])/2)-1,((basePol[1][1]+basePol[2][1])/2)+yDist/2,0])(firstDoor)
												else:
													yDo = xDist
													xDo = 12
													firstDoor = doorwindow.ggplDoor(xDoor,yDoor,occurrencyDoor)(yDo,xDo,130)
													firstDoor = R([1,2])(PI)(firstDoor)
													firstDoor = T([1,2,3])([((basePol[0][0]+basePol[1][0])/2)+xDist/2,((basePol[1][1]+basePol[2][1])/2)+12,0])(firstDoor)

											groundFloor = STRUCT([groundFloor,firstDoor])
											if flag == 1:
												groundFloor2 = STRUCT([groundFloor2,firstDoor])
											
											basePol = []
											cont = 0
								
								""" Inserimento porte all'interno dei piani dell'abitazione con muri interni differenti """
								if flag != 1:
									with open("lines/"+secondFloor + ".lines", "rb") as file:
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
													firstDoor = doorwindow.ggplDoor(xDoor,yDoor,occurrencyDoor)(xDo,yDo,130)
													firstDoor = R([1,2])(-PI/2)(firstDoor)
													firstDoor = T([1,2,3])([((basePol[0][0]+basePol[1][0])/2)-1,((basePol[1][1]+basePol[2][1])/2)+yDist/2,0])(firstDoor)
												else:
													yDo = xDist
													xDo = 12
													firstDoor = doorwindow.ggplDoor(xDoor,yDoor,occurrencyDoor)(yDo,xDo,130)
													firstDoor = R([1,2])(PI)(firstDoor)
													firstDoor = T([1,2,3])([((basePol[0][0]+basePol[1][0])/2)+xDist/2,((basePol[1][1]+basePol[2][1])/2)+12,0])(firstDoor)
												

												
												groundFloor2 = STRUCT([groundFloor2,firstDoor])
												basePol = []
												cont = 0

								""" Realizzazione scale """

								with open("lines/"+stair + ".lines", "rb") as file:
									reader = csv.reader(file, delimiter=",")
									stairPol = []
									for line in reader:
										stairPol.append([float(line[0]),float(line[1])])
								xStair =  math.fabs(stairPol[0][0]-stairPol[1][0])
								yStair =  math.fabs(stairPol[1][1]-stairPol[2][1])
								zStair = storeys*150/2
								if xStair ==0 or yStair ==0:
									if flag==1:
										xStair =  math.fabs(stairPol[0][0]-stairPol[2][0])-5
										yStair =  math.fabs(stairPol[0][1]-stairPol[1][1])-5
										
									else:
										xStair =  math.fabs(stairPol[0][0]-stairPol[2][0])
										yStair =  math.fabs(stairPol[0][1]-stairPol[1][1])
								
								""" Condizione per realizzare il tipo di scala congeniale con l'abitazione per rotazione e posizione del pianerottolo di uscita"""
								if flag!=1:
									houseStair = stairs.ggpl_spiral_staircase(xStair*0.015,yStair*0.015,150*0.017*storeys*2)
									houseStair = S(3)(0.5)(houseStair)
									houseStair = R([1,2])(PI)(houseStair)
									houseStair = T([1,2])([stairPol[2][0]*0.015+6*0.015,stairPol[2][1]*0.015+6*0.015])(houseStair)
								else:
									houseStair = stairs.ggpl_spiral_staircase(yStair*0.015,xStair*0.015,150*0.0125*storeys*2)
									houseStair = S(3)(0.5)(houseStair)
									houseStair = R([1,2])(PI/2)(houseStair)
									houseStair = T([1,2])([stairPol[2][0]*0.015+6*0.015,stairPol[2][1]*0.015+6*0.015-yStair*0.015])(houseStair)

								""" Realizzazione tetto """

								with open("lines/"+roofPol + ".lines", "rb") as file:
									reader = csv.reader(file, delimiter=",")
									roofArray = []
									for line in reader:
										roofArray.append([float(line[0]),float(line[1])])
								hfloor = 0.0118
								if flag != 1:
									hfloor = 0.0171

								groundFloor = S([1,2,3])([0.015,0.015,hfloor])(groundFloor)
								groundFloor2 = S([1,2,3])([0.015,0.015,hfloor])(groundFloor2)
								
								g = groundFloor2
								for i in range(storeys-1):
									otherFloor = T(3)((i+1)*150*hfloor)(g)
									groundFloor = STRUCT([groundFloor,otherFloor])

								houseRoof = roof.builder_roof(roofPol)
								houseRoof = S([1,2,3])([0.015,0.015,hfloor])(houseRoof)
								finalHouse = STRUCT([groundFloor,houseStair])
								
								centroid = roof.centroid_of_polygon(roofArray)
								houseRoof= T([1,2,3])([centroid[0]*0.015+27*0.015,centroid[1]*0.015+9*0.015,zStair*hfloor*4])(houseRoof)
								houseRoof = TEXTURE("texture/tetto3.jpg")(houseRoof)
								houseRoof = S([1,2,3])([1.15,1.15,0.5])(houseRoof)

								""" Condizione per ridimensionare il tetto in maniera opportuna a seconda del tipo di casa """

								if flag == 1:
									houseRoof = T([1,2])([-SIZE([1])(houseRoof)[0]*0.095,-SIZE([2])(houseRoof)[0]*0.095]) (houseRoof)
								else:
									houseRoof = T([1,2])([-SIZE([1])(houseRoof)[0]*0.245,-SIZE([2])(houseRoof)[0]*0.075]) (houseRoof)

								""" Creazione vialetto/giardino di casa """
								houseGarden = house.builder_2D(garden)
								houseGarden = S([1,2])([2,2])(houseGarden)
								houseGarden = T([1,2])([-(SIZE([1])(houseGarden)[0])/4,-(SIZE([2])(houseGarden)[0])/4])(houseGarden)
								houseGarden = SOLIDIFY(houseGarden)
								houseGarden = DIFFERENCE([houseGarden,f])
								houseGarden = S([1,2])([0.015,0.015])(houseGarden)

								""" Valore randomico per la scelta della texture da utilizzare """
								random = randint(1,4)
								houseGarden = TEXTURE("textureVialetto/vialetto"+str(random)+".jpg")(houseGarden)
								finalHouse = STRUCT([finalHouse,houseGarden])
								finalHouse = STRUCT([finalHouse,houseRoof])
								finalHouse = S([1,2,3])([2,2,1.5])(finalHouse)
								return finalHouse
							return garden
						return houseRoof
					return houseStair
				return houseDoors
			return houseWindows
		return houseFloor
	return singleStoreyBuilder


if __name__=='__main__':
	VIEW(fullHouseBuilder(2,0)("muri_esterni","muri_interni","doors","windows","doors2")("muri_esterni")(xWindow,yWindow,occurrencyWindow)(xDoor,yDoor,occurrencyDoor)("stair")("muri_esterni")("garden"))
	VIEW(fullHouseBuilder(5,1)("muri_esterniCasa2","muri_interniCasa2","doorsCasa2","windowsCasa2","muri_esterni_2Casa2")("perimetroCasa2")(xWindow,yWindow,occurrencyWindow)(xDoor,yDoor,occurrencyDoor)("stairCasa2")("roofCasa2")("gardenCasa2"))



