# def solution(N, M):
#     # write your code in Python 2.7
#     wrappers = []
#     current = 0
#     while current not in wrappers:
#         wrappers.append(current)
#         current = (current + M) % N
#     return len(wrappers)
#
# solution(10, 4)



def gcd(a, b):
    # Get the greatest common divisor
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)

def solution(N, M):
    print gcd(M,N)
    return N / gcd(M, N) # Least common multiple


print solution(10, 4)
