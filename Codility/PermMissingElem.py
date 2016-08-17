def solution(A):
    # write your code in Python 2.7
    sum_A = sum(range(1,len(A)+2))
    temp_sum = 0
    for item in A:
        temp_sum += item
    return sum_A - temp_sum

if __name__ == '__main__':
    print solution([1,3,2,5])
    x = [1,2,3,4]
