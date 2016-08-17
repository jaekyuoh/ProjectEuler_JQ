import math

def gcd(a, b):
    # Get the greatest common divisor
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)

def is_prime(num):
    for k in xrange(2, int(math.sqrt(num))+1):
        if num % k == 0:
            return False
    return True


def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice


def caterpillarMethod(A, s):
    n = len(A)
    front, total = 0, 0
    for back in xrange(n):
        while (front < n and total + A[front] <= s):
            total += A[front]
            front += 1
            print front,total

        if total == s:
            return True
        total -= A[back]
        print A[back]
    return False

print caterpillarMethod([6,2,7,4,1,3,6],12)



