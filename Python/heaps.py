import heapq as hq


grades = [ 99, 100, 91, 97, 71, 77, 83, 88, 89, 86 ]


print(hq.nsmallest(3, grades))
print(f"These are the top 3 grades: {hq.nlargest(3, grades)}")
