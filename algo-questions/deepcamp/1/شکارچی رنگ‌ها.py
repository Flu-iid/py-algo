from ast import literal_eval

COLORS: dict[str, dict[str, int]] = {
    "white": {"R": 255, "G": 255, "B": 255},
    "black": {"R": 0, "G": 0, "B": 0},
    "red": {"R": 255, "G": 0, "B": 0},
    "green": {"R": 0, "G": 255, "B": 0},
    "blue": {"R": 0, "G": 0, "B": 255},
    "yellow": {"R": 255, "G": 255, "B": 0},
    "gray": {"R": 160, "G": 160, "B": 160},
    "purple": {"R": 255, "G": 0, "B": 255},
    "light green": {"R": 128, "G": 255, "B": 0},
}


def get_user_input(input_string: str) -> dict[str, int]:
    try:
        user_input = literal_eval(input_string)
        # eval bug raises syntax error
        if not isinstance(user_input, dict):
            raise TypeError
        elif set(user_input) != set("RGB"):
            raise KeyError
        else:
            for k in user_input:
                v: int = user_input[k]
                if not isinstance(v, (int, float)) or v > 255 or v < 0:
                    raise ValueError
    except (SyntaxError, ValueError, KeyError, TypeError):
        return None
    else:
        return user_input


def color_distance(input_dict: dict[str, int], color_dict: dict[str, int]) -> float:
    dr = input_dict["R"] - color_dict["R"]
    dg = input_dict["G"] - color_dict["G"]
    db = input_dict["B"] - color_dict["B"]

    return dr * dr + dg * dg + db * db


def color_approx(input_color: dict[str, int] | None) -> None | str:
    if not input_color:
        return None
    input_color_list: list[tuple[float, str]] = []
    for color in COLORS:
        color_accuracy: float = color_distance(input_color, COLORS[color])
        input_color_list.append((color_accuracy, color))
    sorted_color_list = sorted(input_color_list)
    min0, min1 = sorted_color_list[:2]
    if min0[0] == min1[0]:
        return None
    return min0[1]


user_input = get_user_input(input())
print(color_approx(user_input))
