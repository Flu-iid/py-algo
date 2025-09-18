def divide_by_num(input_num: int, div_num: int) -> bool:
    if input_num % div_num == 0:
        return True
    return False


num = int(input())
div_3_result: bool = divide_by_num(num, 3)
div_9_result: bool = divide_by_num(num, 9)
if div_3_result and div_9_result:
    print(f"{num} is dividable by both 9 and 3")
elif div_3_result:
    print(f"{num} is dividable by only 3")
elif div_9_result:
    print(f"{num} is dividable by only 9")
else:
    print(f"{num} is neither dividable by 9 nor 3")
