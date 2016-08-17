# -*- coding: utf-8 -*-

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def get_factorial(num):
    return reduce(lambda x, y: x * y, range(1,num+1))

def solve(limit,factorial_dict):
    result = []
    for i in range(3,limit+1):
        digit_list = map(int, str(i))
        fact_list = []
        for k in digit_list:
            fact_list.append(factorial_dict[k])
        if i == sum(fact_list):
            result.append(i)
    print result

if __name__ == '__main__':
    factorial_dict = {0: 0, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
    solve(9999999, factorial_dict)

    print "This is problem 34"