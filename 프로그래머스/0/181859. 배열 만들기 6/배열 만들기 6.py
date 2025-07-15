def solution(arr):
    stk = []
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk = stk[:-1]
        else:
            stk.append(arr[i])
    return stk if len(stk) else [-1]