def solution(n_str):
    for i in n_str:
        if(int(i) == 0):
            n_str = n_str[1:]
        else: break
    return n_str