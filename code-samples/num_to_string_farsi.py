farsi_num_map = {
    0: "صفر",
    1: "یک",
    2: "دو",
    3: "سه",
    4: "چهار",
    5: "پنج",
    6: "شش",
    7: "هفت",
    8: "هشت",
    9: "نه",
    10: "ده",
    11: "یازده",
    12: "دوازده",
    13: "سیزده",
    14: "چهارده",
    15: "پانزده",
    16: "شانزده",
    17: "هفده",
    18: "هشزده",
    19: "نوزده",
    20: "بیست",
    30: "سی",
    40: "چهل",
    50: "پنجاه",
    60: "شصت",
    70: "هفتاد",
    80: "هشتاد",
    90: "نود",
    100: "صد",
    200: "دویست",
    300: "سیصد",
    400: "چهارصد",
    500: "پانصد",
    600: "ششصد",
    700: "هفتصد",
    800: "هشتصد",
    900: "نهصد",
    10**3: "هزار",
    10**6: "میلیون",
    10**9: "میلیارد"
}


def number_to_farsi(n: str) -> str:
    if not n:
        return ""
    elif int(n) == 0:
        return farsi_num_map[0]

    result = []
    l = len(n)
    pass_index = False

    for step in range(l):
        c = n[l - step - 1]
        c_next = n[l - step - 2] if l - step - 2 >= 0 else ""
        c_next_next = n[l - step - 3] if l - step - 3 >= 0 else ""

        if pass_index:
            pass_index = False
            continue

        match step % 3:
            case 1:
                answer = farsi_num_map[int(c)*10] if c != "0" else ""
            case 2:
                answer = farsi_num_map[int(c)*100] if c != "0" else ""
            case 0:
                if c_next == "1":
                    answer = farsi_num_map[int(c_next + c)]
                    pass_index = True
                else:
                    answer = farsi_num_map[int(c)] if c != "0" else ""
                if (step//3) and not (c == "0" and c_next == "0" and c_next_next == "0"):
                    answer += " " + farsi_num_map[10**(3*step//3)]

        if answer:
            result.append(answer)

    return " و ".join(result[::-1])


if __name__ == "__main__":
    print(number_to_farsi(input()))
