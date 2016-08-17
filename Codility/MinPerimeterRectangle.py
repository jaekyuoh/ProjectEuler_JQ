import math
def solution(N):
    # find factors
    factors = []
    min_perimeter = N*N + 4
    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            factors.append(i)
    for k in factors:
        pair = N/k
        if min_perimeter > (pair + k)*2:
            min_perimeter = (pair + k)*2
    return min_perimeter

print solution(1)
