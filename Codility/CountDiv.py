# def solution(A, B, K):
#     # write your code in Python 2.7
#     count = 0
#     for i in range(A,B+1):
#         if i % K == 0:
#             count += 1
#     return count


def solution(A, B, K):
    # write your code in Python 2.7
    if A%K == 0:
        answer = B/K - (A/K -1)
    else:
        answer = B / K - (A / K)
    return answer


print solution(1,1,11)