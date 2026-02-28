
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other): # Number + Number
        if isinstance(other, Number):
            return Number(self.value + other.value)
        return NotImplemented

    def __sub__(self, other): # Number - Number
        if isinstance(other, Number):
            return Number(self.value - other.value)
        return NotImplemented

    def __mul__(self, other): # Number * Number
        if isinstance(other, Number):
            return Number(self.value * other.value)
        return NotImplemented

    def __truediv__(self, other): # Number / Number
        if isinstance(other, Number):
            return Number(self.value / other.value)
        return NotImplemented

    def __repr__(self):
        return f"Number({self.value})"
    
class Vector:
    def __init__(self, dimension: Number, values: list[Number]):
        self.dimension = dimension
        self.values = values

    def __add__(self, other): # Vector + Vector
        if isinstance(other, Vector):
            if self.dimension.value == other.dimension.value:
                return Vector(self.dimension, [a + b for a, b in zip(self.values, other.values)])
        return NotImplemented

    def __sub__(self, other): # Vector - Vector
        if isinstance(other, Vector):
            if self.dimension.value == other.dimension.value:
                return Vector(self.dimension, [a - b for a, b in zip(self.values, other.values)])
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector): # Vector * Vector
            if self.dimension.value == other.dimension.value:
                return Number(sum([a.value * b.value for a, b in zip(self.values, other.values)]))
        elif isinstance(other, Number): # Vector * Number
            return Vector(self.dimension, [Number(a.value * other.value) for a in self.values])
        return NotImplemented

    def __rmul__(self, other): # Righthand multiplication
        if isinstance(other, Number): # Number * Vector
            return Vector(self.dimension, [Number(other.value * a.value) for a in self.values])
        return NotImplemented

    def __repr__(self):
        return f"{self.dimension.value}-Vector({self.values})"

    def length(self): # euclidean length
        return Number(sum([a.value ** 2 for a in self.values]) ** 0.5)

    def normalize(self): # Normalize the vector
        length = self.length()
        if length.value != 0:
            return Vector(self.dimension, [Number(a.value / length.value) for a in self.values])
        return NotImplemented

    def cross(self, other): # Cross product 3D!
        if isinstance(other, Vector):
            if self.dimension.value == 3 and other.dimension.value == 3:
                x = self.values[1].value * other.values[2].value - self.values[2].value * other.values[1].value
                y = self.values[2].value * other.values[0].value - self.values[0].value * other.values[2].value
                z = self.values[0].value * other.values[1].value - self.values[1].value * other.values[0].value
                return Vector(self.dimension, [Number(x), Number(y), Number(z)])
        return NotImplemented

class Point:
    def __init__(self, dimension: Number, coordinates: list[Number]):
        self.dimension = dimension
        self.coordinates = coordinates

    def __eq__(self, value):
        if isinstance(value, Point):
            return self.coordinates == value.coordinates
        return NotImplemented

    def location_vector(self):
        return Vector(self.dimension, [Number(c.value) for c in self.coordinates])

    def __repr__(self):
        return f"Point({self.coordinates})"

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
