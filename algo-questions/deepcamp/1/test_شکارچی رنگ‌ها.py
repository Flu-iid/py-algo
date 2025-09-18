def test():
    test_cases = [
        ('{"R": 255, "G": 0, "B": 0}', "red"),
        ('{"R": 0, "G": 255, "B": 0}', "green"),
        ('{"R": 0, "G": 0, "B": 255}', "blue"),
        ('{"R": 255, "G": 255, "B": 0}', "yellow"),
        ('{"R": 160, "G": 160, "B": 160}', "gray"),
        ('{"R": 255, "G": 0, "B": 255}', "purple"),
        ('{"R": 128, "G": 255, "B": 0}', "light green"),
        ('{"R": 64, "G": 255, "B": 0}', None),  # Tie between green and light green
        ('{"R": 255, "G": 255, "B": 255}', "white"),
        ('{"R": 0, "G": 0, "B": 0}', "black"),
        ('{"R": 255.0, "G": 0.0, "B": 0.0}', "red"),  # Float values that are integers
        ('{"R": 256, "G": 0, "B": 0}', None),  # Value out of range
        ('{"R": -1, "G": 0, "B": 0}', None),  # Value negative
        ('{"R": 255.5, "G": 0, "B": 0}', None),  # Non-integer float
        ('{"R": "255", "G": 0, "B": 0}', None),  # String value
        ('{"R": 255, "G": 0}', None),  # Missing key
        ('{"R": 255, "G": 0, "B": 0, "A": 0}', None),  # Extra key
        ("[255, 0, 0]", None),  # Not a dictionary
        ('{"R": 255, "G": 0, "B": 0', None),  # Syntax error
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        user_input = get_user_input(input_str)
        result = color_approx(user_input)
        if result == expected:
            print(f"Test {i + 1} passed: {input_str} -> {result}")
        else:
            print(
                f"Test {i + 1} failed: {input_str} -> expected {expected}, got {result}"
            )


# Uncomment the line below to run tests
test()
