def solution(myStr):
    for i in myStr:
        if i in ['a', 'b', 'c']:
           myStr = myStr.replace(i, ' ')
    answer = list(filter(lambda x: x , myStr.split(' '))) 
    return answer if len(answer) > 0 else ['EMPTY']