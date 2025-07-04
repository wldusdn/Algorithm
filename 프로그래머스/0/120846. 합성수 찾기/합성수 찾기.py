def solution(n):
    answer = []
    if n <= 3:
        return 0
    for i in range(4, n+1):
        for j in range(2,i):
            if i % j == 0:
                answer.append(i)
                break
    return len(answer)