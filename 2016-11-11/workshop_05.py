from larlib import *

def make_blackboard(dx,dy,dz):
	# This function is used to build a blackboard
	blackboard = CUBOID([dx,dy,dz])
	skel1 = SKEL_1(blackboard)
	skel1=(OFFSET([.05,.05,.05])(skel1))
	return STRUCT([skel1,COLOR(BLACK)(blackboard)])

def make_chair(dx,dy,dz):
	# This function is used to build a chair
	r = 0.025
	chair = []
	chairLeg = COLOR(GRAY)(CYLINDER([r,3*dz/4.0])(30))
	chair.append(chairLeg)
	chair.append(STRUCT([T([1,2,3])([dx,0,0]),COLOR(GRAY)(CYLINDER([r,3*dz/4.0])(30))]))
	chair.append(STRUCT([T([1,2,3])([0,dy,0]),COLOR(GRAY)(CYLINDER([r,dz/2.0])(30))]))
	chair.append(STRUCT([T([1,2,3])([dx,dy,0]),COLOR(GRAY)(CYLINDER([r,dz/2.0])(30))]))
	chair.append(STRUCT([T([1,2,3])([-r,-r,dz/2.0]),COLOR(Color4f([227/255.0,171/255.0,115/255.0,1.0]))(CUBOID([dx+2*r,dy+2*r,0.02]))]))
	chair.append(STRUCT([T([1,2,3])([-r,-r,3*dz/4.0]),COLOR(Color4f([227/255.0,171/255.0,115/255.0,1.0]))(CUBOID([dx+2*r,2*r,dz/4.0]))]))
	return STRUCT([STRUCT(chair)])


def make_desk(dx,dy,dz):
	# This function is used to build a desk
	r = 0.025
	desk = []
	deskLeg = COLOR(GRAY)(CYLINDER([r,dz])(30))
	desk.append(deskLeg)
	desk.append(STRUCT([T([1,2,3])([dx,0,0]),COLOR(GRAY)(deskLeg)]))
	desk.append(STRUCT([(T([1,2,3]))([0,dy,0]),COLOR(GRAY)(deskLeg)]))
	desk.append(STRUCT([(T([1,2,3]))([dx,dy,0]),COLOR(GRAY)(deskLeg)]))
	desk.append(STRUCT([(T([1,2,3]))([-r,-r,dz]),COLOR(Color4f([3/255.0,229/255.0,121/255.0,1.0]))(CUBOID([dx+2*r,dy+2*r,0.02]))]))
	desk.append(STRUCT([(T([1,2,3]))([0,0,dz-0.15]),COLOR(Color4f([202/255.0,135/255.0,53/255.0,1.0]))(CUBOID([dx,dy,0.01]))]))
	desk.append(STRUCT([(T([1,2,3]))([0,0,dz-0.15]),COLOR(Color4f([202/255.0,135/255.0,53/255.0,1.0]))(CUBOID([0.01,dy,0.1]))]))
	desk.append(STRUCT([(T([1,2,3]))([dx,0,dz-0.15]),COLOR(Color4f([202/255.0,135/255.0,53/255.0,1.0]))(CUBOID([0.01,dy,0.1]))]))
	desk.append(STRUCT([(T([1,2,3]))([0,dy,dz-0.15]),COLOR(Color4f([202/255.0,135/255.0,53/255.0,1.0]))(CUBOID([dx,0.01,0.1]))]))
	return STRUCT([STRUCT(desk)])

def make_desk_chair(dx,dy,dz):
	#this function is used to build a desk whit two chairs
	deskChairs = []
	deskChairs.append(STRUCT([T([1,2,3])([0,0.15,0]),make_desk(dx,dy,dz-0.15)]))
	deskChairs.append(STRUCT([T([1,2,3])([(dx-2*(dx/3.30)-0.15)/2,0,0]),(make_chair(dx/3.30,2*dy/3.0,dz))]))
	deskChairs.append(STRUCT([T([1,2,3])([(dx-2*(dx/3.30)-0.15)/2+dx/3.30+0.15,0,0]),(make_chair(dx/3.30,2*dy/3.0,dz))]))
	return STRUCT(deskChairs)

