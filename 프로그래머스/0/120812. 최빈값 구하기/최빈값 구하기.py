
def solution(array):
    count = dict();
    duplicate = 0;
    answer = 0;
    for i in array:
        count[i] = array.count(i)
    for i in count.keys():
        if count[i] == max(count.values()):
            duplicate += 1;
            answer = i
    return answer if duplicate < 2 else -1