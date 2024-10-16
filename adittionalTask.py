import math

class Figure:
    sides_count = 0
    #__sides = []
    def __init__(self, color, sides, sides_count, filled = True):
        self.__sides = sides
        if self.__is_valid_color(color[0], color[1], color[2]):
            self.__color = []
            self.__color = color
        else:
            self.__color = (255, 255, 255)# default color
        self.filled = filled
        self.sides_count = sides_count

    def get_color(self):
        return [self.__color[0], self.__color[1], self.__color[2]]

    def __is_valid_color(self, r, g, b):
        r = int(r)
        g = int(g)
        b = int(b)
        if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
            return True
        else:
            return False
    def  set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = []
            self.__color.extend([r, g, b])
        else:
            print('Веедите корректный цвет в диапазоне от 0 до 255')

    def __is_valid_sides(self, *args):
        for i in args:
            if i < 0 and isinstance(i, int):
                return False
            else:
                print('Вы ввели неправельно. Введите положительное целое число')
        if self.sides_count != len(args):
            return False
        else:
            return True

    def get_sides(self):
        return self.__sides


    def __len__(self):
        if self.sides_count == 12:
            return int(12 * self.__sides[0])
        elif self.sides_count == 3:
            return int(self.__sides[0] + self.__sides[1] + self.__sides[2])
        elif self.sides_count == 1:
            return int(self.__sides[0])
        else:
            return 0


    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = []
            for i in new_sides:
                self.__sides.append(i)
        else:
            print("Не соответствует количеству стоон данной фигуры")


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, size_side, sides = sides_count):
        send_size = []
        if sides == self.sides_count:
            send_size = [size_side]
        else:
            send_size = [1]
        super().__init__(color, send_size, self.sides_count)
        self.__radius = super().get_sides()[0] / (2 * math.pi)


    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, size_side, sides = sides_count):
        send_size = []
        if sides == self.sides_count:
            for i in range(self.sides_count):
                send_size.append(size_side)
        else:
            for i in range(self.sides_count):
                send_size.append(1)
        super().__init__(color, send_size, self.sides_count)

    def get_square(self):
        temp_list = super().get_sides()[0]
        p = 1/2 * (super().get_sides()[0] + super().get_sides()[1] + super().get_sides()[2])
        S = math.sqrt(p*(p - super().get_sides()[0]) * (p - super().get_sides()[1]) * (p - super().get_sides()[2]))
        return S

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, size_side, sides = sides_count):
        send_size = []
        if sides == self.sides_count:
            for i in range(self.sides_count):
                send_size.append(size_side)
        else:
            for i in range(self.sides_count):
                send_size.append(1)
        super().__init__(color, send_size, self.sides_count)

    def get_volume(self):
        return super().get_sides()[0] ** 3

#print(Circle.__mro__)

circle1 = Circle([200, 200, 100], 10) # (Цвет, стороны)
cube1 = Cube([222, 35, 130], 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

triangle1 = Triangle([234, 23, 32], 33, 6)
print(triangle1.get_color())
print(triangle1.get_sides())
print(triangle1.get_square())
print(triangle1.sides_count)