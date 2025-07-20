def solution(arr):
    i = 1
    while(len(arr) > i):
        i *= 2
    for i in range(i-len(arr)):
        arr.append(0)
    return arr  