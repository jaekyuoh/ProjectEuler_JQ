# def solution(A):
#     # write your code in Python 2.7
#     max_sum = 0
#     max_end = 0
#     neg_count = 0
#     for i in xrange(0,len(A)):
#         if A[i] <= 0:
#             neg_count+=1
#         max_end = max(0, max_end + A[i])
#         max_sum = max(max_sum, max_end)
#     if neg_count == len(A):
#         return max(A)
#     return max_sum
#
#
# def golden_max_slice(A):
#     max_ending = max_slice = 0
#     for a in A:
#         max_ending = max(0, max_ending + a)
#         max_slice = max(max_slice, max_ending)
#     return max_slice

# import sys
# def solution(A):
#     # write your code in Python 2.7
#
#     max_num = -1000000000
#     min_num = 1000000000
#     for a in A:
#         if max_num <= a:
#             max_num = a
#         elif min_num >=a:
#             min_num = a
#     return abs(max_num-min_num)
#
#
# def solution(A):
#     # write your code in Python 2.7
#
#     max_num = -1000000000
#     min_num = 1000000000
#     max_dict = {}
#     min_dict = {}
#     for i in xrange(0,len(A)-1):
#         if max_num <= A[i]:
#             max_num = A[i]
#         if min_num >= A[len(A)-2-i]:
#             min_num = A[len(A)-2-i]
#         max_dict[i] = max_num
#         min_dict[len(A)-2-i] = min_num
#         print 'max'
#         print max_dict
#         print 'min'
#         print min_dict
#
#     result = -1000000000
#     for k in xrange(0, len(max_dict)):
#         max_n = max_dict[k]
#         min_n = min_dict[k]
#         if result <= abs(max_n - min_n):
#             result = abs(max_n - min_n)
#     return result


def solution(A):
    # write your code in Python 2.7

    max_num = -1000000000
    max_num_prime = -1000000000
    max_dict = {}
    max_dict_prime = {}
    for i in xrange(0,len(A)-1):
        if max_num <= A[i]:
            max_num = A[i]
        if max_num_prime <= A[len(A)-1-i]:
            max_num_prime = A[len(A)-1-i]
        max_dict[i] = max_num
        max_dict_prime[len(A)-1-i] = max_num_prime
        print 'max'
        print max_dict
        print 'min'
        print max_dict_prime
    result = -1000000000
    for k in xrange(0, len(max_dict)):
        max_n = max_dict[k]
        min_n = max_dict_prime[k+1]
        if result <= abs(max_n - min_n):
            result = abs(max_n - min_n)
    return result

print solution([-1,-1,-4,-10])
# print solution([1,3])
print solution([4,3,2,5,1,1])
# print solution([1,3,-3])