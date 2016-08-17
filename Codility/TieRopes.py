def solution(K,A):
    count = 0
    sum = 0
    for i in xrange(0,len(A)):
        sum += A[i]
        if sum >= K:
            count += 1
            sum = 0
    return count


print solution(4,[1,2,3,4,1,1,3])