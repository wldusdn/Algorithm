def solution(arr, flag):
    answer = []
    for i,n in enumerate(arr):
        if flag[i]:
            for j in range(n*2):
                answer.append(n)
        else:
            answer = answer[:len(answer)-n]
    return answer