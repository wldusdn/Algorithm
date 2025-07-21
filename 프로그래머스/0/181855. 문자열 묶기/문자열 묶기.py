def solution(strArr):
    dic = dict()
    for s in strArr:
        if len(s) in dic :
            dic[len(s)] += 1
        else:
            dic[len(s)] = 1
    return max(dic.values())