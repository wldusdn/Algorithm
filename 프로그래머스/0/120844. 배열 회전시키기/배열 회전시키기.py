def solution(numbers, direction):
    dic = {'right':-1, 'left':1}
    return numbers[dic[direction]:]+numbers[:dic[direction]]