from math import pi, sqrt
from typing import Literal


class Circle:
    def __init__(self, radius: float, center_x: float, center_y: float) -> None:
        self.radius: float = radius
        self.center_x: float = center_x
        self.center_y: float = center_y

    def perimeter(self) -> float:
        return 2 * pi * self.radius

    def area(self) -> float:
        return round(pi * self.radius * self.radius, 2)

    def distance_from_center(self, point_x: float, point_y: float) -> float:
        d_x: float = self.center_x - point_x
        d_y: float = self.center_y - point_y

        if not d_x and not d_y:
            return 0
        elif not d_x:
            return d_y
        elif not d_y:
            return d_x
        else:
            return sqrt(d_x * d_x + d_y * d_y)

    def poistion(
        self, point_x, point_y
    ) -> Literal["on"] | Literal["out"] | Literal["in"]:
        dist: float = self.distance_from_center(point_x, point_y)
        if dist == self.radius:
            return "on"
        elif dist > self.radius:
            return "out"
        else:
            return "in"


my_radius, my_center_x, my_center_y = [float(i) for i in input().split()]
point_x, point_y = [float(i) for i in input().split()]
my_circle = Circle(my_radius, my_center_x, my_center_y)
perimeter: float = my_circle.perimeter()
area: float = my_circle.area()
point_distance: float = my_circle.distance_from_center(point_x, point_y)
position: Literal["on"] | Literal["out"] | Literal["in"] = my_circle.poistion(
    point_x, point_y
)

result = f"{perimeter:.2f}\n{area:.2f}\n{point_distance:.2f}\n{position}"

print(result)
