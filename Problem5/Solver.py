# -*- coding: utf-8 -*-
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import sys
def solver():
    num_list = range(1, 21)
    i = len(num_list)
    while True:
        count = 0
        for k in range(1, 21):
            if (i % k == 0):
                count += 1
        if (count == 20):
            return i
        i += 1
    return 0


if __name__ == "__main__":
    result = solver()
    print result
    print "This is problem5"