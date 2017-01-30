from pyplasm import * 
from random import randint

def base():
    return STRUCT([COLOR([161/255.0,111/255.0,78/255.0,1])((PROD([CIRCLE(0.95)([30,1]),Q(0.02)]))),
           T(3)(0.03)(COLOR(RED)(TORUS([0.9,1.0])([30,3])))
           ])

def foglie():
    celement = T(3)(0.2)(R([1,2])(PI)(S(3)(2)(SPHERE(0.3)([8,8]))))
    sramo = (CYLINDER([0.1,0.8])(15))
    sram = STRUCT([sramo,S([1,2,3])([2.9,2.9,2.3])(celement)])
    sramo = T(1)(0.15)(R([1,3])(-1*PI/4)(sramo))
    sramo = STRUCT([sramo,T(1)(0.7)(S([1,2,3])([3,3,2])(celement))])
    for i in range(5):
        el = R([1,2])(i*2*PI/5)(sramo)
        sram = STRUCT([sram,el])
    sram = T(3)(4.5)(sram)
    random = randint(1,4)
    sram = TEXTURE("texture/foglie"+str(random)+".jpg")(sram)
    return sram

def tronco():
	return TEXTURE("texture/tronco.jpg")(CYLINDER([0.2,5])(40))

def albero():
	return STRUCT([base(),foglie(),tronco()])

def main():
	VIEW(albero())

if __name__=='__main__':
	main()