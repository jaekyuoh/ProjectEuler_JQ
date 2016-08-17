

def solution(N, A):
    # write your code in Python 2.7
    counters = [0] * N
    hold_max = 0
    max_num = 0

    for i in range(0,len(A)):
        if A[i] <= N and A[i] >=1:
            if hold_max > counters[A[i]-1]:
                counters[A[i]-1] = hold_max
            counters[A[i]-1] += 1
            if counters[A[i]-1] > max_num:
                max_num = counters[A[i]-1]
        elif A[i] == N+1:
            hold_max = max_num
    for k in range(0, N):
        if counters[k] < hold_max:
            counters[k] = hold_max
    return counters

# def solution(N, A):
#     # write your code in Python 2.7
#     counters = [0] * N
#
#     max_num = 0
#
#     for i in range(0,len(A)):
#         if A[i] <= N and A[i] >=1:
#             counters[A[i]-1] += 1
#             if counters[A[i]-1] > max_num:
#                 max_num = counters[A[i]-1]
#         elif A[i] == N+1:
#             counters = [max_num] * N
#
#     return counters

print solution (5,[3,4,4,6,1,4,4])