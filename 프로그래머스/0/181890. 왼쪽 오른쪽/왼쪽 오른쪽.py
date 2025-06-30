def solution(str_list):
    for i, n in enumerate(str_list):
        if n == "l":
            return str_list[:i]
        elif n == "r":
            return str_list[i+1:]
    return []