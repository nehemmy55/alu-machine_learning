#!/usr/bin/env python3

"""
concatenating 1D arrays
"""

def cat_arrays(arr1, arr2):

    result = []
    for num in arr1:
        result.append(num)
    for number in arr2:
        result.append(number)
    return result
