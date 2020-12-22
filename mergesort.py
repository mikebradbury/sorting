#!/usr/bin/env python3

"""Mergesort in python3 using - recusive solution

Args:
    i[]: an unsorted list (array)

Returns:
    i[]: a list sorted by mergesort
"""

def mergesort(i):
    if not i:
        print("list is empty")
    elif len(i) == 1:
            return i
    elif len(i) == 2:
        if i[0] > i[1]:
            return [i[1], i[0]]
        else:
            return i

    half = len(i)//2
    right = mergesort(i[:half])
    left = mergesort(i[half:])

    sorted_list = []
    while True:
        if len(right) > 0 and len(left) > 0:
            if right[0] <= left[0]:
                sorted_list.append(right[0])
                right = right[1:]
            else:
                sorted_list.append(left[0])
                left = left[1:]
        elif len(right) > 0:
            sorted_list += right
            right = []
        elif len(left) > 0:
            sorted_list += left
            left = []
        else:
            break
    return sorted_list





i = [1,33,5467,23434534,8,4,5,6,1,111,11111,75675,3]

print(mergesort(i))
