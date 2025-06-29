import string
def solution(my_string):
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    answer = []
    for s in upper:
        answer.append(my_string.count(s))
    for s in lower:
        answer.append(my_string.count(s))
    return answer