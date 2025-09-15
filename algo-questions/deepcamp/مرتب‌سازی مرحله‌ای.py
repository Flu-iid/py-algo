from typing import Generator


class EmptyListError(Exception):
    pass


def str_to_int_list(s: str) -> list[int]:
    truncated_string: str = s[1:-1]
    if not truncated_string:
        raise EmptyListError("Empty List")
    return [int(i) for i in truncated_string.split(", ")]


# we couldve just used json loads as well.
# but i figured, more robust solution is what was considered.


def sort_1_by_1(input_list: list[int]) -> Generator:
    result: list = []
    for i in input_list:
        result.append(i)
        yield sorted(result)


try:
    result = str_to_int_list(input())
    for i in sort_1_by_1(result):
        print(i)
except EmptyListError as e:
    print("Error:", e.args[0])
except ValueError:
    print("Error:", "Wrong element type entered")
