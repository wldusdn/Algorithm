def solution(my_string, indices):
    dic = dict()
    for i, char in enumerate(my_string):
        dic[i] = char;
    for d in indices:
        del dic[d]
    return ''.join(dic.values())