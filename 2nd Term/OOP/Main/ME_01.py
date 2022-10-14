# 1.     Створіть клас Rational для виконання арифметичних операцій з раціональними числами. Для ініціалізації
# атрибутів-даних класу - чисельника і знаменника - використовуйте метод __init __ () з аргументами за замовчуванням
# для випадку, якщо початкові значення чисельника і знаменника не надані. Раціональне число в пам'яті повинно
# зберігатися в скороченій формі, наприклад, дріб 2/4 повинна зберігатися як 1 в чисельнику і 2 в знаменнику.
# Передбачити можливість виведення раціональних чисел у форматі a / b, де a - чисельник, b - знаменник і в форматі
# з плаваючою комою.

class Rational:
    def __init__(self, a: int = 1, b: int = 1):
        if b == 0:
            raise "ValueError. A denominator can't be zero."

        mem = 1
        if a != 0 or abs(a) != 1:
            for i in range(1, min(abs(a), (abs(b))//2)+1):
                if a % i == 0 and b % i == 0:
                    mem = i
            if max(abs(a), abs(b)) % min(abs(a), abs(b)) == 0:
                mem = min(abs(a), abs(b))
            self._a = a // mem
            self._b = b // mem
        else:
            self._a = a
            self._b = b

    def __str__(self):
        return f'Fractional form: {self._a}/{self._b}\nFloating point form: {self._a/self._b}'

    def Output(self, dec=False):
        if not dec:
            print(f'{self._a}/{self._b}')
        else:
            print(f'{self._a/self._b}')


# x0 = Rational(0, 0)
# print(x0)
# x0.Output()
# x0.Output(1)
# print()
# Raises exception because invalid denominator

x1 = Rational()
print(x1)
x1.Output()
x1.Output(1)
print()

x2 = Rational(2, -4)
print(x2)
x2.Output()
x2.Output(1)
print()

x3 = Rational(14, -18)
print(x3)
x3.Output()
x3.Output(1)
print()

x4 = Rational(-24, 12)
print(x4)
x4.Output()
x4.Output(2)

# Console application part
print("*" * 80, "\n")
while True:
    x = int(input("Enter a numerator: "))
    y = int(input("Enter a denominator: "))

    x5 = Rational(x, y)

    print(x5)

    if input('Enter "e" to exit: ') == "e":
        break


# 2.     Створіть клас Rectangle. Для ініціалізації атрибутів-даних класу – довжини і ширини прямокутника –
# використовуйте метод __init __ () з аргументами за замовчуванням. Передбачити можливість визначення периметра і
# площі прямокутника. Доступ до атрибутів-даних повинен бути контрольований (довжину і ширину прямокутника обмежити 100
# см). Для демонстрації функціоналу класу Rectangle створіть консольний додаток.

class Rectangle:
    def __init__(self, length: float = 1, width: float = 1):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length <= 0 or length > 100:
            raise ValueError("Length either lower/equal to 0 or bigger than 100 cm.")
        else:
            self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width <= 0 or width > 100:
            raise ValueError("Width either lower/equal to 0 or bigger than 100 cm.")
        else:
            self.__width = width

    def perimeter(self):
        return (self.__length + self.__width) * 2

    def area(self):
        return self.__length * self.__width

    def __str__(self):
        return f'Side a/Length: {self.__length} cm\nSide b/Width: {self.__width} cm\n' \
               f'Perimeter: {self.perimeter()} cm\nArea: {self.area()} cm\u00b2'


# Console application part
while True:
    x = float(input("Enter length/side a of a rectangle (lower than 100): "))
    y = float(input("Enter width/side b of a rectangle (lower than 100): "))

    rect = Rectangle(x, y)

    print(rect)

    if input('Enter "e" to exit: ') == "e":
        break
        