def solution(s):
    array = []
    for i in list(s):
        if(i == ")"):
            if(len(array) == 0): return False
            array.pop()
        else: array.append(i)       
    return False if(len(array) > 0) else True