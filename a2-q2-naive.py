def naive(points):
    n = len(points)
    importance = [0] * n
    for ix,(x,y) in enumerate(points):
        importance[ix] = len([1 for other_x, other_y in points
                                if x > other_x and y > other_y])
    return zip(points, importance)
