# -*- coding: utf-8 -*-

def convert_to_binary(number):
    binary_list = []

    check = False
    max = 0
    count = 0
    while True:
        if number == 0 or number == 1: # base case
            binary_list.append(number)
            if number == 1 and check:
                if count > max:
                    max = count
                count = 0
            break
        if number % 2 == 1:
            number = number / 2
            binary_list.append(1)
            if check == True:
                if count > max:
                    max = count
                count = 0

            check = True
        elif number % 2 == 0:
            number = number / 2
            binary_list.append(0)
            if check:
                count += 1
    binary_list.reverse()
    return binary_list, max


if __name__ == '__main__':
    l,max = convert_to_binary(110002)
    print l
    print max