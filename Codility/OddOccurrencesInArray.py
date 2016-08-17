# -*- coding: utf-8 -*-

def solver(A):
    set = {}
    if A != []:
        for item in A:
            if set.has_key(item):
                set.pop(item)
            else:
                set[item] = item
        l = set.keys()
        return l[0]
    return A


if __name__ == '__main__':
    print solver([9,3,9,3,9,7,9])