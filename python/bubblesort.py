def bsort(listn):
	for i in range(len(listn)):
		for j in range(i+1, len(listn)):
			if listn[i] > listn[j]:
				print("before: ", i, listn[i], j, listn[j])
				temp = listn[i]
				lnums[i] = listn[j]
				lnums[j] = temp
				print("after: ", i, listn[i], j, listn[j])
