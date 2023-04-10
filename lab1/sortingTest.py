"""
file: sortingTest.py
CSCI-665: Hw 1 Problem 5 Solution
Authors: Deepika Kini, Adith Shetty
language: python3
This program compares performance of 3 sorting algorithms across different distribution of input ranges.
"""
import math
import numpy as n
import time


def merge_sort(data):
    """
    Performs a merge sort and returns a newly sorted list.
    :param data: A list of data
    :return: A sorted list
    """
    # an empty list, or list of 1 element is already sorted
    if len(data) < 2:
        return data
    else:
        # split the data into left and right halves
        left, right = _split(data)

        # return the merged recursive mergeSort of the halves
        return _merge(merge_sort(left), merge_sort(right))


def _merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merges two sorted list, left and right, into a combined sorted result
    :param left: A sorted list
    :param right: A sorted list
    :return: One combined sorted list
    """

    # the sorted left + right will be stored in result
    result = []
    left_index, right_index = 0, 0

    # loop through until either the left or right list is exhausted
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # take the un-exhausted list and extend the remainder onto the result
    if left_index < len(left):
        result.extend(left[left_index:])
    elif right_index < len(right):
        result.extend(right[right_index:])

    return result


def _split(data: list[int]) -> tuple[list[int], list[int]]:
    """
    Split the data into halves and return the two halves
    :param data: The list to split in half
    :return: Two lists, cut in half
    """
    return data[:len(data) // 2], data[len(data) // 2:]


def insertion_sort(data):
    """
    Perform an in-place insertion sort of data.
    Note: Code referred from one of the CSCI603 Midterm Labs.
    :param data: The data to be sorted (a list)
    :return: None
    """
    # copying to avoid adding a reference

    sorted_region_index = 0
    for index in range(1, len(data)):
        for sorted_index in range(sorted_region_index, -1, -1):
            index_of_comparison = sorted_index + 1
            if data[index_of_comparison] > data[sorted_index]:
                break
            data[index_of_comparison], data[sorted_index] = data[sorted_index], data[index_of_comparison]
        sorted_region_index += 1
    return data


def bucket_sort(data):
    """
    Performs a bucket sort of data
    :param data: the data to be sorted
    :return:
    """
    n = len(data)
    linked_list_buckets = [[] for i in range(n)]
    # adding to buckets
    for i in range(n):
        linked_list_buckets[math.floor(n * data[i])].append(data[i])
    # print(linked_list_buckets)
    # sorting within buckets using insertion sort
    for i in range(n):
        # overwriting with sorted insertion sort output
        linked_list_buckets[i] = insertion_sort(linked_list_buckets[i])
    # print(linked_list_buckets)
    output = []
    for i in range(n):
        output.extend(linked_list_buckets[i])
    # print(output)


def create_list_uniform(number):
    return n.random.uniform(size=number)


def create_list_gaussian(number):
    return n.random.normal(0.5, 1 / 10000, number)


def run_sorting_algorithms(unsorted_list):
    """
    Runs all the sorting algorithms on the given data
    :param unsorted_list:
    :return:
    """
    times = []

    # Merge Sort
    list_merge = unsorted_list.copy()
    start = time.perf_counter()
    list_merge = merge_sort(list_merge)
    time_elapsed = time.perf_counter() - start
    times.append(time_elapsed)

    # Insertion Sort
    list_insertion = unsorted_list.copy()
    start = time.perf_counter()
    list_insertion = insertion_sort(list_insertion)
    time_elapsed = time.perf_counter() - start
    times.append(time_elapsed)

    # Bucket Sort
    list_bucket = unsorted_list.copy()
    start = time.perf_counter()
    list_bucket = bucket_sort(list_bucket)
    time_elapsed = time.perf_counter() - start
    times.append(time_elapsed)

    return times


def main():
    input_sizes = [100, 1000, 10000, 100000]
    times_uniform = []
    times_gaussian = []

    for size in input_sizes:
        test_list = create_list_uniform(size)
        times_uniform.append(run_sorting_algorithms(test_list))
        print(size)
        print(times_uniform[-1])

        test_list_guassian = create_list_gaussian(size)
        times_gaussian.append(run_sorting_algorithms(test_list_guassian))
        print(size)
        print(times_gaussian[-1])
        print("-------------------------------")

    for i in range(len(input_sizes)):
        print("size: ", input_sizes[i])

        print("Uniform Distribution")

        print("------Merge Sort------")
        print(times_uniform[i][0])
        print("----Insertion Sort----")
        print(times_uniform[i][1])
        print("-----Bucket Sort------")
        print(times_uniform[i][2])

        print("--------------------------------")
        print("Gaussian (normal) Distribution")

        print("------Merge Sort------")
        print(times_gaussian[i][0])
        print("----Insertion Sort----")
        print(times_gaussian[i][1])
        print("-----Bucket Sort------")
        print(times_gaussian[i][2])

        print("-------------------------------------")


if __name__ == '__main__':
    main()
