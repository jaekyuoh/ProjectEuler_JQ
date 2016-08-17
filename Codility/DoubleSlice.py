# def solution(A):
#     for i in range(0,len(A)):
#
#     pass

def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

print golden_max_slice([3,2,6,-1,4,5,-1,2])

