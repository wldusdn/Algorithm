def find_alphabet(string):
    arr = [-1]*26
    for i, char in enumerate(string):
        index = ord(char)-ord("a")
        if arr[index] == -1:
            arr[index] = i
    return arr 

print(*find_alphabet(input()))