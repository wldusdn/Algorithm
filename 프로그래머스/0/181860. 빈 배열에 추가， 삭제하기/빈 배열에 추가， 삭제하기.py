def solution(arr, flag):
    answer = []
    for n, f in zip(arr, flag):
        if f:
            for i in range(n*2):
                answer.append(n)
        else:
            answer = answer[:-n]
    return answer