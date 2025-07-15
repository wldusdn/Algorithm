def solution(quiz):
    answer = []
    for i in quiz:
        a, op, b, _, c = i.split(' ')
        if op == '+':
            answer.append('O') if int(a) + int(b) == int(c) else answer.append('X')
        else: answer.append('O') if int(a) - int(b) == int(c) else answer.append('X')
    return answer