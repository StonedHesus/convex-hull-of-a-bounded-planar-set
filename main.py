import numpy.random as rd
import matplotlib.pyplot as plt


def convex_hull(points):

    starting_vertex = starting_point(points)
    stack = sort_vertices(points, starting_vertex)
    hull = [points[starting_vertex], stack.pop()]

    while stack:

        third_point = stack.pop()
        second_point = hull[-1]
        first_point = hull[-2]

        while not is_turning_left(first_point, second_point, third_point):
            hull.pop()
            first_point, second_point = hull[-2], first_point
        hull.append(third_point)

    return hull

def sort_vertices(points, starting_vertex):
    stack = []

    for i in range(len(points)):
        if i != starting_vertex:
            temporary_stack = []
            while stack != [] and is_turning_left(points[starting_vertex], stack[-1], points[i]):
                temporary_stack.append(stack.pop())

            stack.append(points[i])
            while temporary_stack:
                # We put into stack what we placed into temporary_stack.
                stack.append(temporary_stack.pop())

    return stack


def starting_point(points):
    """

    Return the smallest number from a lexicographical point of view computed on the current universe of discourse.

    :param points:
    :return:
    """
    start = 0

    for index in range(1, len(points)):
        if points[index][0] < points[start][0] or \
                (points[index][0] == points[start][0] and points[index][1] < points[start][1]):
            start = index

    return start


def is_turning_left(first_point, second_point, third_point):
    # This answer is built using a vectorial geometry approach.
    return (second_point[0] - first_point[0]) * (third_point[1] - first_point[1]) >= \
           (second_point[1] - first_point[1]) * (third_point[0] - first_point[0])


def paint(number_of_points):
    figure = plt.figure()

    # We are creating a list of tuples which will contain all the points we are randomly generating.
    points = [(rd.random(), rd.random()) for index in range(number_of_points)]

    # We create two separate lists for the x-coordinates and the y-coordinates.
    x, y = [points[i][0] for i in range(len(points))], [points[i][1] for i in range(len(points))]
    plt.plot(x, y, ".")

    hull = convex_hull(points)
    hull.append(hull[0]) # This enables us to trace a contour which is complete.

    xx, yy = [hull[i][0] for i in range(len(hull))], [hull[i][1] for i in range(len(hull))]
    plt.plot(xx, yy)

    plt.title("Convex hull of a bounded planar set")
    plt.show()


if __name__ == '__main__':
    paint(67)
