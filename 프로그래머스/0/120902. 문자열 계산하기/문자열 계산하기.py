def solution(my_string):
    list = my_string.split(' ')
    num = list[::2]
    op = list[1::2]
    val = int(num[0])
    for i in range(len(op)):
        print(i)
        if op[i] == '+':
            val = val + int(num[i+1])
        else:
            val = val - int(num[i+1])
    return val