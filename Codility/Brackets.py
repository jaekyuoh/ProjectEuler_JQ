def solution(S):
    s_list = list(S)
    visited_stack = []
    if S == '':
        return 1
    if s_list[0] == '}' or s_list[0] == ']' or s_list[0] == ')':
        return 0
    for i in range(0,len(s_list)):
        if s_list[i] != '}' and s_list[i] !=']' and s_list[i] !=')':
            visited_stack.append(s_list[i])
        elif s_list[i] == '}':
            if visited_stack == []:
                return 0
            recent_open = visited_stack.pop()
            if recent_open != '{':
                return 0
        elif s_list[i] == ')':
            if visited_stack == []:
                return 0
            recent_open = visited_stack.pop()
            if recent_open != '(':
                return 0
        elif s_list[i] == ']':
            if visited_stack == []:
                return 0
            recent_open = visited_stack.pop()
            if recent_open != '[':
                return 0

    if visited_stack != []:
        return 0
    return 1

print solution("{}{}{}")
