def product(A):
    return reduce(lambda x, y: x * y, A)

def solution(A):
    # write your code in Python 2.7
    A.sort()
    if len(A) == 3:
        return product(A)
    else:
        front = product(A[:3])
        end = product(A[len(A)-3:len(A)])
        front_two = product([A[0],A[1],A[len(A)-1]])
        end_two = product([A[0],A[len(A)-2],A[len(A)-1]])
        candidate_list = [front,end,front_two,end_two]
        return max(candidate_list)

print solution([-1,2,3,-4])
