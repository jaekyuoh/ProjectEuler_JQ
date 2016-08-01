# -*- coding: utf-8 -*-
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


def is_prime(num):
    for k in range(2, num):
        if num % k == 0:
            return False
    return True

def find_primes_sum(limit):
    prime_list = []
    for i in range(2,limit+1):
        if is_prime(i):
            prime_list.append(i)
    return sum(prime_list)


if __name__ == '__main__':
    result = find_primes_sum(2000000)
    print result
    print "This is problem 10"