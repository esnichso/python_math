
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

    def __eq__(self, other):
        if isinstance(other, Point):
            return all([a.value == b.value for a, b in zip(self.coordinates, other.coordinates)])
        return NotImplemented

    def location_vector(self):
        return Vector(self.dimension, [Number(c.value) for c in self.coordinates])

    def __repr__(self):
        return f"Point({self.coordinates})"

class Matrix:
    def __init__(self, rows: Number, columns: Number, values: list[list[Number]]):
        self.rows = rows
        self.columns = columns
        self.values = values
    
    def __add__(self, other): # Matrix + Matrix
        if isinstance(other, Matrix):
            if self.rows.value == other.rows.value and self.columns.value == other.columns.value:
                return Matrix(self.rows, self.columns, [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.values, other.values)])
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Matrix): # Matrix - Matrix
            if self.rows.value == other.rows.value and self.columns.value == other.columns.value:
                return Matrix(self.rows, self.columns, [[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.values, other.values)])
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, Matrix): # Matrix * Matrix
            if self.columns.value == other.rows.value:
                result_values = []
                for i in range(self.rows.value):
                    result_row = []
                    for j in range(other.columns.value):
                        sum_product = Number(0)
                        for k in range(self.columns.value):
                            sum_product += self.values[i][k] * other.values[k][j]
                        result_row.append(sum_product)
                    result_values.append(result_row)
                return Matrix(self.rows, other.columns, result_values)
        elif isinstance(other, Vector): # Matrix * Vector
            if self.columns.value == other.dimension.value:
                result_values = []
                for i in range(self.rows.value):
                    sum_product = Number(0)
                    for j in range(self.columns.value):
                        sum_product += self.values[i][j] * other.values[j]
                    result_values.append(sum_product)
                return Vector(Number(self.rows.value), result_values)
        return NotImplemented
    
    def __rmul__(self, other): # Righthand multiplication
        if isinstance(other, Vector): # Vector * Matrix
            if other.dimension.value == self.rows.value:
                result_values = []
                for j in range(self.columns.value):
                    sum_product = Number(0)
                    for i in range(self.rows.value):
                        sum_product += other.values[i] * self.values[i][j]
                    result_values.append(sum_product)
                return Vector(Number(self.columns.value), result_values)
        return NotImplemented
    
    def __repr__(self):
        return f"{self.rows.value}x{self.columns.value}-Matrix({self.values})"