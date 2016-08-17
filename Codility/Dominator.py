# def solution(A):
#     if A == []:
#         return -1
#     for i in xrange(len(A)-1):
#         if A[i] != '':
#             if A[i] != A[i+1]:
#                 A[i],A[i+1] = '',''
#
#
#     print A
#     #dominator =  filter(lambda x: x!='',A)[0]
#     length = len(filter(lambda x: x!='',A))
#     index = 0
#     for k in xrange(len(A)):
#         if A[k] != '':
#             index = k
#             break
#
#     if length > len(A)//2:
#         return k
#     else:
#         return -1

def solution(A):
    if A == []:
        return -1
    candidate_count = 0
    candidate = A[0]
    candidate_dict = {}
    candidate_dict[A[0]] = 1
    for i in xrange(1,len(A)):
        if A[i] == candidate:
            candidate_dict[candidate] += 1
        else:
            if not candidate_dict.has_key(A[i]):
                candidate_dict[A[i]] = 1
            else:
                candidate_dict[A[i]] += 1
                if candidate_dict[A[i]] > candidate_dict[candidate]:
                    candidate = A[i]
    candidate_count = candidate_dict[candidate]
    if candidate_count <= len(A)//2:
        return -1
    for i in xrange(0, len(A)):
        if A[i] == candidate:
            return i

print solution([1,1,2,2,2,2,3,4,5,3])


