# def solution(A):
#     dict1 = {}
#     dict2={}
#     list1 = []
#     list2 = []
#     max_key1 = A[0]
#     max_key2 =A[-1]
#     for i in range(0,len(A)):
#         #compute which one is leader
#         if dict1.has_key(A[i]):
#             dict1[A[i]] += 1
#             if dict1[max_key1] < dict1[A[i]]:
#                 max_key1 = A[i]
#         else:
#             dict1[A[i]] = 1
#         list1.append(max_key1)
#         print dict1
#         print list1
#
#         if dict2.has_key(A[len(A)-1-i]):
#             dict2[A[len(A)-1-i]] += 1
#             if dict2[max_key2] < dict2[A[len(A)-1-i]]:
#                 max_key2 = A[len(A)-1-i]
#         else:
#             dict2[A[len(A)-1-i]] = 1
#         list2.append(max_key2)
#         print dict2
#         print list2
#     return list1,list2.reverse()
def solution(A):
    for i in range(0, len(A)-1):
        list1 = A[:i+1]
        list2 = A[i+1:]

        print list1,list2

solution([4,3,4,4,4,2])
