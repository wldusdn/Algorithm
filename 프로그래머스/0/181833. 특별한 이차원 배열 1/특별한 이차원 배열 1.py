def solution(n):
    answer = [[0] * (n-1) for _ in range(n)]
    for i in range(n):
        answer[i].insert(i, 1)
    return answer