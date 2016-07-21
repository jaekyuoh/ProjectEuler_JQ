# -*- coding: utf-8 -*-
# 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?


def Fibonacci(n):
    if n == 1:
        print 1
        return 1
    elif n == 2:
        print 2
        # even_sum += 2
        return 2
    else:
        fibonacci = Fibonacci(n-1) + Fibonacci(n-2)
        print fibonacci
        return fibonacci


def fib(n):
    even_sum = 0
    a,b = 1,2
    for i in range(n-1):
        if a > 4000000:
            return a, even_sum
        a,b = b,a+b
        if (a % 2 == 0):
            even_sum += a
    return a, even_sum


if __name__ == "__main__":
    print "This is problem2"
    sequence, even = fib(100)
    print even

