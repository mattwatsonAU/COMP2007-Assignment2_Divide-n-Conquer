from queue import PriorityQueue

leftQ=PriorityQueue()
leftQA=PriorityQueue()
rightQ=PriorityQueue()
rightQA=PriorityQueue()
n = int(input())
l = int(input())

for _ in range(l):
    x, y, imp = map(float, input().split())
    leftQ.put((y,x,int(imp)))
    leftQA.put((x,y,int(imp)))

r = int(input())
for _ in range(r):
	x, y, imp = map(float, input().split())
	rightQ.put((y,x,int(imp)))

counter=0

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

#Print the results

while not leftQA.empty():
    next_item = leftQA.get()
    print(int(next_item[2]))

while not rightQA.empty():
    next_item = rightQA.get()
    print(next_item[2])