def unique_count(input_list: list) -> int:
    return len(set(input_list))


def max_unique(input_dict: dict[str, list[int]]) -> str:
    compare = None
    for k in input_dict:
        v = input_dict[k]
        v_unique = unique_count(v)
        if not compare or v_unique > compare[0]:
            compare = (v_unique, k)

    return compare[1]


user_dict = eval(input())
print(max_unique(user_dict))
