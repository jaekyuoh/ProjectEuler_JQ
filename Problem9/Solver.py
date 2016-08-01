# -*- coding: utf-8 -*-
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.



def find_triplet(sum):
    for i in range(1,sum/2+1):
        if i > 1000:
            break
        for j in range(1, sum/2 + 1):
            if j > 1000:
                break
            for k in range(1, sum/2 + 1):
                if k > 1000:
                    break
                left = i**2 + j**2
                right = k**2

                if left == right:
                    if i+j+k == sum:
                        return i,j,k
if __name__ == '__main__':
    i,j,k = find_triplet(1000)
    print i,j,k
    result = i*j*k
    print result

    print "This is problem 9"