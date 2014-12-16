def binary_search(lst, num):
    if lst is None or len(lst) == 0:
        return -1

    left = 0
    right = len(lst) - 1
    mid = (right - left) // 2

    while True:
        if lst[mid] == num:
            return mid
        elif num > lst[mid] and right > mid:
            left = mid + 1
            mid = (right - left) // 2 + left
        elif num < lst[mid] and left < mid:
            right = mid - 1
            mid = (right - left) // 2 + left
        else:
            return -1
