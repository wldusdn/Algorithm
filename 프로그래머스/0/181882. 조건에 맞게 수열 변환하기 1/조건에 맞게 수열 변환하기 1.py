def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 :
            answer.append(i // 2 if i % 2 == 0 else i)
        else:
            answer.append(i * 2 if i % 2 != 0 else i)
    return answer