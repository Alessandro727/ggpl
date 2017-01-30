from pyplasm import *

def distributore():
	pompa = CUBOID([2,8,0.25])
	pilastri = CUBOID([0.6,0.6,5])
	pilastri = T([1,2,3])([0.7,3.7,0])(pilastri)
	distributore = COLOR(GRAY)(CUBOID([0.8,0.6,1.5]))
	distributore2 = distributore
	distributore = T([1,2,3])([0.6,2.6,0])(distributore)
	distributore2 = T([1,2,3])([0.6,4.8,0])(distributore2)
	distributore = STRUCT([distributore,distributore2])
	stazione = STRUCT([pompa,pilastri,distributore])
	stazione2 = T(1)(4)(stazione)
	stazione3 = T(1)(7)(stazione)
	copertura = CUBOID([15,12,1])
	copertura = T([1,2,3])([-3,-2,5])(copertura)
	copertura = COLOR(YELLOW)(copertura)
	stazione = STRUCT([stazione,stazione2,stazione3])
	palo = (CYLINDER([0.3,5])(40))
	insegna = (CUBOID([2.5,0.6,2.5]))
	insegna = T([1,2,3])([-0.3,-0.3,5])(insegna)
	insegna = STRUCT([palo,insegna])
	insegna = T(2)(-5)(insegna)
	logo = TEXTURE("texture/logoEni.png")(CUBOID([2.5,0.1,2.5]))
	logo2 = logo
	logo = T([1,2,3])([-0.3,-5.4,5])(logo)
	logo2 = T([1,2,3])([-0.3,-4.6,5])(logo2)
	insegna = STRUCT([insegna,logo,logo2])
	logo3 = TEXTURE("texture/logoEni2.jpg")(CUBOID([0.1,2.5,1]))
	logo3 = T([1,2,3])([12,-2,5])(logo3)
	logo4 = T(1)(-15.1)(logo3)
	insegna = STRUCT([insegna,logo3,logo4])
	return STRUCT([stazione,copertura,insegna])


def main():
	VIEW(distributore())

if __name__=='__main__':
	main()