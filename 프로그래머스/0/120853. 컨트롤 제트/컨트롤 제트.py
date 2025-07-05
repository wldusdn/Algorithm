def solution(s):
    sum = 0
    for i, n in enumerate(s.split()):
        if n == 'Z':
            sum -= int(s.split()[i-1]) 
        else:
            sum += int(n)     
    return sum