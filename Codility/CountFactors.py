import math
def solution(N):
    # write your code in Python 2.7
    count = 0
    if N == 1:
        return 1
    for i in range(1,int(math.sqrt(N))+1):
        if N % i == 0:
            count += 1
    temp = int(math.sqrt(N))
    temp = float(temp)
    if math.sqrt(N) == temp:
        return count * 2 -1
    return count * 2
print solution(16)