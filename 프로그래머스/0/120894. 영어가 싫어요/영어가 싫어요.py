def solution(numbers):
    num = {'zero': '0' , 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for s, n in num.items():
        numbers = numbers.replace(s, n)
    return int(numbers)