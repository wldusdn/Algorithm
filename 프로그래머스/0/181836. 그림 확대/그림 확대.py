def solution(picture, k):
    answer = []
    # for pic in picture:
    #     word = ""
    #     for p in pic:
    #         for i in range(k):
    #             word += p
    #     for i in range(k):
    #         answer.append(word)
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace(".", "."*k).replace("x","x"*k))
    return answer