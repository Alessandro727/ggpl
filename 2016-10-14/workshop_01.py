from larlib import * 

def make_struct((px,py),by,pillar_distances, beam_interstory_heights):
	
	""" array for the pillar foundations """
	pillar_array = [px]
	for value in pillar_distances:
		pillar_array = pillar_array+[-value]+[px]
	
	""" x-axis of the pillar """
	x_base_pillar = QUOTE(pillar_array)
	
	""" y-axis of the pillar """
	y_base_pillar = QUOTE([py])

	xy_base_pillar = PROD([x_base_pillar, y_base_pillar])

	""" array for the z-axis of the pillar """
	heights_pillar = []
	for value in beam_interstory_heights:
		heights_pillar = heights_pillar+[value+px]
	
	""" z-axis of the pillar """
	z_base_pillar = QUOTE(heights_pillar)

	pillars = PROD([xy_base_pillar, z_base_pillar])

	""" array for the realization of the beams """
	beam_struct = [ -x for x in pillar_array]
	
	""" x-axis of the beams """
	x_base_beam = QUOTE(beam_struct)

	""" y-axis of the beams """
	y_base_beam = QUOTE([by])

	xy_base_beam = PROD([x_base_beam, y_base_beam])

	""" array for distance between the beams """
	beams_distance = []
	for value in beam_interstory_heights:
		beams_distance = beams_distance+[-value]+[by]

	beams = PROD([xy_base_beam, QUOTE(beams_distance)])

	struct = STRUCT([pillars, beams])
	
	return struct
	


def main():
	VIEW(make_struct((0.4,0.4),(0.4),[1,1,5,2],[2,2,1,4]))

if __name__=='__main__':
	main()