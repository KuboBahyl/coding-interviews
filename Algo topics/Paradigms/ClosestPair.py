# closest pair problem - given 2D [x,y] points, find the closest ones
points = [[0, 5], [0, 2], [0.5, 3], [1, 3], [1, 2.7], [1.5, 4], [2, 1], [2, 3], [2.5, 2], [3, 0], [3, 3], [3.5, 1],
          [4, 4], [4, 1]]
import matplotlib.pyplot as plt

plt.scatter([arr[0] for arr in points], [arr[1] for arr in points])
from math import sqrt, inf


# O(N^2) solution
def closest_pair(points):
    def calc_distance(point_1, point_2):
        x_squared = (point_1[0] - point_2[0]) ** 2
        y_squared = (point_1[1] - point_2[1]) ** 2
        return sqrt(x_squared + y_squared)

    def brute_force(points):
        if len(points) == 2:
            return calc_distance(points[0], points[1])
        if len(points) == 3:
            dist_min = inf
            for i in range(3):
                for j in range(3):
                    if i != j:
                        dist_ij = calc_distance(points[i], points[j])
                        if dist_ij < dist_min:
                            dist_min = dist_ij
            return dist_min

    def merge_points(points_left, points_right, dist_min):
        mid_x = points_right[0][0]

        strip_left = []
        for i in range(len(points_left)):
            point = points_left[i]
            if point[0] > mid_x - dist_min:
                strip_left.append(point)

        strip_right = []
        for i in range(len(points_right)):
            point = points_right[i]
            if point[0] < mid_x + dist_min:
                strip_right.append(point)

        for point_left in strip_left:
            for point_right in strip_right:
                dist = calc_distance(point_left, point_right)
                if dist < dist_min:
                    dist_min = dist

        return dist_min

    def divide_recursively(points):
        N = len(points)

        # escaping condition
        if N <= 3:
            return brute_force(points)

        # divide
        mid = N // 2
        points_left = points[:mid]
        points_right = points[mid:]

        # recursion
        dist_left = divide_recursively(points_left)
        dist_right = divide_recursively(points_right)
        dist_min = min(dist_left, dist_right)

        # merge
        return merge_points(points_left, points_right, dist_min)

    N = len(points)
    return divide_recursively(points)


closest_pair(points)

# there is also the O(n logn logn) solution - same as this, but we sort srip[] and find the min more effectively