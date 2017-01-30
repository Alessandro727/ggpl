from pyplasm import * 
from random import randint

def car():
	telaio = CUBOID([1.8,4.5,0.05])
	telaio = T(3)([0.35]) (telaio)
	ruota = CIRCLE(0.35)([40,40])

	ruota = PROD([Q(0.4),ruota])
	ruota1 = T([1,2,3])([0,0.9,0.35])(ruota)
	ruota2 = T([1,2,3])([0,3.6,0.35])(ruota)
	
	ruote = STRUCT([ruota1,ruota2])
	ruote = T(1)([-0.05])(ruote)
	ruote3_4 = T(1)([1.5])(ruote)
	ruote = STRUCT([ruote,ruote3_4])
	ruote = COLOR(BLACK)(ruote)

	paraurtiAnteriore = CUBOID([1.8,0.05,0.8])
	paraurtiPosteriore = CUBOID([1.8,0.05,0.7])
	paraurtiPosteriore = T(3)([0.35])(paraurtiPosteriore)
	paraurtiAnteriore = R([2,3])(0.3489)(paraurtiAnteriore)
	paraurtiAnteriore = T([2,3])([4.5,0.35])(paraurtiAnteriore)

	portabagagli = CUBOID([1.8,0.9,0.05])
	portabagagli = T(3)([1.05])(portabagagli)

	cofano = CUBOID([1.8,1.5,0.05])
	cofano = T([2,3])([2.8,1.05])(cofano)
	

	car = STRUCT([telaio,paraurtiAnteriore,paraurtiPosteriore])
	car = STRUCT([car,portabagagli,cofano])

	scocca = MKPOL([[[0,0.9,0],[0.3,1.2,0.7],[0.3,2.5,0.7],[0,2.8,0]],[[1,2,3,4]],None])
	scocca2 = MKPOL([[[0,2.8,0],[0.3,2.5,0.7],[1.5,2.5,0.7],[1.8,2.8,0]],[[1,2,3,4]],None])
	scocca3 = MKPOL([[[1.8,0.9,0],[1.5,1.2,0.7],[1.5,2.5,0.7],[1.8,2.8,0]],[[1,2,3,4]],None])
	scocca4 = MKPOL([[[1.8,0.9,0],[1.5,1.2,0.7],[0.3,1.2,0.7],[0,0.9,0]],[[1,2,3,4]],None])
	scocca = STRUCT([scocca,scocca2,scocca3])
	scocca = STRUCT([scocca,scocca4])
	scocca = T(3)([1.05])(scocca)
	vetri = COLOR([93/255.0,188/255.0,210/255.0,1])(scocca)
	scoccaskel = SKELETON(1)(scocca)
	
	tetto = MKPOL([[[0.3,1.2,1.75],[0.3,2.5,1.75],[1.5,2.5,1.75],[1.5,1.2,1.75]],[[1,2,3,4]],None])
	car = STRUCT([car,tetto,scoccaskel])
	random1=randint(0,255)
	random2=randint(0,255)
	random3=randint(0,255)

	
	fiancata = MKPOL([[[0,0,0.35],[0,4.5,0.35],[0,4.3,1.05],[0,0,1.05]],[[1,2,3,4]],None])
	fiancata1 = MKPOL([[[0,0,0.35],[0,4.5,1.05],[0,4.3,0.35],[0,0,1.05]],[[1,2,3,4]],None])
	fiancata1 = R([1,3])(PI)(fiancata1)
	fiancata1 = T(3)([01.4])(fiancata1)
	fiancata2 = T(1)([1.8])(fiancata)
	#ruote = OFFSET([0.2,0.4])(ruote)
	car = STRUCT([car,fiancata1,fiancata2])

	car = MATERIAL([.01,.01,.01,1,  random1/255.0,random2/255.0,random3/255.0,1,  0,0,0,1, 0,0,0,1, 1])(car)

	faroPosteriore = CUBOID([0.4,0.05,0.2])
	faroPosteriore = T([1,2,3])([0.2,-0.05,0.7])(faroPosteriore)
	faroPosteriore2 = T([1,2,3])([1,0,0])(faroPosteriore)

	fari = STRUCT([faroPosteriore,faroPosteriore2])
	
	fariAnteriori = R([2,3])(0.3489)(fari)
	fariAnteriori = T(2)([4.7])(fariAnteriori)

	fariAnteriori = COLOR([236/255.0,237/255.0,280/255.0,1])(fariAnteriori)
	fari = COLOR(RED)(fari)

	car = STRUCT([car,fari,fariAnteriori])

	return STRUCT([car,ruote,vetri])

def main():
	VIEW(car())

if __name__=='__main__':
	main()
