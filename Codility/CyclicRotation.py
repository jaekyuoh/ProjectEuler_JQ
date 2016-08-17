# -*- coding: utf-8 -*-

def solver(A,K):
    stack  = A
    if A != []:
        for i in range(0,K):
            item = stack.pop()
            stack.insert(0,item)
        return stack
    return A


if __name__ == '__main__':
    print solver([], 3)
