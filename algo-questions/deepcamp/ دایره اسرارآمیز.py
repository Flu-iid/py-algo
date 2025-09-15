from math import pi
from typing import Literal


def circle_area(r: float) -> float | Literal[False]:
    if r <= 0:
        return False
    return pi * r**2


def circle_perimeter(r: float) -> float | Literal[False]:
    if r <= 0:
        return False
    return 2 * pi * r


radius: float = float(input())
result_area = circle_area(radius)
result_permimeter = circle_perimeter(radius)

if not result_area:
    print("Out of range")
else:
    print(f"area: {result_area:.4f}, perimeter: {result_permimeter:.4f}")
    print("Big Circle" if result_area >= 10 else "Small Circle")
