def solution(dot):
    x, y = dot
    return (1 if x > 0 else 3) if x*y > 0 else (4 if x > 0 else 2)