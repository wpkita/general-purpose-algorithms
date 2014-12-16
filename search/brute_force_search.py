def brute_force_search(lst, num):
    index_of = -1

    if lst is None or len(lst) == 0:
        return index_of

    for i in range(0, len(lst)):
        if lst[i] == num:
            return i

    return index_of
