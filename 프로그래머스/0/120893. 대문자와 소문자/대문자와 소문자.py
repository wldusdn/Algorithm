def solution(my_string):
    answer = []
    for s in my_string:
        if s.islower():
            answer.append(s.upper())
        else:
            answer.append(s.lower())
    return ''.join(answer)