def make_teaching_post(dx,dy,dz):
	#This function is used to build a teaching post
	r = 0.025
	desk = []
	deskLeg = COLOR(GRAY)(CYLINDER([r,dz])(30))
	desk.append(deskLeg)
	desk.append(STRUCT([T([1,2,3])([dx,0,0]),COLOR(GRAY)(deskLeg)]))
	desk.append(STRUCT([(T([1,2,3]))([0,dy,0]),COLOR(GRAY)(deskLeg)]))
	desk.append(STRUCT([(T([1,2,3]))([dx,dy,0]),COLOR(GRAY)(deskLeg)]))
	desk.append(STRUCT([(T([1,2,3]))([-r,-r,dz]),COLOR(Color4f([202/255.0,135/255.0,53/255.0,1.0]))(CUBOID([dx+2*r,dy+2*r,0.02]))]))
	desk.append(STRUCT([(T([1,2,3]))([0,0,dz-0.15]),COLOR(Color4f([202/255.0,135/255.0,53/255.0,1.0]))(CUBOID([0.01,dy,-dz+0.4]))]))
	desk.append(STRUCT([(T([1,2,3]))([dx,0,dz-0.15]),COLOR(Color4f([202/255.0,135/255.0,53/255.0,1.0]))(CUBOID([0.01,dy,-dz+0.4]))]))
	desk.append(STRUCT([(T([1,2,3]))([0,dy,dz]),COLOR(Color4f([202/255.0,135/255.0,53/255.0,1.0]))(CUBOID([dx,0.01,-dz+0.2]))]))
	desk = STRUCT(desk)
	desk = T(2)(0.15)(desk)
	chair = make_chair(0.7,0.8,1.3)
	desk = STRUCT([desk,T([1,2,3])([(dx/2)-(0.35)]),(chair)])
	return desk
	
def make_floor(dx,dy,dz):
	# This function is used to build a floor
	tile = (CUBOID([.3,.3,0]))
	skel1 = SKEL_1(tile)
	skel1=COLOR(BLACK)(OFFSET([.005,.005,.005])(skel1))
	tile = STRUCT([skel1,COLOR(Color4f([210/255.0,246/255.0,249/255.0,1.0]))(tile)])
	floorX = tile
	x = 0.3
	while dx-x>=0.3:
		floorX = STRUCT([floorX,T(1)(x),tile])
		x += 0.3
	if dx-x!=0:
		finalTile = COLOR(Color4f([210/255.0,246/255.0,249/255.0,1.0]))(CUBOID([dx-x,0.3,0]))
		finalSkel = SKEL_1(finalTile)
		skel1=COLOR(BLACK)(OFFSET([.01,.01,.01])(finalSkel))
		finalTile = STRUCT([skel1,finalTile])
		floorX = STRUCT([floorX,T(1)(x),finalTile])
	y=.3
	floor = floorX
	while dy-y>=0.3:
		floor = STRUCT([floor,T(2)(y),floorX])
		y += 0.3
	if dy-y!=0:
		floorY = COLOR(Color4f([210/255.0,246/255.0,249/255.0,1.0]))(CUBOID([.3,dy-y,0]))
		skel1 = SKEL_1(floorY)
		skel1=COLOR(BLACK)(OFFSET([.01,.01,.01])(skel1))
		floorY = STRUCT([skel1,floorY])
		x = 0.3
		while dx-x>=0.3:
			floor = STRUCT([floor,T(1)(x),floorY])
			x += 0.3
	return floor

