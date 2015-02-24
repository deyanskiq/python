def tetrahedron_filled(tetrahedrons, water):
	var=0
	br=0
	tetrahedrons.sort()
	for numbers in tetrahedrons:
		v=(tetrahedrons[var]**3*(2**0.5))/12000
		if v<water:
			br=br+1
			water=water-v
		var=var+1
	print (br)


print (tetrahedron_filled([1000,10],10))