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
    for step in range(l):
        c = n[l - 1 - step]

        if c == "0":
            continue

        match step % 3:
            case 1:
                answer = farsi_num_map[int(c)*10]
            case 2:
                answer = farsi_num_map[int(c)*100]
            case 0:
                answer = farsi_num_map[int(c)]
                if (step//3):
                    answer += " " + farsi_num_map[10**(3*step//3)]

        result.append(answer)

    return " و ".join(result[::-1])


print(number_to_farsi(input()))
