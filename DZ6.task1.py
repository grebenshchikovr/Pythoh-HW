class Triangle:

    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

        if not self.is_triangle():
            exit(1)

    def is_triangle(self):
        a = self.a
        b = self.b
        c = self.c
        if (a < b + c) and (b < a + c) and (c < b + a):
            return True
        else:
            print("Такой треугольник нельзя создать")
            return False

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def print(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


T = Triangle(5, 12, 13)

print(T.is_triangle())
print(T.perimeter())
print(T.area())
print(T.print())
