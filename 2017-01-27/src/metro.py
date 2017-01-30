from pyplasm import *

def metro():
	palo = COLOR(BLACK)(CYLINDER([0.05,3])(40))
	insegna = TEXTURE("texture/metro.png")(CUBOID([0.6,0.1,0.6]))
	insegna = T([1,2,3])([-0.3,-0.05,3])(insegna)
	return STRUCT([insegna,palo])

def main():
	VIEW(metro())

if __name__=='__main__':
	main()