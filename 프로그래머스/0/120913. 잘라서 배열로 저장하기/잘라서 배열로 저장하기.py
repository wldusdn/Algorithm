import math
def solution(my_str, n):   
    return [my_str[i*n:n*i+n] for i in range(math.ceil(len(my_str)/n))]
        