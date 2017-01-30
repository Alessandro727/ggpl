from pyplasm import * 
from src import workshop_10 as w10
from src import workshop_09 as w09
from src import car 
from src import palalottomatica as pala
from src import albero
from src import metro as met
from src import distributore as dist
import csv

xWindow=[.05,.4,.05,.4,.05,.4,.05,.4,.05]
yWindow=[.05,.4,.05,.4,.05,.4,.05,.4,.05]
occurrencyWindow=[[1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1]]

xDoor=[.05,.003,.3,.8,.3,.003,.05,.25,.05]
yDoor=[.1,.45,.15,.15,.15,.15,.15,.15,.15,.15,.15,.4,.1,.05]
occurrencyDoor=[[1,0,1,1,1,0,1,1,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1]]


def ggpl_neighborhood_EUR_maker(filename):
	with open("lines/"+filename + ".lines", "rb") as file:
		reader = csv.reader(file, delimiter=",")
		street = []
		for line in reader:
			street.append([float(line[0]),float(line[1])])
			street.append([float(line[2]),float(line[3])])

	curve = []
	curva = []
	cont = 0
	for i in range(len(street)):
		curva.append(street[i])
		cont += 1
		if cont == 2:
			strada = MAP(BEZIER(S1)(curva))(INTERVALS(1)(5))
			curva = []
			curve.append(strada)
			cont= 0
	curve = STRUCT(curve)
	lineeStrada=curve
	curve = OFFSET([10,10])(curve)
	lineeStrada = OFFSET([15,15])(lineeStrada)
	curve = PROD([QUOTE([3]),curve])
	lineeStrada = PROD([QUOTE([1]),lineeStrada])
	curve = R([1,3])(PI/2)(curve)
	lineeStrada = R([1,3])(PI/2)(lineeStrada)
	lineeStrada = T([1,2])([2.5,-2.5])(lineeStrada)
	box = BOX([1,2])(curve)
	
	box2 = OFFSET([0,0,10])(box)
	box = OFFSET([0,0,40])(box)
	curve = T(3)(49.5)(curve)
	lineeStrada = T(3)(50)(lineeStrada)
	box2 = T(3)(40)(box2)
	curve = MATERIAL([.01,.01,.01,1,  106/255.0,101/255.0,97/255.0,1,  0,0,0,1, 0,0,0,1, 1]) (curve)
	box2 = TEXTURE("texture/grass4.jpg")(box2)
	box = MATERIAL([.01,.01,.01,1,  .4,.2,0,1,  0,0,0,1, 0,0,0,1, 1])(box)
	box = STRUCT([box,box2])
	
	secondHouse = w10.fullHouseBuilder(2,1)("muri_esterniCasa2","muri_interniCasa2","doorsCasa2","windowsCasa2","muri_esterni_2Casa2")("perimetroCasa2")(xWindow,yWindow,occurrencyWindow)(xDoor,yDoor,occurrencyDoor)("stairCasa2")("roofCasa2")("gardenCasa2")
	house = w10.fullHouseBuilder(4,0)("muri_esterni","muri_interni","doors","windows","doors2")("muri_esterni")(xWindow,yWindow,occurrencyWindow)(xDoor,yDoor,occurrencyDoor)("stair")("muri_esterni")("garden")
	curve = STRUCT([box,curve,lineeStrada])
	house =S([1,2,3])([2*(SIZE([1])(curve)[0])/(17*SIZE([1])(house)[0]),(SIZE([2])(curve)[0])/(17*SIZE([2])(house)[0]),(SIZE([3])(curve)[0])/(1*SIZE([3])(house)[0])]) (house)
	house2 = T(2)(-100)(house)
	secondHouse = S([1,2,3])([(SIZE([1])(curve)[0])/(3.5*SIZE([1])(house)[0]),(SIZE([2])(house)[0])/(0.5*SIZE([2])(house)[0]),(SIZE([3])(curve)[0])/(0.3*SIZE([3])(house)[0])]) (secondHouse)
	secondHouse = R([1,2])(1.919)(secondHouse)
	thirdHouse = secondHouse
	residenza1 = STRUCT([house,house2])
	residenza2 = residenza1
	residenza1 = R([1,2])(0.3489)(residenza1)
	residenza2 = residenza1
	residenza3 = residenza1
	residenza1 = T([1,2,3])([-525,625,51])(residenza1)
	residenza2 = T([1,2,3])([-450,425,51])(residenza2)
	residenza3 = T([1,2,3])([-125,810,51])(residenza3)
	secondHouse = T([1,2,3])([-320,780,51])(secondHouse)
	thirdHouse = T([1,2,3])([-190,475,51])(thirdHouse)
	palalottomatica = pala.palalottomatica()
	palalottomatica = S([1,2,3])([(SIZE([1])(curve)[0])/(2.5*SIZE([1])(house)[0]),(SIZE([1])(curve)[0])/(2.5*SIZE([1])(house)[0]),(SIZE([3])(curve)[0])/(0.5*SIZE([3])(house)[0])]) (palalottomatica)
	palalottomatica = T([1,2,3])([-140,160,51])(palalottomatica)
	alberi = [albero.albero()]
	for i in range(5):
		alberi.append(T(2)([(i+1)*5])(albero.albero()))
	alberi = STRUCT(alberi)
	alberi = S([1,2,3])([(SIZE([1])(curve)[0])/(3.5/2*SIZE([1])(house)[0]),(SIZE([1])(curve)[0])/(3.5/2*SIZE([1])(house)[0]),(2*SIZE([3])(curve)[0])/(0.6*SIZE([3])(house)[0])]) (alberi)
	alberi = R([1,2])(0.3489)(alberi)
	alberi2 = T([1,2,3])([-95,635,51])(alberi)
	alberi = T([1,2,3])([-280,400,51])(alberi)
	alberi= STRUCT([alberi,alberi2])
	cars = [car.car()]
	for i in range(2):
		cars.append(T(2)([(i+1)*10])(car.car()))
	cars = STRUCT(cars)
	cars = S([1,2,3])([(SIZE([1])(curve)[0])/(3.5/2*SIZE([1])(house)[0]),(SIZE([1])(curve)[0])/(2.5/2*SIZE([1])(house)[0]),(2*SIZE([3])(curve)[0])/(0.6*SIZE([3])(house)[0])]) (cars)
	cars = R([1,2])(1.919)(cars)
	cars2 = T([1,2,3])([-350,325,52])(cars)
	cars = T([1,2,3])([-380,735,52])(cars)
	cars= STRUCT([cars,cars2])
	metro = met.metro()
	metro = S([1,2,3])([(SIZE([1])(curve)[0])/(1.5*SIZE([1])(house)[0]),(SIZE([1])(curve)[0])/(1.5/2*SIZE([1])(house)[0]),(2*SIZE([3])(curve)[0])/(0.6*SIZE([3])(house)[0])]) (metro)
	metro2 = metro
	metro = T([1,2,3])([-430,740,51])(metro)
	metro2 = T([1,2,3])([-430,705,51])(metro2)
	metro = STRUCT([metro,metro2])
	distributore = dist.distributore()
	distributore = S([1,2,3])([(SIZE([1])(curve)[0])/(1.7*SIZE([1])(house)[0]),(SIZE([1])(curve)[0])/(1.7*SIZE([1])(house)[0]),(2*SIZE([3])(curve)[0])/(0.6*SIZE([3])(house)[0])]) (distributore)
	distributore = R([1,2])(0.3489)(distributore)
	distributore = T([1,2,3])([-420,100,51])(distributore)
	curve = STRUCT([curve,residenza1])
	curve = STRUCT([curve,residenza2])
	curve = STRUCT([curve,residenza3])
	curve = STRUCT([curve,secondHouse])
	curve = STRUCT([curve,thirdHouse])
	curve = STRUCT([curve,palalottomatica])
	curve = STRUCT([curve,alberi])
	curve = STRUCT([curve,cars])
	curve = STRUCT([curve,metro])
	return STRUCT([curve,distributore])
	


def main():
	VIEW(ggpl_neighborhood_EUR_maker("street"))

if __name__=='__main__':
	main()
