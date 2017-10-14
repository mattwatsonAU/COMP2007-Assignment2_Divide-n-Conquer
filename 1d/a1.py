n = int(input())
points = []
for _ in range(n):
    p = int(input())
    points.append(p)

def makeheap(array, size, index):
	largest_importance = index
	left = (2 * index) + 1
	right = (2 * index) + 2

	if left < size and array[index] < array[left]:
		largest_importance = left

	if right < size and array[largest_importance] < array[right]:
		largest_importance = right

	if largest_importance != index:
		array[index],array[largest_importance] = array[largest_importance],array[index]
		makeheap(array, size, largest_importance)

def heapsort(array, size):
	for i in range(size, -1, -1):
		makeheap(array, size, i)

	for i in range(size-1, 0, -1):
		array[i], array[0] = array[0], array[i]
		makeheap(array, i, 0)

def importance(input,n):
	
	heapsort(input,n) # use heapsort to sort our list of points from smallest to largest importance
	
	for i in range(n):
		if(i==0):
			duplicateImportance=0 # initialise a counter to keep track of matching point importances
			numLowerPoints = i
			print(numLowerPoints)
		
		elif(points[i]==points[i-1]):
			duplicateImportance+=1
			print(numLowerPoints)

		elif(points[i]>points[i-1]):
			numLowerPoints = numLowerPoints+duplicateImportance+1
			print(numLowerPoints)
			duplicateImportance=0 # reset our counter of matching point importances as this is will be the first iteration of this importance value

importance(points,n)