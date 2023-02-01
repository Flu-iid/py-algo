def is_q_int(i: tuple) -> str:
    if not all(map(lambda x: 0 < x < 101, i)):
        return "No"
    return "Yes" if (i[0]-i[1]) / i[2] == (i[0]-i[1]) // i[2] else "No"


input_mock: str = "3\n" \
                  "7 2 1\n" \
                  "25 5 5\n" \
                  "7 2 2"

test_amount, test_data = input_mock.split("\n", 1)
pieces = tuple(int(d) for d in test_data.replace("\n", " ").split(" "))
for test_idx in range(0, int(test_amount) * 3, 3):
    print(is_q_int((pieces[test_idx], pieces[test_idx + 1], pieces[test_idx + 2])))