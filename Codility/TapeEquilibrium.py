# -*- coding: utf-8 -*-
import sys

def solver(A):
    min_diff = sys.maxsize
    total_sum = sum(A)
    temp_sum = 0
    for i in range(0,len(A)-1):
        temp_sum += A[i]
        diff = abs(temp_sum - (total_sum-temp_sum))
        if min_diff > diff:
            min_diff = diff
    return min_diff


if __name__ == '__main__':
    print solver([-1000,1000])
