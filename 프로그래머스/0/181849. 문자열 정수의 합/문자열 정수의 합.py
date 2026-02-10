def solution(num_str):
    num = int(num_str)
    answer = 0
    for i in range(1,len(num_str)+1):
        answer += num % 10
        num = (num - (num % 10)) // 10
    return answer