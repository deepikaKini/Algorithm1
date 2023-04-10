"""
file: colinear.py
CSCI-665: Hw 3 Problem 3 Solution
Authors: Deepika Kini, Adith Shetty
language: python3
"""


def get_input():  # O(n)
    n = int(input())
    cords = []
    for _ in range(n):
        cords.append(tuple(list(map(int, input().split(" ")))))
    return n, cords


def pointSearch(sorted_list, point):  # O(log(n))
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == point:
            return True
        elif sorted_list[mid][0] == point[0]:
            if point[1] > sorted_list[mid][1]:
                left = mid + 1
            else:
                right = mid - 1
        elif point[0] > sorted_list[mid][0]:
            left = mid + 1
        else:
            right = mid - 1
    return False


def co_linear_exists(n, cords):  # O(n^2(log(n)))
    for point1 in range(n):  # O(n)
        for point2 in range(n):  # O(n)
            if point1 != point2:
                midpoint = ((cords[point1][0] + cords[point2][0]) / 2, (cords[point1][1] + cords[point2][1]) / 2)
                if pointSearch(cords, midpoint):  # O(log(n))
                    return "YES"
    return "NO"


def co_linear_exists_set(cords):  # O(n^2)
    for point1 in cords:  # O(n)
        for point2 in cords:  # O(n)
            if point1 != point2:
                midpoint = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)
                if midpoint in cords:  # O(1)
                    return "YES"
    return "NO"


def main():
    n, cords = get_input()  # O(n)

    y_sorted = sorted(cords, key=lambda c: c[1])  # O(n(log(n)))
    x_sorted = sorted(y_sorted, key=lambda c: c[0])  # O(n(log(n)))

    print(co_linear_exists(n, x_sorted))  # O(n^2(log(n)))

    # print(co_linear_exists_set(set(cords))) # O(n^2)


if __name__ == '__main__':
    main()
