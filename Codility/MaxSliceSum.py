def solution(A):
    # write your code in Python 2.7
    max_sum = 0
    max_end = 0
    neg_count = 0
    for i in xrange(0,len(A)):
        if A[i] <= 0:
            neg_count+=1
        max_end = max(0, max_end + A[i])
        max_sum = max(max_sum, max_end)
    if neg_count == len(A):
        return max(A)
    return max_sum


print solution([-1,-1,-2,1,-2,-3])