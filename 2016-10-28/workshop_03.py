from larlib import *

def ggpl_spiral_staircase(dx,dy,dz):
	"""ogni 3 metri di piano 8 scalini"""
	nstep = int(dy*2.7)-1
	""" steps parameters """
	stepWidth = dx*0.33
	riserHeight = (0.50*dy)/nstep
	treadDept = (0.6300-riserHeight)/2.0
	""" number of steps and length of landing for each side """
	nsteplatox = int(((dx-2*stepWidth)/treadDept)+0.5) 
	landingLengthX=dy-((nstep+1)*treadDept)
	landingLengthY=dx-((nsteplatox)*treadDept)-stepWidth
	nsteplatoy = int(((dy-stepWidth-landingLengthX)/treadDept)+0.5)
	""" skeleton of the box that contains the stair """
	box = SKEL_1(CUBOID([dx,dy,dz]))
	""" total steps """
	totalSteps = int((dz/riserHeight))
	""" number of floor """
	nfloor = int(round(dz/2)+1)
	""" first stair """
	firstStair=make_stair(nstep-1,treadDept,riserHeight,landingLengthX+treadDept,stepWidth,1)
	stairs = [firstStair]
	""" variable that takes into account the number of steps made """
	realizedStep = nstep
	x=0
	sideX=0
	floorX = 0
	floorY = 0

	""" realization of the stairs """
	for j in range(int(nfloor+2)):
		""" condition for the realization of the final stair """
		if (totalSteps-realizedStep<=nsteplatox) or (totalSteps-realizedStep<=nsteplatoy):
			nfloor = floorX+floorY+1
			finalStair= make_stair((totalSteps-realizedStep-nfloor+1),treadDept,riserHeight,0,stepWidth,2)
			
			if nfloor%2==0:
				if (nfloor-2)%4==0:
					""" rotation and translation of the scale in the correct position """
					finalStair = R([1,2])((PI))(finalStair)
					finalStair = STRUCT([(T([1,2,3])([dx,dy-stepWidth+treadDept,(floorX)*(nsteplatox)*riserHeight+(floorY)*(nsteplatoy+1)*riserHeight+nstep*riserHeight+riserHeight])),finalStair])
				if (nfloor-2)%4==2:
					""" rotation and translation of the scale in the correct position """
					finalStair = R([1,2])((2*PI))(finalStair)
					finalStair = STRUCT([(T([1,2,3])([0,stepWidth,(floorX)*(nsteplatox+1)*riserHeight+(floorY)*(nsteplatoy+1)*riserHeight+(nstep)*riserHeight])),finalStair])
			
			else:
				if (nfloor-2)%4==1:
					""" rotation and translation of the scale in the correct position """
					finalStair = R([1,2])(PI/2)(finalStair)
					finalStair = STRUCT([(T([1,2,3])([dx-stepWidth,0,nstep*riserHeight+(floorX)*(nsteplatox+1)*riserHeight+(floorY)*(nsteplatoy+1)*riserHeight-riserHeight])),finalStair])
				if (nfloor-2)%4==3:
					""" rotation and translation of the scale in the correct position """
					finalStair = R([1,2])(3*PI/2)(finalStair)
					finalStair = STRUCT([(T([1,2,3])([stepWidth,dy,nstep*riserHeight+(floorX)*(nsteplatox+1)*riserHeight+(floorY)*(nsteplatoy+1)*riserHeight-riserHeight])),finalStair])	
				
			stairs.append(finalStair)
			return STRUCT([STRUCT(stairs),box])
		else:
			if j%2==0: 
				stairx = make_stair(nsteplatox,treadDept,riserHeight,landingLengthY,stepWidth,0)
				""" rotation of the scale in the correct position """
				stairx = R([1,2])((j+1)*3*PI/2)(stairx)
				stair2 = stairx
				if j == 0:
					""" translation of the scale in the correct position """
					stair2 = STRUCT([(T([1,2,3])([(stepWidth-treadDept),dy-(j)*(dy-landingLengthX+treadDept),(j+1)*((nstep-1)*riserHeight)])),stair2])
					
				else:
					if j%4==0:
						""" translation of the scale in the correct position """
						stair2 = STRUCT([(T([1,2,3])([(stepWidth-treadDept),dy,(j-2)*((nsteplatoy+nsteplatox+1)*riserHeight)+nstep*riserHeight])),stair2])
						
					else:
						""" translation of the scale in the correct position """
						stair2 = STRUCT([(T([1,2,3])([dx-stepWidth+treadDept,0,((j-1)*((nsteplatoy+nsteplatox+1)*riserHeight))+(nstep)*riserHeight])),stair2])
						
				stairs.append(stair2)
				""" addition number of realizaed steps """
				realizedStep += nsteplatox
				""" addition number of stairs on x-side """
				floorX += 1

			else:
				stairy = make_stair(nsteplatoy,treadDept,riserHeight,landingLengthX,stepWidth,1)
				""" rotation of the scale in the correct position """
				stairy = R([1,2])((j+1)*PI/2)(stairy)
				stair3 = stairy
				if (j+1)%4!=0:
					""" translation of the scale in the correct position """
					stair3 = STRUCT([(T([1,2,3])([dx,dy-stepWidth+treadDept,nstep*riserHeight+(j-x)*(nsteplatox+1)*riserHeight+(j-x-1)*nsteplatoy*riserHeight])),stair3])
					x+=2
				else:
					""" translation of the scale in the correct position """
					stair3 = STRUCT([(T([1,2,3])([0,stepWidth-treadDept,nstep*riserHeight+(j-1)*(nsteplatox+1)*riserHeight+(j-2)*nsteplatoy*riserHeight])),stair3])
					
				realizedStep += nsteplatoy
				floorY += 1
				stairs.append(stair3)

	return STRUCT([STRUCT(stairs),box])

""" function for the realization of the stair """
def make_stair(nstep,treadDept,riserHeight,landingLength,stepWidth,n):
	""" realization of the first step """
	step = MKPOL([[[0,0],[0,riserHeight],[2*treadDept,riserHeight], [treadDept,0]],[[1,2,3,4]],1])
	step = PROD([QUOTE([stepWidth]),step])
	stair = [step]
	if n == 0:
		stair = []
	""" realization total step """
	for i in range(nstep):
		stair.append(T([2,3])([treadDept,riserHeight]))
		stair.append(step)
	if n!=2 :
		stair.append(T([2,3])([(treadDept),(riserHeight)]))
		stair.append(CUBOID([stepWidth,landingLength,riserHeight]))
	return STRUCT(stair)


def main():
	VIEW(ggpl_spiral_staircase(6,5,10))

if __name__=='__main__':
	main()