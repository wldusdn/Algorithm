def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        if len(answer) == k:   
            return answer
    answer += [-1] * (k-len(answer))
    return answer