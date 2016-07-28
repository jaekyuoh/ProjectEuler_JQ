# -*- coding: utf-8 -*-
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(num):
    for k in range(2, num):
        if num % k == 0:
            return False
    return True

def ith_prime(num):
    current_num=2
    ith=0
    while True:
        if is_prime(current_num):
            ith += 1
            if ith == num:
                print ith
                return current_num
        current_num+=1

if __name__ == "__main__":


    result = ith_prime(10001)
    print result
    print "This is problem6"
