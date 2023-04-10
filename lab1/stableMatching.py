"""
file: oneMatch.py
CSCI-665: Hw 1 Problem 4 Solution
Authors: Deepika Kini, Adith Shetty
language: python3
This program determines the number of elements from the first set that have only
one valid partner in the stable matching problem
"""


def invert_matrix(pref_two_inverted, pref_two, count):
    """
    :param pref_two_inverted:the empty matrix for holding inverted
            preference list of responder set
    :param pref_two: the matrix containing preference list for
                    responder set
    :param count: the count of entities in the set
    :return: None
    """
    for i in range(count):
        for j in range(count):
            pref_two_inverted[i][pref_two[i][j]] = j

def main():
    """
    The main function takes in the inputs and initializes data structures for the two runs
    :return: None
    """
    #take the count of entites in the sets
    count = int(input())
    #initialize the lists
    pref_one,pref_two, pref_two_inverted = [], [], []
    #take preference lists of the first set - O(n^2)
    for i in range(count):
        temp = list(map(int, input().strip().split(" ")))
        pref_one.append(temp )
        for j in range(count):
            pref_one[i][j] = pref_one[i][j]

    # take preference lists of the second set - O(n^2)
    for i in range(count):
        temp = list(map(int, input().strip().split(" ")))
        pref_two.append(temp )
        for j in range(count):
            pref_two[i][j] = pref_two[i][j]
        #initializing the inverted list
        pref_two_inverted.append([0 for _ in range(count)])

    #create inverse list for second pref list
    invert_matrix(pref_two_inverted, pref_two, count)

    # print(pref_two, pref_two_inverted)
    #lists to hold matched pairs for set one and two, init to -1  - O(n)
    list_one_matched_with = [-1 for i in range(count)]
    list_two_matched_with = [-1 for i in range(count)]

    #pointer to pref list for each asker for the next responder to be asked
    asker_next_ask = [0 for _ in range(count)]

    #stack holding askers that are free
    asker_unmatched_stack = [i for i in range(count -1 ,-1, -1)]
    #stack_two_unmatched = [i for i in range(count -1, -1, -1)]
    # print(list_one_matched_with, list_two_matched_with,"\n", pref_one, pref_two_inverted)


    def stable_match():
        """
        The Gale Shapely algorithm is implemented in O(n^2) complexity
        :return:
        """
        while asker_unmatched_stack != [] :
            current_asker = asker_unmatched_stack.pop()
            # print(current_asker)
            student_to_ask = pref_one[current_asker][asker_next_ask[current_asker]]
            # print(student_to_ask)
            asker_next_ask[current_asker] += 1
            # print("//",  pref_two_inverted[student_to_ask][list_two_matched_with[student_to_ask]],pref_two_inverted[student_to_ask][current_asker] )
            if list_two_matched_with[student_to_ask] == -1:
                list_two_matched_with[student_to_ask] = current_asker
                list_one_matched_with[current_asker] = student_to_ask
            elif list_two_matched_with[student_to_ask] != -1 and pref_two_inverted[student_to_ask][list_two_matched_with[student_to_ask]] >\
                    pref_two_inverted[student_to_ask][current_asker]:
                #the one prev matched with student needs to be pushed onto stack and unmatch it
                list1_unmatched = list_two_matched_with[student_to_ask]
                asker_unmatched_stack.append(list1_unmatched)
                # print(asker_unmatched_stack, "stack")
                list_one_matched_with[list1_unmatched] = -1
                list_two_matched_with[student_to_ask] = current_asker
                list_one_matched_with[current_asker] = student_to_ask
            else:
                #push the current asker again so that he can go to the next responder in his pref list
                asker_unmatched_stack.append(current_asker)


    #Round 1
    stable_match()
    # print(list_one_matched_with, list_two_matched_with)

    #round 2 - swap asker and responder lists and initialize the data structures
    list_one_matched_with_2 = list_one_matched_with #O(n)
    list_two_matched_with_2 = list_two_matched_with
    #reinitialize
    list_one_matched_with = [-1 for i in range(count)]
    list_two_matched_with = [-1 for i in range(count)]
    asker_next_ask = [0 for _ in range(count)]
    asker_unmatched_stack = [i for i in range(count - 1, -1, -1)]

    #swap lists
    pref_one, pref_two = pref_two, pref_one

    #get invested list for pref_two
    invert_matrix(pref_two_inverted, pref_two, count)

    stable_match()

    # checking the pref_list outputs
    count_of_el_same_partners = 0

    for i in range(count):
        if list_one_matched_with[i] == list_two_matched_with_2[i]:
            count_of_el_same_partners += 1
            list_two_matched_with_2[i]

    print(count_of_el_same_partners)



if __name__ == '__main__':
    main()
