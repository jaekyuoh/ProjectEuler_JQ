def solution(A):
    # write your code in Python 2.7
    A.sort()
    return len(set(A))
