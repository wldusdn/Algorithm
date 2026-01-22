def toArray(array):
    answer = []
    for i in array:
        answer.append(int(i))
    return answer

def solution(n):
    return toArray(list(str(n)[::-1]))