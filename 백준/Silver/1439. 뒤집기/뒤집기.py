def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero_to_one = 0
    one_to_zero = 0
    before_num = string[0]
    for i in string[1:]:
        if before_num != i:
            if before_num == "0" : zero_to_one += 1
            else: one_to_zero += 1
        before_num = i
 
    return zero_to_one if zero_to_one >= one_to_zero else one_to_zero


result = find_count_to_turn_out_to_all_zero_or_all_one(input())
print(result)