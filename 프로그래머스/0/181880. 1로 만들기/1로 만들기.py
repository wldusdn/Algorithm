def div(n):
    count = 0
    while(n != 1):
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n-1)//2
        count += 1
    return count

def solution(num_list):
    answer = 0
    for i in num_list:
        answer += div(i)
    return answer