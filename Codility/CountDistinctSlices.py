# import math
#
# def solution(M,A):
#     prev = 0
#     count = 0
#     if len(A) == 1:
#         return 1
#     for i in xrange(0,len(A)-1):
#         if A[i] == A[i+1] or A[i+1] == A[prev]:
#             count += sum(range(1,prev + 1-i+1))
#             prev = i + 1
#             print count
#         elif i+1 == len(A)-1:
#             print i, prev
#             count += sum(range(1,prev + 1 - i +1+1))
#             print count
#
#
#     return count

def solution(M,A):
    count = 0
    history = {}
    if len(A) == 1:
        return 1
    for i in xrange(0,len(A)):
        if history.has_key(A[i]):
            # count and reset dict
            count += sum(range(0,len(history)+1))
            if count >= 1000000000:
                return 1000000000
            history = {}
        if i == len(A) -1:
            history[A[i]] = 1
            count += sum(range(0, len(history) + 1))
            if count >= 1000000000:
                return 1000000000

        history[A[i]] = 1


    return count

print solution(100000, [3,4,5,5,5,2])
# print solution(100000, [1,1])

