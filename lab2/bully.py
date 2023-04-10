"""
file: bully.py
CSCI-665: Hw 2 Problem 3 Solution
Authors: Deepika Kini, Adith Shetty
language: python3
This program provides the bully cases (counts inversion) for the data provided
It mainly uses merge sort and counts the left array elements greater than
the right array element, hence making it a O(n*log(n)) algorithm
Note: the logic here is to make array in descending order

"""

def main():
    # number of items in the list
    count = int(input())
    # items present in the list
    count_bully_cases = 0
    numbers = list(map(int, input().strip().split()))  # O(n)
    #temp will hold smaller arrays in between -1 values
    temp = []
    #inversion count for each temp array evaluation
    inversion_count = 0
    #total inversion count
    final_inversion_count = 0
    for i in range(len(numbers)):
        # if -1 or end of input not encountered
        if numbers[i] != -1 and i != len(numbers) - 1:
            #append numbers in temp
            temp.append(numbers[i])
            inversion_count = 0


        else:
            #append the current number and call merge sort,
            #reinitialise temp
            # print("inside else ")
            temp.append(numbers[i])
            inversion_count, temp1 = merge_sort(temp)
            # print(temp)
            temp = []
            # print("if", inversion_count)
        #add inversion count of the round to final value
        final_inversion_count += inversion_count

    print(final_inversion_count)


def merge_sort(data):
    """
    Performs a merge sort and returns a newly sorted list.
    Logic for keeping track of #inversions added
    :param data: list of data
    :return: count of inversions and sorted list
    """
    # an empty list, or list of 1 element is already sorted
    if len(data) < 2:
        return (0, data)
    else:
        # split the data into left and right halves
        left, right = _split(data)
        # takes the counts for inversion in respective array and
        # adds them, return the merged recursive mergeSort of the halves

        invl, left_merged = merge_sort(left)
        invr, right_merged = merge_sort(right)
        invr = invr + invl
        return _merge(invr, left_merged, right_merged)


def _merge(inversion_count, left, right):
    """
    Merges two sorted list, left and right, into a combined sorted result
    :param inversion_count: the count
    :param left: a sorted list
    :param right: a sorted list
    :return:inversion count and sorted merged list
    """

    # the sorted left + right will be stored in result
    result = []
    left_index, right_index = 0, 0

    # loop through until either the left or right list is exhausted
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:  #changed the comparison operator to make it descending sorting
            result.append(left[left_index])
            left_index += 1

        #if equal, append left(priority to older kid) and increment left  pointer
        elif left[left_index] == right[right_index]:
            result.append(left[left_index])
            left_index += 1


        else:
            #if right value greater than left value, inversion count
            # will be incremented by number of elements remaining in left array
            result.append(right[right_index])
            inversion_count += len(left) - left_index
            right_index += 1

    # take the un-exhausted list and extend the remainder onto the result
    if left_index < len(left):
        result.extend(left[left_index:])

    elif right_index < len(right):
        result.extend(right[right_index:])

    return inversion_count, result


def _split(data):
    """
    Split the data into halves and return the two halves
    :param data: The list to split in half
    :return: Two lists, cut in half
    """
    return data[:len(data) // 2], data[len(data) // 2:]



if __name__ == '__main__':
    main()
