import random
import sys
#assumption no duplicate ages
def select_rand(A, k):
    """
    as per algorithm provided in the lecture slides.
    This uses a random value to partition the array into 3 separate arrays.
    :param A: unsorted array input to find value in
    :param k: the index of value that needs to be retrieved
    :return: the kth value
    """
    print("k :",A,  k )
    random_index = random.randint(0, len(A) -1)
    L, E, G = [], [], []
    random_number_chosen = A[random_index]
    print("random value selected is :" , random_number_chosen)
    if len(A) == 1:
        return random_number_chosen
    for i in range(len(A)):
        if A[i] > random_number_chosen:
            G.append(A[i])
        elif  A[i] == random_number_chosen:
            E.append(A[i])
        else:
            L.append(A[i])
    print(L, E, G, len(L), len(E), len(G))
    if (k < len(L)):
        return select_rand(L, k)
    elif (k >= len(L) and k < len(L) + len(E)):
        return random_number_chosen
    else:
        return select_rand(G, k - len(L) - len(E))





def main():
    """
    takes the input
    :return:
    """
    no_of_kids = int(input())
    teacher1_wt =  float(input())
    teacher2_wt = float(input())
    print(no_of_kids, teacher1_wt, teacher2_wt)
    kids_array = []
    total_wt = teacher1_wt + teacher2_wt
    age_array = []
    for i in range(no_of_kids):
        kids_array.append(list(map(float, input().strip().split())))
        total_wt += kids_array[-1][1]
        age_array.append(kids_array[-1][0])

    print(kids_array, age_array)
    balance_value = total_wt / 2
    print("bal" , balance_value)
    if len(kids_array) % 2 == 0:
        k = len(kids_array) // 2  - 1 #check
    else:
        k = len(kids_array) // 2
        #passing only age in the select_rand method
    kth_value = select_rand(age_array, k)
    print(kth_value)


    wt_younger, wt_older = 0, 0
    count_left = 0

    # O(n)
    for i in range(len(kids_array)):
        if kids_array[i][0] < kth_value:
            wt_younger += kids_array[i][1]
            count_left += 1
        elif kids_array[i][0] > kth_value:
            wt_older += kids_array[i][1]
        else:
            wt_kth = kids_array[i][1]
    print("younger and older kids' weights:" , wt_younger,wt_older, wt_kth, wt_younger + wt_older +wt_kth , "count", count_left)
    #teacher 1 on left
    array_solution = []
    left1_1 = wt_younger + teacher1_wt + wt_kth
    right1_1 = wt_older + teacher2_wt
    no_kids_left1_1 = count_left + 1

    #swapping teachers
    left2_1 = wt_younger + teacher2_wt + wt_kth
    right2_1 = wt_older + teacher1_wt
    no_kids_left2_1 = count_left + 1

    # teacher 1 on left
    left1_2 = wt_younger + teacher1_wt
    right1_2 = wt_older + teacher2_wt + wt_kth
    no_kids_left1_2 = count_left


    # swapping teachers
    left2_2 = wt_younger + teacher2_wt
    right2_2 = wt_older + teacher1_wt + wt_kth
    no_kids_left2_2 = count_left

    distribution1_1 = abs(left1_1 - balance_value) + abs(right1_1 - balance_value)
    distribution2_1 = abs(left2_1 - balance_value) + abs(right2_1 - balance_value)
    distribution1_2 = abs(left1_2 - balance_value) + abs(right1_2 - balance_value)
    distribution2_2 = abs(left2_2 - balance_value) + abs(right2_2 - balance_value)
    print(distribution1_1, distribution2_1, distribution1_2, distribution2_2)
    print(no_kids_left1_1, no_kids_left2_1, no_kids_left1_2, no_kids_left2_2)
    array_solution.append([distribution1_1, no_kids_left1_1])
    array_solution.append([distribution2_1, no_kids_left2_1])
    array_solution.append([distribution1_2, no_kids_left1_2])
    array_solution.append([distribution2_2, no_kids_left2_2])
    max_students_on_left = 0
    found_balance = False
    optimal_balance_deviation = float(sys.maxsize)
    optimal_balance_count = sys.maxsize
    print(float(sys.maxsize))
    #O(const)
    for i in range(len(array_solution)):
        if int(array_solution[i][0]) == 0:
            if max_students_on_left < array_solution[i][1]:
                max_students_on_left = array_solution[i][1]
                found_balance = True
        else:
            if optimal_balance_deviation > array_solution[i][0]:
                print(optimal_balance_deviation, array_solution[i][0])
                optimal_balance_deviation = array_solution[i][0]
                optimal_balance_count = array_solution[i][1]


    #if total balance obtained on left and right print count
    #else go to find better balance if possible
    if found_balance: print(max_students_on_left)
    else:
        print("not fully balanced", optimal_balance_deviation, optimal_balance_count)
        if (len(kids_array) > 4):
            pass











if __name__ == '__main__':
    main()