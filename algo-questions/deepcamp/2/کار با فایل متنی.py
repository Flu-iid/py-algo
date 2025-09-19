def calculate(v1: float, v2: float, opr: str) -> float:
    return eval(f"{v1}{opr}{v2}")


def calculate_file(file_name: str) -> list[float]:
    with open(file_name, "r") as fin:
        i = 0
        values = []
        answers = []
        while line := fin.readline().strip():
            i += 1
            if i % 2:
                values += [float(i) for i in line.split()]
            else:
                value_1, value_2 = values
                answers.append(calculate(value_1, value_2, line))
                values.clear()
        return answers


f_name = input()
try:
    result: list[float] = calculate_file(f_name)
except (ZeroDivisionError, FileNotFoundError):
    print("Invalid input or file")
else:
    print(result)
