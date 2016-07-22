# -*- coding: utf-8 -*-
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(product):
    number_str = str(product)
    for i in range(0,len(number_str)):
        if (number_str[i] != number_str[len(number_str)-1-i]):
            return False
    return True


def largest_palindrome():
    max_palindrome, num1, num2 = 0, 0, 0
    for i in range(1,999):
        for k in range(1,999):
            product = i*k
            if is_palindrome(product):
                if max_palindrome < product:
                    max_palindrome = product
                    num1 = i
                    num2 = k
    print num1, num2
    print max_palindrome

if __name__ == "__main__":
    largest_palindrome()
    print "This is problem4"