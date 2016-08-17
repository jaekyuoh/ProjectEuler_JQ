def solution(A):
    # write your code in Python 2.7
    first_car = A[0]
    rate = 1
    total = 0
    for i in range(1,len(A)):
        if A[i] == first_car:
            rate += 1
        else:
            total += rate
    if total > 1000000000:
        return -1
    return total


print solution([1,0])