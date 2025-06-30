def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f
def solution(balls, share):
    return factorial(balls) / (factorial(balls-share) * factorial(share))