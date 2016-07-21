# -*- coding: utf-8 -*-
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def prime_factors(num):
    factors = []
    divider = 2
    while num > 1:
        while num % divider == 0:
            print divider
            factors.append(divider)
            num /= divider
        divider = divider + 1

    return factors


if __name__ == "__main__":
    p = prime_factors(13195)
    print max(p)
    print "This is problem3"
