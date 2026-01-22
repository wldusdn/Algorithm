def solution(n):
    answer = []
    for i in range(len(str(n))-1,-1,-1):
        v = 10**i
        answer.append(n//v)
        n = n%v
    return sum(answer)