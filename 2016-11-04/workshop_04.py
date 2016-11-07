from pyplasm import *
import math

# The following function takes as input a list of vertices and returns as output the same list 
# with values adjusted to eliminate the wrong values caused by UKPOL function.
def fixVerts(verts):
	for v in verts:
		v[0]=math.fabs(round(v[0],2))
		v[1]=math.fabs(round(v[1],2))
		v[2]=math.fabs(round(v[2],2))
	return verts

# The following function deletes duplicates vertices within the "verts" list made by UKPOL function.
def deleteDuplicates(verts):
	vertsNoDuplicates = []
	for n in verts:
		exists = 0
		for g in vertsNoDuplicates:
			if n==g:
				exists = 1
		if exists == 0:
			vertsNoDuplicates.append(n)
	return vertsNoDuplicates

# The 'order ()' function takes as input a list of vertices and sorts them according to the value of the z component. 
# If two or more vertices have the same z then they are sorted according to their x component. 
# Finally, even if they have the same x, they are sorted according to the y component.
def order(verts):
	newVerts = sorted(verts, key=lambda item: (item[2],item[0],item[1]))
	return newVerts


# The 'ggpl_build_roof ()' function takes as input a HPC object (the Polygonal shape of the roof)
# and returns outputs a HPC object (the roof builded).
# Depending on the type of the input object the function is able to create a different type of roof.
def ggpl_build_roof(roof):
	
	# skeleton of the roff in 2D 
	skel2 = SKEL_2(roof)
	verts, cells, pol = UKPOL(skel2)
	
	# adjusted to the values of the vertices
	verts = fixVerts(verts)
	
	# roof structure
	skel1 = SKEL_1(roof)
	skel1=COLOR(RED)(OFFSET([.1,.1,.3])(skel1))

	# order verts whitout duplicates
	vertsNoDuplicates = order(deleteDuplicates(verts))

	
	# Depending on the verts length field used to realize the input object in the function realizes a different type of roof. 
	# Finally he realizes the ultimate roof ordering every time the list of vertices to it being given the correct place in the list.
	print vertsNoDuplicates

	if len(vertsNoDuplicates)==6: #Gamble/Hip
		cellsTemp = []
		cellsTemp.append([5,2,1])
		cellsTemp.append([6,3,4])
		cellsTemp.append([6,5,3,1])
		cellsTemp.append([2,4,5,6])
		finalRoof = MKPOL([vertsNoDuplicates,cellsTemp,1])
		return [skel1,COLOR(RED)(finalRoof)]

	if len(vertsNoDuplicates)==4: #Shed
		cellsTemp = []
		cellsTemp.append([1,2,3,4])
		finalRoof = MKPOL([vertsNoDuplicates,cellsTemp,1])
		return [skel1,COLOR(RED)(finalRoof)]

	if len(vertsNoDuplicates)==8: #Mansard/Flat
		cellsTemp = []
		cellsTemp.append([2,1,5,6])
		cellsTemp.append([3,4,7,8])
		cellsTemp.append([7,5,3,1])
		cellsTemp.append([2,4,6,8])
		cellsTemp.append([5,6,7,8])
		finalRoof = MKPOL([vertsNoDuplicates,cellsTemp,1])
		return [skel1,COLOR(RED)(finalRoof)]

	if len(vertsNoDuplicates)==9: #Lroof
		cellsTemp = []
		cellsTemp.append([7,2,1,8])
		cellsTemp.append([8,4,2])
		cellsTemp.append([7,4,3,8])
		cellsTemp.append([3,6,7,9])
		cellsTemp.append([5,6,9])
		cellsTemp.append([1,5,7,9])
		finalRoof = MKPOL([vertsNoDuplicates,cellsTemp,1])
		return [skel1,COLOR(RED)(finalRoof)]

	if len(vertsNoDuplicates)==10: #Gambrel
		print 10
		cellsTemp = []
		cellsTemp.append([1,5,3,7])
		cellsTemp.append([10,9,7,5])
		cellsTemp.append([6,8,9,10])
		cellsTemp.append([2,4,6,8])
		finalRoof = MKPOL([vertsNoDuplicates,cellsTemp,1])
		return [skel1,COLOR(RED)(finalRoof)]

	if len(vertsNoDuplicates)==12: #Butterfly
		cellsTemp = []
		cellsTemp.append([5,9,3,1])
		cellsTemp.append([6,1,10,3])
		cellsTemp.append([7,9,5,11])
		cellsTemp.append([6,8,10,12])
		cellsTemp.append([2,4,8,12])
		cellsTemp.append([2,4,7,11])
		cellsTemp.append([7,5,2,1])
		cellsTemp.append([1,2,6,8])
		cellsTemp.append([3,4,9,11])
		cellsTemp.append([12,10,4,3])
		finalRoof = MKPOL([vertsNoDuplicates,cellsTemp,1])
		return [skel1,COLOR(RED)(finalRoof)]

	if len(vertsNoDuplicates)==14: #CombinationRoof
		cellsTemp = []
		cellsTemp.append([1,5,6,2])
		cellsTemp.append([3,4,7,8])
		cellsTemp.append([7,3,5,1])
		cellsTemp.append([2,4,6,8])
		cellsTemp.append([10,9,6,5])
		cellsTemp.append([7,8,11,12])
		cellsTemp.append([12,10,8,6])
		cellsTemp.append([5,7,9,11])
		cellsTemp.append([13,10,9])
		cellsTemp.append([11,12,14])
		cellsTemp.append([9,13,11,14])
		cellsTemp.append([14,13,12,10])
		finalRoof = MKPOL([vertsNoDuplicates,cellsTemp,1])
		return [skel1,COLOR(RED)(finalRoof)]


def main():
	verts = [[0,0,0],[0,8,0],[0,0,2],[0,8,2],[16,0,0],[16,8,0],[16,0,2],[16,8,2],[4,3,5],[12,3,5],[4,5,5],[12,5,5],[5,4,8],[11,4,8]]
	cells = [[1,3,4,2],[7,5,3,1],[5,7,6,8],[2,4,6,8],[11,9,4,3],[3,7,9,10],[7,8,10,12],[8,4,11,12],[9,10,13,14],[14,13,12,11],[11,9,13],[10,12,14],[2,6,1,5]]
	roof = MKPOL([verts,cells,None])
	VIEW(STRUCT(ggpl_build_roof(roof)))

if __name__=='__main__':
	main()