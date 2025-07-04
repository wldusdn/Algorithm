def solution(n):
    fac = 1
    for i in range(2,12):
        fac *= i
        if fac > n:
            return i-1