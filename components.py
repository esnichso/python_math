
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Number):
            return Number(self.value / other.value)
        return NotImplemented

    def __repr__(self):
        return f"Number({self.value})"
    
class Vector:
    def __init__(self, dimension: Number, values: list[Number]):
        self.dimension = dimension
        self.values = values

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.dimension.value == other.dimension.value:
                return Vector(self.dimension, [a + b for a, b in zip(self.values, other.values)])
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.dimension.value == other.dimension.value:
                return Number(sum([a.value * b.value for a, b in zip(self.values, other.values)]))
        elif isinstance(other, Number):
            return Vector(self.dimension, [Number(a.value * other.value) for a in self.values])
        return NotImplemented

    def __repr__(self):
        return f"{self.dimension.value}-Vector({self.values})"

    # TODO length of Vector
    # TODO normalization of Vector
    # TODO Cross product of Vector

# Test Cases

a = Number(5)
b = Number(10)
c = a + b
d = a * b
e = a / b
f = Vector(Number(2), [Number(1), Number(2)])
g = Vector(Number(2), [Number(3), Number(4)])
h = f + g
i = f * g
j = f * Number(2)

print(c)  # Number(15)
print(d)  # Number(50)
print(e)  # Number(0.5)
print(f)  # 2-Vector([1, 2])
print(g)  # 2-Vector([3, 4])
print(h)  # 2-Vector([4, 6])
print(i)  # Number(11)
print(j)  # 2-Vector([2, 4])
