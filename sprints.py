import math

def MyFunc(myList):
	
	found = False
	
	total = 0
	count = 0
	max_float = -math.inf

	for num in myList:
		if type(num) is int:
			total += num
			count += 1
			found = True
		elif type(num) is float:
			max_float = max(max_float, num)
			found = True
	if count > 0:
		mean = total/count
	if found:
		return mean, max_float
	else:
		return 0
