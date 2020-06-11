def triangle_third_edge_range(len1, len2):
     
	max_r = len1 + len2
	min_r = max(len1,len2) - min(len1, len2)

	print("Third triangle edge range is ", (min_r, max_r))



triangle_third_edge_range(2, 9)
