# def solution(X, A):
#     # write your code in Python 2.7
#     check_list = [0]*(X+1)
#     count = 0
#     for i in range(0,len(A)):
#         if A[i] <= X:
#             if check_list[A[i]] == 0:
#                 check_list[A[i]] = 1
#                 count += 1
#
#         if count == X:
#             return i
#     return -1


def solution(X, A):
    # write your code in Python 2.7
    leaf_set = set()
    for i in xrange(0,len(A)):
        if A[i] <= X:
            leaf_set.add(A[i])
            if len(leaf_set) == X:
                return i
    return -1


    pass


if __name__ == '__main__':
    # print solution(5,[1,3,1,4,2,3,5,4])
    print solution(3,[1,2,1])
    print max([1,3,1,4,2,3,5,4])