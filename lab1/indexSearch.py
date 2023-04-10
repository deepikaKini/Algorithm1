"""
file: indexSearch.py
CSCI-665: Hw 1 Problem 3 Solution
Authors: Deepika Kini, Adith Shetty
language: python3
This program determines if there exists an integer k in an array A, such that A[k] = k
"""


def index_search(arr, start, end):
    """
    Searches the array for a valid value which is equal to its index.
    Works recursively, where each call splits the array to search in half, thereby performing in O(log(n)) or o(n)

    :param arr: Array of integers
    :param start: start index
    :param end: end index
    :return bool:
    """
    # No elements are remaining to be checked.
    if end < start:
        return False
    # index to compare - midpoint
    index = (end + start) // 2
    # A[k] = k check
    if arr[index] == index + 1:
        print(index)
        return True
    # Discarding the left half of the array if A[k]<k
    elif arr[index] < index + 1:
        return index_search(arr, index + 1, end)
    # Discarding the right half of the array if A[k]>k
    elif arr[index] > index + 1:
        return index_search(arr, start, index - 1)


def main():
    # number of items in the list
    count = int(input())
    # items present in the list
    numbers = list(map(int, input().strip().split(" ")))  # O(n)
    output = index_search(numbers, 0, count - 1)
    if output:
        print("TRUE")
    else:
        print("FALSE")


if __name__ == '__main__':
    main()
