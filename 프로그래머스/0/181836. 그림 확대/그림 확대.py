def solution(picture, k):
    answer = []
    for pic in picture:
        word = ""
        for p in pic:
            for i in range(k):
                word += p
        for i in range(k):
            answer.append(word)
    return answer