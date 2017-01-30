from pyplasm import *
from src import albero as al

def palalottomatica():
	pala0 = CYLINDER([30,1])(30)
	pala = pala0
	for i in range(5):
	    pala = TOP([pala,pala0])
	pala = COLOR(WHITE)(SKELETON(1)(pala))
	interno = CYLINDER([30,6])(30)
	pala = COLOR(GRAY)(OFFSET([0.3,0.3,0.3])(pala))
	interno = COLOR([90/255.0,118/255.0,150/255.0,1])(interno)
	copertura = CONE([30,3.5])(50)
	copertura = T(3)([6])(copertura)
	copertura2 = CONE([8,3.5])(50)
	copertura2 = T(3)([7.5])(copertura2)
	copertura = STRUCT([copertura,copertura2])
	albero = al.albero()
	albero = T(1)([40])(albero)
	alberi = STRUCT([albero])
	for i in range(17):
		albero2 = R([1,2])((i+1)*20/57.324)(albero)
		alberi = STRUCT([alberi,albero2])
	pala = STRUCT([pala,interno,copertura])
	pala = S(3)([2])(pala)
	pala = STRUCT([pala,alberi])
	return pala

	

def main():
	VIEW(palalottomatica())

if __name__=='__main__':
	main()