from pyplasm import *

def ggpl_spiral_staircase(dx,dy,dz):

	nstep = int(dy*2.7)+1
	riserHeight = (0.50*dy)/nstep
	treadDept = (0.6300-riserHeight)/2.0
	landingLengthY=dy-((nstep+1)*treadDept)
	stepWidth = landingLengthY
	nsteplatox = int(((dx-2*stepWidth)/treadDept)+0.5) 
	landingLengthX=stepWidth
	nsteplatoy = int(((dy-stepWidth-landingLengthY)/treadDept)+0.5)
	totalSteps = int((dz/riserHeight))
	nfloor = int(round(dz/2)+1)
	heightfloor = (nstep)*riserHeight
	stair=make_stair(nstep-1,treadDept,riserHeight,landingLengthY+treadDept,stepWidth,1)
	realizedStep = nstep
	r =4
	for j in range(int(nfloor)*2):
		if (totalSteps-realizedStep<=nsteplatox) or (totalSteps-realizedStep<=nsteplatoy):
			if (totalSteps-realizedStep<=nsteplatox) and r%2==1:
				finalStair = make_stair((totalSteps-realizedStep-1),treadDept,riserHeight,dy-stepWidth-(totalSteps-realizedStep-1)*treadDept,stepWidth,2)
			else:
				finalStair = make_stair((totalSteps-realizedStep-1),treadDept,riserHeight,dx-stepWidth-(totalSteps-realizedStep-1)*treadDept,stepWidth,2)
			if r==4:
				finalStair=R([1,2])(3*PI/2)(finalStair)
				finalStair = T([1,2,3])([stepWidth-treadDept,dy,heightfloor])(finalStair)
				stair = STRUCT([stair,finalStair])
				break
			if r==1:
				finalStair = R([1,2])(PI)(finalStair)
				finalStair = T([1,2,3])([dx,dy-landingLengthY+treadDept ,heightfloor])(finalStair)
				stair = STRUCT([stair,finalStair])
				break
			if r==2:
				finalStair = R([1,2])(PI/2)(finalStair)
				finalStair = T([1,2,3])([dx-landingLengthY+treadDept,0,heightfloor])(finalStair)
				stair = STRUCT([stair,finalStair])
				break
			if r==3:
				finalStair = T([1,2,3])([0,stepWidth-treadDept,heightfloor])(finalStair)
				stair = STRUCT([stair,finalStair])
				break

		else:
			if j%4== 0:
				stepsX = make_stair(nsteplatox,treadDept,riserHeight,landingLengthX,stepWidth,1)
				stepsX = R([1,2])(3*PI/2)(stepsX)
				stepsX = T([1,2,3])([stepWidth-treadDept,dy,heightfloor])(stepsX)
				stair = STRUCT([stair,stepsX])
				heightfloor += (nsteplatox+1)*riserHeight 
				realizedStep += nsteplatox+1
				r=1
			if j%4== 1:
				stepsY = make_stair(nsteplatoy,treadDept,riserHeight,dy-nsteplatoy*treadDept-stepWidth,stepWidth,1)
				stepsY = R([1,2])(PI)(stepsY)
				stepsY = T([1,2,3])([dx,dy-landingLengthY+treadDept ,heightfloor])(stepsY)
				stair = STRUCT([stair,stepsY])
				heightfloor += (nsteplatoy+1)*riserHeight 
				realizedStep += nsteplatoy+1
				r=2
			if j%4== 2:
				stepsX = make_stair(nsteplatox,treadDept,riserHeight,landingLengthX,stepWidth,1)
				stepsX = R([1,2])(PI/2)(stepsX)
				stepsX = T([1,2,3])([dx-landingLengthY+treadDept,0,heightfloor])(stepsX)
				stair = STRUCT([stair,stepsX])
				heightfloor += (nsteplatox+1)*riserHeight 
				realizedStep += nsteplatox+1
				r=3
			if j%4== 3:
				stepsY = make_stair(nsteplatoy,treadDept,riserHeight,landingLengthY,stepWidth,1)
				stepsY = T([1,2,3])([0,stepWidth-treadDept,heightfloor])(stepsY)
				stair = STRUCT([stair,stepsY])
				heightfloor += (nsteplatoy+1)*riserHeight 
				realizedStep += nsteplatoy+1
				r=4
		
	floor = CUBOID([dx,dy,0.05])
	floor = TEXTURE("texture/floorStair.jpg")(floor)

	return STRUCT([stair,floor])


def make_stair(nstep,treadDept,riserHeight,landingLength,stepWidth,n):
	""" realization of the first step """
	step = MKPOL([[[0,0],[0,riserHeight],[2*treadDept,riserHeight], [treadDept,0]],[[1,2,3,4]],1])
	step1 = MKPOL([[[0,0],[0,riserHeight],[treadDept,2*riserHeight], [treadDept,riserHeight]],[[1,2,3,4]],1])
	step = PROD([QUOTE([stepWidth]),step])
	step = TEXTURE("texture/Liptus.jpg")(step)
	handrailTop = PROD([QUOTE([stepWidth/15.0]),step1])
	handrail = CIRCLE(stepWidth/30.0)([20,20])

	handrail = PROD([QUOTE([1]),handrail])
	
	handrail = R([1,3])(PI/2)(handrail)
	handrail = T([1,2,3])([stepWidth-(stepWidth/30.0),treadDept/2,riserHeight])(handrail)
	handrail = COLOR(BLACK)(handrail)
	step = STRUCT([step,handrail])
	handrailTop = R([2,3])(PI)(handrailTop)
	handrailTop = T([1,2,3])([stepWidth-(stepWidth/15.0),treadDept,1+2*riserHeight])(handrailTop)
	handrailTop = TEXTURE("texture/Liptus.jpg")(handrailTop)
	step = STRUCT([step,handrailTop])
	stair = [step]
	if n == 0:
		stair = []
	""" realization total step """
	for i in range(nstep):
		step = T([2,3])([treadDept,riserHeight])(step)
		stair.append(step)
	finalStep = T([2,3])([(treadDept*(nstep+1)),(riserHeight*(nstep))])(CUBOID([stepWidth,landingLength,riserHeight]))
	finalStep = TEXTURE("texture/Liptus.jpg")(finalStep)
	stair.append(finalStep)
	return STRUCT(stair)


def main():
	VIEW(ggpl_spiral_staircase(6,4,3))

if __name__=='__main__':
	main()