def make_bookcase(dx,dy,dz): 
	# This function is used to build a bookcase
	panel = COLOR(Color4f([195/255.0,125/255.0,17/255.0,1.0]))(CUBOID([0.1,dy,dz]))
	bookcase = STRUCT([panel,T(1)(dx-0.1),panel])
	panel2 = COLOR(Color4f([195/255.0,125/255.0,17/255.0,1.0]))(CUBOID([dx,dy,0.1]))
	bookcase = STRUCT([bookcase,T(3)(dz/3.0),panel2])
	bookcase = STRUCT([bookcase,T(3)(2*dz/3.0),panel2])
	bookcase = STRUCT([bookcase,T(3)(dz),panel2])
	book = COLOR(RED)(CUBOID([0.05,0.14,0.22]))
	book2 = COLOR(YELLOW)(CUBOID([0.05,0.14,0.22]))
	book3 = COLOR(GREEN)(CUBOID([0.05,0.14,0.28]))
	book4 = COLOR(MAGENTA)(CUBOID([0.05,0.14,0.25]))
	book5 = COLOR(BLUE)(CUBOID([0.06,0.14,0.22]))
	book6 = COLOR(GREEN)(CUBOID([0.03,0.14,0.22]))
	book7 = COLOR(Color4f([210/255.0,246/255.0,249/255.0,1.0]))(CUBOID([0.05,0.14,0.22]))
	book8 = COLOR(Color4f([167/255.0,89/255.0,105/255.0,1.0]))(CUBOID([0.05,0.14,0.22]))
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1,dy-0.14,dz/3.0+0.1]),book])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05,dy-0.14,dz/3.0+0.1]),book2])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05+0.05,dy-0.14,dz/3.0+0.1]),book3])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05+0.05+0.10,dy-0.14,dz/3.0+0.1]),book4])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05+0.05+0.10+0.06,dy-0.14,dz/3.0+0.1]),book5])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05+0.05+0.10+0.06+0.03,dy-0.14,dz/3.0+0.1]),book6])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05+0.05+0.10+0.06+0.03+0.05,dy-0.14,dz/3.0+0.1]),book7])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05+0.05+0.10+0.06+0.03+0.05+0.05,dy-0.14,dz/3.0+0.1]),book8])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1,dy-0.14,2*dz/3.0+0.1]),book4])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05,dy-0.14,2*dz/3.0+0.1]),book8])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05+0.05,dy-0.14,2*dz/3.0+0.1]),book2])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05+0.05+0.10,dy-0.14,2*dz/3.0+0.1]),book7])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05+0.05+0.10+0.06,dy-0.14,2*dz/3.0+0.1]),book])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05+0.05+0.10+0.06+0.03,dy-0.14,2*dz/3.0+0.1]),book3])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05+0.05+0.10+0.06+0.03+0.05,dy-0.14,2*dz/3.0+0.1]),book5])
	bookcase = STRUCT([bookcase,T([1,2,3])([0.1+0.05+0.05+0.10+0.06+0.03+0.05+0.05,dy-0.14,2*dz/3.0+0.1]),book6])
	return bookcase


def make_class(dx,dy,dz):
	# This function is to build a fully equipped classroom
	deskWidth = 1.5
	deskLength = 0.5
	awayFromTheWall = 0.5
	deskRow = T([1,2])([awayFromTheWall,0.4])(make_desk_chair(deskWidth,deskLength,0.7))
	distanceBetweenDesks = 0.5
	box = SKEL_1(CUBOID([dx,dy,dz]))
	lx = deskWidth+awayFromTheWall+distanceBetweenDesks
	while lx < (dx-awayFromTheWall):
		deskRow = STRUCT([deskRow,T([1,2])([lx,0.4]),make_desk_chair(deskWidth,deskLength,0.7)])
		lx += deskWidth+distanceBetweenDesks
	room = deskRow 
	ly = 0
	awayFromTheBlackboard = 3
	while ly < (dy-awayFromTheBlackboard):
		room = STRUCT([room,T(2)(ly),deskRow])
		ly += deskLength+distanceBetweenDesks

	teachingPost = T(1)(2.5)(R([1,2])(PI)(make_teaching_post(2.5,0.8,0.9)))
	blackboard = make_blackboard(dx/2,dz/3,0)
	blackboard = R([2,3])(PI/2)(blackboard)
	room = STRUCT([room,T([1,2,3])([dx/2-1.25,dy-1.5,0]),teachingPost])
	room = STRUCT([room,T([1,2,3])([dx/2-dx/4,dy,dz/2-dz/6]),blackboard])

	room = STRUCT([room,make_floor(dx,dy,dz)])
	bookcase = make_bookcase(1,0.2,1.5)
	bookcase = T([1,2,3])([0.2,2.5,0])(R([1,2])(PI/2)(bookcase))
	room = STRUCT([room,bookcase])
	VIEW(STRUCT([box,room]))
	

def main():
	make_class(12,8,3.2)
	

	
	
if __name__=='__main__':
	main()
