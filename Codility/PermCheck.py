def solution(A):
    # write your code in Python 2.7
    max_element = max(A)
    permutation_list = range(1,max_element+1)
    A.sort()
    if len(A) != len(permutation_list):
        return 0
    for i in range(0,len(A)):
        if permutation_list[i] != A[i]:
            return 0
    return 1

if __name__ == '__main__':
    print solution([1,2,2,3,2,5])
