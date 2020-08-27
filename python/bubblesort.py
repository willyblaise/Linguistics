def bsort(listn):
	for i in range(len(listn)):
		for j in range(i+1, len(listn)):
			if listn[i] > listn[j]:
				print("before: ", i, listn[i], j, listn[j])
				temp = listn[i]
				lnums[i] = listn[j]
				lnums[j] = temp
				print("after: ", i, listn[i], j, listn[j])

				
				
for i in range(len(blist)):
     for j in range(i+1, len(blist)):
             print(i, blist[i], j, blist[j])
             if blist[i] > blist[j]:
                     temp = blist[i]
                     blist[i] = blist[j]
                     blist[j] = temp
	print("after", blist[i], blist[j])
				
