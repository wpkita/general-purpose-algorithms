from utility.list_utilities import *


def get_index_of_minimum(lst):
    index_of_minimum = -1
    minimum = float('inf')

    for i in range(len(lst) - 1, -1, -1):
        if lst[i] <= minimum:
            minimum = lst[i]
            index_of_minimum = i

    return index_of_minimum


def selection_sort(lst):
    if lst is None:
        return None

    lst_len = len(lst)

    if lst_len <= 1:
        return lst

    for i in range(0, lst_len - 1):
        index_of_minimum = get_index_of_minimum(lst[i:])
        swap(lst, index_of_minimum + i, i)

    return lst
