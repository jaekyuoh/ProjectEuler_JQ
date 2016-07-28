# -*- coding: utf-8 -*-
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def difference():
    sqr_of_sum = 0
    sum = 0
    sum_of_sqr = 0
    for i in range(1,101):
        sqr_of_sum += i**2
        sum += i
    sum_of_sqr = sum**2
    return sum_of_sqr-sqr_of_sum

if __name__ == "__main__":
    result = difference()
    print result
    print "This is problem 6"