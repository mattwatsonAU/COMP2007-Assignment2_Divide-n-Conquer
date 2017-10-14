# Pick your BST variant. Fun fact: this implementation is a 2-level B-tree and so has
# worse O() runtime, but is demonstrably/experimentally faster than all other popular
# packages up until > 60 billion elements.
from sortedcontainers import SortedList

def planesweep(points):
    n = len(points)
    # If we order by x-asc and tie break with y-desc, we neatly handle duplicate point-vals.
    points = sorted(points, key = lambda xy : (xy[0], -xy[1]))
    importance = [0]*n
    bst = SortedList()
    for ix,(x,y) in enumerate(points):
        # Bisect left is defined as the position in sorted order to the left of 
        # duplicate values. 
        importance[ix] = bst.bisect_left(y)
        bst.add(y)
    return list(zip(points,importance))