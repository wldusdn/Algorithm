def solution(emergency):
    sortedarr = sorted(emergency, reverse=True)
    arr = []
    dic = dict()
    for i, n in enumerate(sortedarr):
        dic[n] = i+1
    for i in emergency:
        arr.append(dic[i])
    return arr