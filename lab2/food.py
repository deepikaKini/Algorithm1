"""
file: food.py
CSCI-665: Hw 2 Problem 5 Solution
Authors: Deepika Kini, Adith Shetty
language: python3
This program  determines if it will be possible to use all the donated food without any going to waste.
"""


def split(_list):
    if len(_list) == 2:
        return [_list[0]], [_list[1]]
    else:
        mid = len(_list) // 2
        return _list[:mid], _list[mid:]


def merge(left, right):
    l_index, r_index = 0, 0
    sorted_so_far = []

    while l_index < len(left) and r_index < len(right):
        if left[l_index][1] <= right[r_index][1]:
            sorted_so_far.append(left[l_index])
            l_index += 1
        else:
            sorted_so_far.append(right[r_index])
            r_index += 1

    if l_index < len(left):
        sorted_so_far.extend(left[l_index:])
    elif r_index < len(right):
        sorted_so_far.extend(right[r_index:])
    return sorted_so_far


def merge_sort(_list):
    if len(_list) <= 1:
        return _list
    else:
        left, right = split(_list)
        return merge(merge_sort(left), merge_sort(right))


def sort_food_by_actual_expiration(food_arrival_and_expiration):
    expirations = []
    for item in food_arrival_and_expiration:
        if item[0] == 0:
            expirations.append([item[0], item[1]])
        else:
            expirations.append([item[0], item[0] + (item[1] - 1)])

    return expirations


def heapify_up_test(_list, item_loc, curr_day):
    while item_loc > 0:
        if _list[item_loc][1] > _list[parent(item_loc)][1]:
            break
        elif _list[item_loc][1] == _list[parent(item_loc)][1]:

            # Making sure that the parent is consumed before it's expiry date to avoid clashing.
            _list[parent(item_loc)][1] -= 1

            if _list[parent(item_loc)][1] < curr_day:
                return False

            # update rest of the upper tree with.
            return heapify_up_test(_list, parent(item_loc), curr_day)

        else:
            _list[item_loc], _list[parent(item_loc)] = _list[parent(item_loc)], _list[item_loc]
            item_loc = parent(item_loc)
    return True


def heapify_down(_list, last_index):
    curr_index = 0
    while (left_child(curr_index) <= last_index and _list[curr_index][1] > _list[left_child(curr_index)][1]) or (
            right_child(curr_index) <= last_index and _list[curr_index][1] > _list[right_child(curr_index)][1]):
        if right_child(curr_index) > last_index or _list[left_child(curr_index)][1] < _list[right_child(curr_index)][1]:
            index = left_child(curr_index)
        else:
            index = right_child(curr_index)
        _list[curr_index], _list[index] = _list[index], _list[curr_index]
        curr_index = index


def parent(item_loc):
    return (item_loc - 1) // 2


def left_child(item_loc):
    return 2 * item_loc + 1


def right_child(item_loc):
    return 2 * item_loc + 2


def expiration_day(item):
    # return item
    return item[1] if item[0] == 0 else item[0] + (item[1] - 1)


def main():
    total_food_items = int(input())
    food_arrival_and_expiration = []

    for i in range(total_food_items):
        food_arrival_and_expiration.append(list(map(int, input().split(" "))))

    expirations = sort_food_by_actual_expiration(food_arrival_and_expiration)

    if test_2(total_food_items, expirations):
        print("YES")
    else:
        print("NO")


def test_2(total_food_items, items):
    food_consumed = 0
    # Day 0
    index = 0
    heap = []
    while index < total_food_items and items[index][0] == 0:
        heap.append(items[index])
        if heapify_up_test(heap, index, 1):
            index += 1
        else:
            return False

    curr_day = 0

    while food_consumed < total_food_items:
        if len(heap) == 0:
            # Updating current day to the next arrival day, since all other items have been consumed
            curr_day = items[index][0]
        else:
            curr_day += 1
            # Expiry Check
            if heap[0][1] < curr_day:
                return False

        # Adding in the items added on this day, if any
        while index < total_food_items and items[index][0] == curr_day:
            heap.append(items[index])
            if heapify_up_test(heap, len(heap) - 1, curr_day):
                index += 1
            else:
                return False

        # Consuming one of the food items
        heap[0], heap[-1] = heap[-1], heap[0]
        heap = heap[:-1]
        heapify_down(heap, len(heap) - 1)

        food_consumed += 1

    return True


if __name__ == '__main__':
    main()
