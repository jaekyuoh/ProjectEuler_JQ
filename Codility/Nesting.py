def solution(S):
    count_open = 0
    count_close = 0
    if S == '':
        return 1
    if S[0] == ')':
        return 0

    for char in S:
        if char == '(':
            count_open += 1
        elif char != '(':
            count_close += 1
        if count_open < count_close:
            return 0
    if count_open != count_close:
        return 0
    else:
        return 1

print solution('()))((')