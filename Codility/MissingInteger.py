def solution(A):
    A.sort()
    B = []
    for i in range(0,len(A)):
        if A[i] > 0:
            B.append(A[i])

    if B == []:
        return 1
    if B[0] > 1:
        if A != B:
            return 1
        return B[0] - 1
    for i in range(0,len(B)-1):
        if abs(B[i]-B[i+1]) > 1:
            return B[i] + 1
    return B[len(B)-1] + 1



print solution([4,5])