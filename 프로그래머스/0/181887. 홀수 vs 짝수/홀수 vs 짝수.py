def solution(num_list):
    odd, even = 0, 0
    for i in num_list[1::2]:
        odd += i 
    for i in num_list[::2]:
        even += i
    return max(odd,even)