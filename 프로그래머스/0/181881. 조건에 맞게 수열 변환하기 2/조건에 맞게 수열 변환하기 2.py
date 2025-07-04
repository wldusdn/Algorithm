def transfer(arr):
    answer = []
    for i in arr:
        if i >= 50 :
            answer.append(i // 2 if i % 2 == 0 else i)
        else:
            answer.append(i * 2 + 1 if i % 2 != 0 else i)
    return answer

def solution(arr):
    b_list = []
    c_list = arr
    count = 0
    while(b_list != c_list):
        b_list = c_list
        c_list = transfer(c_list)
        count += 1
    return count-1
