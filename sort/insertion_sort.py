from utility.list_utilities import *


def insertion_sort(lst):
    if lst is None:
        return None

    # cache length of list here
    lst_len = len(lst)

    if lst_len <= 1:
        return lst

    for i in range(1, lst_len):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                swap(lst, j, j - 1)
            else:
                break
    return lst
