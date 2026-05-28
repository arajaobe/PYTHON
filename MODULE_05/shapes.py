from abc import ABC, abstractmethod
from typing import Any

class Shape(ABC):
    @abstractmethod
    def area(self, value: Any) -> Any:      # accepts anything
        pass


class Circle(Shape):
    def area(self, value: float) -> float:  # overrides, but restricts to float
        if not isinstance(value, float):
            raise TypeError(f"Circle.area expects float, got {type(value).__name__}")
        return 3.14 * value ** 2


class Square(Shape):
    def area(self, value: int) -> int:      # overrides, but restricts to int
        if not isinstance(value, int):
            raise TypeError(f"Square.area expects int, got {type(value).__name__}")
        return value ** 2


c = Circle()
r = c.area(5.0)     # ✅ 78.5
#c.area(5)       # ❌ TypeError: Circle.area expects float, got int
print(r)
s = Square()
s.area(5)       # ✅ 25
#s.area(5.0)     # ❌ TypeError: Square.area expects int, got float
