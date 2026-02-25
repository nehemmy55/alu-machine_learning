#!/usr/bin/env python3

""" CONCATENATING 2D MATRICES ALONG SPECIFIED AXIS """

def cat_matrices2D(mat1, mat2, axis=0):
  
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    if axis == 1 and len(mat1) != len(mat2):
        return None
    if axis == 0:
        result = []
        for elem in mat1:
            result.append(elem)
        for num in mat2:
            result.append(num)
        return result
    elif axis == 1:
        result = []
        for i in range(len(mat1)):
            result.append(mat1[i] + mat2[i])
        return result
