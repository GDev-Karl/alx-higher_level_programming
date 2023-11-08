#!/usr/bin/python3
""" Pascal's Triangle function """


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        fig = triangles[-1]
        tmp = [1]
        for i in range(len(fig) - 1):
            tmp.append(fig[i] + fig[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
