def solution(A):
    distict_set = set()
    for i in xrange(0,len(A)):
        distict_set.add(abs(A[i]))
    return len(distict_set)


print solution([-5])