import math
def solution(X,Y):
    result = 0
    if X ==0 or Y ==0:
        temp_sum = abs(X)*2 + abs(Y)*2
    temp_sum = abs(X) + abs(Y)
    if temp_sum%2 ==0:
        print result

        result = abs(temp_sum * abs(X - 1 + X))
        if (X == Y):
            result = result
        elif(X >= 0 and Y < 0):
            print result
            print temp_sum*2
            result += temp_sum*2
        elif(X < 0 and Y <0 ):
            result += temp_sum * 3
        elif (X < 0 and Y >= 0):
            result += temp_sum * 4
    return result




print solution(2,2)