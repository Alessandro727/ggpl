from pyplasm import *

""" resize is a function that can change the size of the door/window without altering the width of the object frame.
	@param x: array of distances on x axis
	@param y: array of distances on y axis
	@param dX: length of the final window on the x axis
	@param dY: length of the final window on the y axis """
def resize(x,y,dX,dY):
	sumX = sum(x)
	sumY = sum(y)

	for i in range(len(x)-2):
		x[i+1] = x[i+1]/(sumX/dX)
	for j in range(len(y)-2):
		y[j+1] = y[j+1]/(sumY/dY)

""" removeNegative is a function to remove the part of an object 
	which is located below the reference axis by removing the negative cells calculated through the object UKPOL 
	and it returns the original object without the bad part.
	@param ukpol: object UKPOL """
def remove_negative(ukpol):
	for cellIndex in range(len(ukpol[1])):
		for vertex in ukpol[1][cellIndex]:
			if (ukpol[0][vertex-1][1] < -0.01):
				ukpol[1][cellIndex] = [0,0]
	return MKPOL([ukpol[0], ukpol[1], 1])

""" make_arc is a function to realize the upper arc of a window. 
	@param dx: length of the final window on the x axis
	@param dy: length of the final window on the y axis
	@param dz: length of the final window on the z axis """
def make_arc(dx,dy,dz):
	arc = CIRCLE(dx/2.)([12,2])
	arc = R([1,3])(PI/2)(arc)
	arc = remove_negative(UKPOL(SKEL_1(arc)))
	arc = OFFSET([dy/3.,dy/3.,dy/3.])(arc)
	arc = R([1,3])(3*PI/2)(arc)
	arc = MAP([S1,S3,S2])(arc)
	arc = T([1,2,3])([dx/2.,dy/3., dz-dy/3.])(arc)
	arc = S(2)(dy/SIZE([2])(arc)[0])(arc)

	return arc


""" make_handle is a function for the creation of the door handle to represent. 
	The function returns handles that have a semi-elliptical shape. 
	@param dz: length of the final door on the z axis """
def make_handle(dz):
	handle = CIRCLE(2*dz/3.)([100,1])
	handle = R([1,3])(PI/2)(handle)
	handle = T(2)((-dz)/1.8)(handle)
	handle = remove_negative(UKPOL(SKEL_1(handle)))
	handle = OFFSET([0.1,0.05,0])(handle)
	handle = T(2)(-dz/20.)(handle)
	handle = remove_negative(UKPOL((handle)))

	return handle


""" ggpl_window is a function able to realize any type of rectangular window 
	thanks to two arrays with the distances of the various parts which is on the x axis and y axis 
	to an array with the occurrences of each part. 
	The function in question creates the window and adds a bow to produce the image to be displayed.
	@param xWindow: array with the distances of the various parts of the window on the x axis
	@param yWindow: array with the distances of the various parts of the window on the y axis 
	@param occurrencyWindow: array with the parties occurrences
	@param dx: length of the final window on the x axis 
	@param dy: length of the final window on the y axis
	@param dz: length of the final window on the z axis """
def ggpl_window(xWindow,yWindow, occurrencyWindow):

	def ggpl_window0(dx,dy,dz):
	
		window=STRUCT([CUBOID([0,0,0])])
		resize(xWindow,yWindow,dx,dz)
		for i in range(len(xWindow)):
			counterX=sum(xWindow[:i])
			for j in range(len(yWindow)):
				counterY=sum(yWindow[:j])
				if occurrencyWindow[j][i]==1:
					cube=CUBOID([xWindow[i],yWindow[j],dy])
					window=STRUCT([window,T([1,2])([counterX,counterY])(cube)])
		window = R([2,3])(PI/2)(window)
		window = T(2)(dy)(window)
		arc = make_arc(sum(xWindow)-dy/3.,dy,dz)

		VIEW(COLOR(Color4f([165/255.0,131/255.0,36/255.0,1.0]))(STRUCT([window,arc])))

	return ggpl_window0	

""" ggpl_window is a function able to realize any type of rectangular door 
	thanks to two arrays with the distances of the various parts which is on the x axis and y axis 
	to an array with the occurrences of each part. 
	The function in question creates the door and adds a handle to produce the image to be displayed.
	@param xDoor: array with the distances of the various parts of the door on the x axis
	@param yDoor: array with the distances of the various parts of the door on the y axis 
	@param occurrencyDoor: array with the parties occurrences
	@param dx: length of the final door on the x axis 
	@param dy: length of the final door on the y axis
	@param dz: length of the final door on the z axis """
def ggpl_door(xDoor,yDoor, occurrencyDoor):

	def ggpl_door0(dx,dy,dz):
	
		door=STRUCT([CUBOID([0,0,0])])
		resize(xDoor,yDoor,dx,dz)
		for i in range(len(xDoor)):
			
			counterX=sum(xDoor[:i])
			for j in range(len(yDoor)):
				counterY=sum(yDoor[:j])
				if occurrencyDoor[j][i]==1:
					cube=CUBOID([xDoor[i],yDoor[j],dy])
					door=STRUCT([door,T([1,2])([counterX,counterY])(cube)])
		door = R([2,3])(PI/2)(door)
		door = T(2)(dy)(door)
		handle = COLOR(GRAY)(make_handle(dz/2.5))
		handle = R([1,2])(PI)(handle)
		handle = T([1,2,3])([2*dx/2.7,0.03,dz/2])(handle)
		VIEW(STRUCT([door,handle]))

	return ggpl_door0	

	

			
		


if __name__=='__main__':
	x1=[.05,.003,.3,.8,.3,.003,.05,.25,.05]
	y1=[.1,.45,.15,.15,.15,.15,.15,.15,.15,.15,.15,.4,.1,.05]
	b1=[[1,0,1,1,1,0,1,1,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,0,1,0,1,0,1,0,1],[1,0,1,1,1,0,1,0,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1]]
	x=[.05,.4,.05,.4,.05,.4,.05,.4,.05]
	y=[.05,.4,.05,.4,.05,.4,.05,.4,.05]
	b=[[1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1]]
	ggpl_window(x,y,b)(1.5,0.2,1.5)
	ggpl_door(x1,y1,b1)(2,0.2,4)
	
