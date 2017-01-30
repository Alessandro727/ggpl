from pyplasm import * 

def prova():
	step1 = MKPOL([[[0,0],[0,0.2],[2*0.15,0.2], [0.15,0]],[[1,2,3,4]],1])
	step = PROD([QUOTE([0.4]),step1])
	handrail = CIRCUMFERENCE(0.4/15.0)(20)
	handrail = PROD([QUOTE([0.5]),handrail])
	handrail = T([1,2,3])([0.4-(0.4/15.0),0.2/2,0.15])(handrail)
	handrail = R([1,3])(PI/2)(handrail)
	handrailTop = PROD([QUOTE([0.4/15.0]),step1])
	#handrailTop = T([1,3])([0.4-(0.4/15.0),0.8])(handrailTop)
	VIEW(handrailTop)

prova()