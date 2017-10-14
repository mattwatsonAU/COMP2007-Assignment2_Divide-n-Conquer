from queue import PriorityQueue

n = int(input())

Q=PriorityQueue()

for _ in range(n):
    x, y = map(float, input().split())
    Q.put((x,y,0))

def compare(points):
	left=PriorityQueue()
	right=PriorityQueue()
	length=points.qsize()
	firsthalf=int((length/2))
	secondhalf=int(length-firsthalf)
	for _ in range(firsthalf):
		currL_point=points.get()
		left.put(currL_point)
	for _ in range(secondhalf):
		currR_point=points.get()
		right.put(currR_point)
	if length==2 :
		return merge(left,right)
	elif left.qsize()==1 and right.qsize()>1 :
		return merge(left, compare(right))
	else:
		return merge(compare(left), compare(right))


def merge(left,right):
	leftQ=PriorityQueue()
	rightQ=PriorityQueue()
	leftQA=PriorityQueue()
	rightQA=PriorityQueue()
	counter=0
	output=PriorityQueue()
	while not left.empty():
		next_item=left.get()
		imp=next_item[2]
		x=float(next_item[0])
		y=float(next_item[1])
		leftQ.put((y,x,int(imp)))
		leftQA.put((x,y,int(imp)))

	while not right.empty():
		next_item=right.get()
		imp=next_item[2]
		x=float(next_item[0])
		y=float(next_item[1])
		rightQ.put((y,x,int(imp)))

	while not leftQ.empty() and not rightQ.empty():
		left=leftQ.get()
		right=rightQ.get()
		leftX=left[0]
		rightX=right[0]
		
		if(leftX>rightX):
			leftQ.put(left)
			imp=right[2]+counter
			x=float(right[0])
			y=float(right[1])
			rightQA.put((y,x,imp))
		elif(leftX<rightX):
			counter+=1
			rightQ.put(right)

	if leftQ.empty() and not rightQ.empty():
		while not rightQ.empty():
			right=rightQ.get()
			imp=right[2]+counter
			x=float(right[0])
			y=float(right[1])
			rightQA.put((y,x,imp))

	while not leftQA.empty():
		next_item = leftQA.get()
		output.put(next_item)

	while not rightQA.empty():
		next_item = rightQA.get()
		output.put(next_item)
	return(output)

out = compare(Q)

while not out.empty():
	next_item=out.get()
	print(next_item[2])
