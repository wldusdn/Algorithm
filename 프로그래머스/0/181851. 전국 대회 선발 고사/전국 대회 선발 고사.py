def solution(rank, attendance):
    answer = []
    for i,r in enumerate(rank):
        if(attendance[i]):
            if(len(answer)>=3 and max(answer[0]) > r):
                answer.remove(max(answer))
                answer.append([r,i])
            else: answer.append([r,i])
    answer.sort()
    return 10000*answer[0][1] + 100*answer[1][1] + answer[2][1]