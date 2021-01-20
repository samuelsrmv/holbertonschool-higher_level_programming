#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """"module for print pascal triangle"""
    """
    if n < 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [[1], [1, 1]]
    """
    array = []

    for x in range(1, n + 1):
        array.append([1] * x)

    for j in range(2, n):
        row = array[j]
        anterior = array[j - 1]

        for k in range(1, len(row) - 1):
            row[k] = anterior[k - 1] + anterior[k]

    return array


"""
    print(array)
if __name__ == "__main__":
    print(pascal_triangle(4))
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
"""
