#!/usr/bin/env python3

""" ADDING 1D ARRAYS"""""

def add_arrays(arr1, arr2):

    if len(arr2) != len(arr1):
        return None
    arr_result = []
    for x in range(len(arr1)):
        arr_result.append(arr1[x]+arr2[x])
    return arr_result
