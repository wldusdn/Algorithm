def solution(binomial):
    a, op, b = binomial.split(' ')
    dic = { '+': int(a)+int(b), '-': int(a)-int(b), '*': int(a)*int(b)}
    return dic[op]