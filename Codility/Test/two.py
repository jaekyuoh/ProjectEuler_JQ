import sys

def solution(A):
    # write your code in Python 2.7
    if len(A) == 1:
        return -2
    A.sort()
    print A
    min_val = sys.maxsize
    for i in xrange(0,len(A)-1):
        if min_val > abs(A[i]-A[i+1]):
            min_val = abs(A[i]-A[i+1])
    if min_val > 100000000:
        return -1

    return min_val




print solution([0,3,3,7,5,3,11,1])
print solution([-9,-3,-5,-11])
print solution([-9,-3,-5,-11, 0, 10, 111])
print solution([-1,100000000])
print solution([0])