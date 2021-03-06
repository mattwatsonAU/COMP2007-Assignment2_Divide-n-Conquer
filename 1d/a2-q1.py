def merge(left, right):
    # We can assume the points in each segment are ordered by ascending y-coord.
    # as long as we maintain this order in our returned pointset. 
    merged = []
    # Input is rows of the form ((x,y),i): We split into points and importances.
    left, left_imp = zip(*left)
    right, right_imp = zip(*right)
    i = j = counter = 0
    Y_COORD = 1
    while len(merged) != len(left) + len(right):
        if right[j][Y_COORD] <= left[i][Y_COORD]:
            merged.append((right[j], right_imp[j] + counter))
            j += 1
        else:
            merged.append((left[i], left_imp[i]))
            counter += 1
			i += 1
			
        if i == len(left): # All left points have been included.
            merged += [(point, importance + counter)
                        for point, importance in zip(right[j:], right_imp[j:])]
        elif j == len(right): # All right points have been included
            merged += [(point, importance)
                        for point, importance in zip(left[i:], left_imp[i:])]
    return merged