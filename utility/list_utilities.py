def swap(lst, first_index, second_index):
    temp = lst[first_index]
    lst[first_index] = lst[second_index]
    lst[second_index] = temp
