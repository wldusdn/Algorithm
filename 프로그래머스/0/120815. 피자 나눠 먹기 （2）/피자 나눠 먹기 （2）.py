def solution(n):
    r = 1;
    while (r*6 % n != 0):
        r += 1;
    return r