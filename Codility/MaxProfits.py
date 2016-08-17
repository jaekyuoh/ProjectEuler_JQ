def solution(A):
    if len(A) == 0:
        return 0
    max_profit = 0
    min_price = A[0]

    for item in A:
        min_price = min(min_price,item)
        max_profit = max(max_profit, item - min_price)
    return max_profit


def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

# print golden_max_slice([5,-7,3,5,-2,4,-1])


# print solution([23171,21011,21123,21366,21013,21367])
print solution([3,2,2,2,4,2,2,10,5,1])
print solution([3])
