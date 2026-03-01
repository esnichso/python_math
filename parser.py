from components import Number, Vector, Point, Matrix

class Parser:
    def __init__(self):
        self.variables = {}

    def parse(self, expr):
        """
        Notation:
        - just the value for Number(value)
        - $v(value1 ... valueN) for Vector(N, [value1, ..., valueN])
        - $m((value11 ... value1M) ... (valueN1 ... valueNM)) for Matrix(N, M, [[value11, ..., value1M], ..., [valueN1, ..., valueNM]])
        - $p(value1 ... valueN) for Point(N, [value1, ..., valueN])
        - + for addition, - for subtraction, * for multiplication, / for division, x for cross product
        - lv(point) for location vector of a point
        - norm(vector) for normalization of a vector
        - len(vector) for length of a vector
        - get(var) to retrieve a variable's value
        """
        # This is a very basic implementation and does not handle operator precedence or parentheses
        tokens = expr.split()
        if not tokens:
            return None

        # Handle variable assignment
        if len(tokens) >= 3 and tokens[1] == '=':
            var_name = tokens[0]
            value_expr = ' '.join(tokens[2:])
            value = self.parse(value_expr)
            self.variables[var_name] = value
            return value

        # Handle get(var)
        if tokens[0] == 'get' and len(tokens) == 2:
            var_name = tokens[1]
            return self.variables.get(var_name, NotImplemented)

        # Handle lv(point), norm(vector), len(vector)
        if tokens[0] in ['lv', 'norm', 'len'] and len(tokens) == 2:
            func = tokens[0]
            arg_expr = tokens[1]
            arg_value = self.parse(arg_expr)
            match func:
                case 'lv' if isinstance(arg_value, Point):
                    return arg_value.location_vector()
                case 'norm' if isinstance(arg_value, Vector):
                    return arg_value.normalize()
                case 'len' if isinstance(arg_value, Vector):
                    return arg_value.length()
                case _:
                    return NotImplemented

        # Handle operations
        if len(tokens) == 3:
            left_expr, op, right_expr = tokens
            left_value = self.parse(left_expr)
            right_value = self.parse(right_expr)
            if op == '+':
                return left_value + right_value
            elif op == '-':
                return left_value - right_value
            elif op == '*':
                return left_value * right_value
            elif op == '/':
                return left_value / right_value
            elif op == 'x':
                return left_value.cross(right_value)

        # Handle literals for Number, Vector, Matrix, Point
        if tokens[0].startswith('$v'):
            values = [Number(float(v)) for v in tokens[0][2:].strip('()').split()]
            return Vector(Number(len(values)), values)
        elif tokens[0].startswith('$m'):
            rows = []
            for row_str in tokens[0][2:].strip('()').split(') ('):
                row_values = [Number(float(v)) for v in row_str.split()]
                rows.append(row_values)
            num_rows = len(rows)
            num_cols = len(rows[0]) if rows else 0
            return Matrix(Number(num_rows), Number(num_cols), rows)
        elif tokens[0].startswith('$p'):
            values = [Number(float(v)) for v in tokens[0][2:].strip('()').split()]
            return Point(Number(len(values)), values)
        else:
            try:
                return Number(float(tokens[0]))
            except ValueError:
                return NotImplemented

        


p = Parser()
while True:
    try:
        expr = input("Enter expression (or 'exit' to quit): ")
        if expr.lower() == 'exit':
            break
        result = p.parse(expr)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
        
