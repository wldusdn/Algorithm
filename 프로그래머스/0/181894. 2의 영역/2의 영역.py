def solution(arr):
    count = arr.count(2)
    if (count > 0):
        s, e = -1, 0
        for i, n in enumerate(arr):
            if n == 2:
                if s >= 0:
                    e = i
                else: s = i
        return arr[s:e+1] if e != 0 else [arr[s]]
    else: return [-1]