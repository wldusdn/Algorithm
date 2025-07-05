def solution(myString, pat):
    count = 0
    for i in range(len(myString)-len(pat)+1):
        if pat == myString[i:i+len(pat)]:
            count += 1
    return count