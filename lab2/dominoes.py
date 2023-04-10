"""
file: dominoes.py
CSCI-665: Hw 4 Problem 3 Solution
Authors: Deepika Kini, Adith Shetty
language: python3
This program provides the solution for whether there exist two dominoes in this
set, call them a and b, along with a way to order each domino, call it a = {a1, a2}, b =
{b1, b2}, such that |a1 − b1| + |a2 − b2| ≤ T, for some given threshold, T
The code uses radix sorting

"""

def main():
    """
    the main function takes in the input and calls radix sort,
    plus computes the main logic of checking the differences
    with threshold
    :return:  None
    """
    # number of items in the list
    count_dominoes = int(input())
    # items present in the list
    t_value = int(input())
    max_x = 0
    max_y = 0
    boolean_output = False
    numbers = []

    for i in range(count_dominoes):
        #reading input
        numbers.append(list(map(int, input().strip().split())))
        #in each row containing (x,y), we consider x to contain max values
        #access last row and compare their x and y values
        if numbers[-1][0] < numbers[-1][1]: #O(1)
            numbers[-1][0], numbers[-1][1] = numbers[-1][1], numbers[-1][0]
        if numbers[-1][0] > max_x:
            max_x = numbers[-1][0]
        if numbers[-1][1] > max_y:
            max_y = numbers[-1][1]

    numbers = radix_sort(numbers, max_x, 0)
    output = compute_equation(numbers, t_value)


    if output == "YES":
        print("YES")

    else:
        #if not found a pair, sort on min column
        numbers = radix_sort(numbers, max_y, 1)
        output = compute_equation(numbers, t_value)
        print(output)


def compute_equation(numbers, t_value):
    """
     iterating over sorted list and comparing 2 consecutive dominoes against the equation
    :param numbers: the array
    :param t_value: the threshold value
    :return: string value if found a pair or not
    """
    i = 0
    j = 1
    boolean_output = False
    while j < len(numbers):
        # print(numbers[i][0], numbers[i][1])
        if abs(numbers[i][1] - numbers[j][1]) <= t_value - abs(numbers[i][0] - numbers[j][0]):
            boolean_output = True
            break
        else:
            i = j
            j += 1
    if boolean_output:
        return("YES")
    else:
        return("NO")

def radix_sort(numbers, max, index_to_sort_on):
    """
    radix sort sorts dominoes based on a column
    :param arr: the domino 2-d array
    :param max: the max value for particular column to be sorted on
    :param index_to_sort_on: mentions if to sort based on max or min value of domino
    :return:
    """
    max1= max
    count = 0
    #count of digits in max value of column
    while max1>= 1:
        count +=1
        max1 = max1 / 10
    # print("count",count)
    divide_term = 1
    #calls sorting for each digit position of the
    for i in range(count):
        divide_term =divide_term * 10
        #calls sorting for each position
        numbers = digit_wise_sort(numbers, index_to_sort_on, divide_term)
    return numbers

def digit_wise_sort(numbers, index_to_sort_on, divide_term):
    """
    Extension of radix sort that creates a chained linked list and buckets the 2d
    array based on digit sorting
    :param numbers: the array
    :param index_to_sort_on: column of 2 d array
    :param divide_term: the exponent of 10 to receive the digit
    :return:
    """
    #initialization of linked list for bucketing values over 0-9 for decimal numbers
    sorting_linked_list = [ [] for i in range(10) ]
    #term that removes unrequired poetion of intermediate number extracted
    subtracting_term = divide_term // 10

    #getting digit from number array and placing in buckets
    for i in range(len(numbers)):
        intermediate = numbers[i][index_to_sort_on] % divide_term
        if subtracting_term != 1:
            intermediate = intermediate // subtracting_term

        sorting_linked_list[intermediate].append(numbers[i])

    #sending numbers over to caller after putting all nodes from the linkedlist
    # in same sequence by traversing the buckets from 0-9

    numbers = []
    for i in range(10):
        numbers.extend(sorting_linked_list[i])

    return numbers




if __name__ == '__main__':
    main()
