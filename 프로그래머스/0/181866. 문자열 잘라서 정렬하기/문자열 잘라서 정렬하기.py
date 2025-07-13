def solution(myString):
    array = sorted(myString.split('x'))
    return list(filter(lambda x: x != '',  array))