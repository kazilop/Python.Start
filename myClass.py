import math


class Point:

    x = int()
    y = int()

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


class Line:

    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def len(self):
        ss = math.sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
        return float(ss)


class Triangle:

    def __init__(self, point1, point2, point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3

    def squar(self):
        s = math.fabs(0.5 * ((self.p2.x - self.p1.x)*(self.p3.y - self.p1.y) - (self.p3.x - self.p1.x)*(self.p2.y - self.p1.y)))
        return s

    def perimetr(self):
        l1 = math.sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
        l2 = math.sqrt((self.p2.x - self.p3.x)**2 + (self.p2.y - self.p3.y)**2)
        l3 = math.sqrt((self.p1.x - self.p3.x)**2 + (self.p1.y - self.p3.y)**2)
        return l1+l2+l3

    def hight(self):
        h = list()
        h.append(self.p1.y)
        h.append(self.p2.y)
        h.append(self.p3.y)
        h_max = max(h)
        h_min = min(h)

        return h_max - h_min


# Задание № 2
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    l1 = float()
    l2 = float()
    l3 = float()
    l4 = float()

    def __init__(self, point1, point2, point3, point4):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3
        self.p4 = point4

        self.line1 = Line(self.p1, self.p2)
        self.line2 = Line(self.p2, self.p3)
        self.line3 = Line(self.p3, self.p4)
        self.line4 = Line(self.p4, self.p1)

    def is_ravnob(self):
        if self.line1.len() == self.line3.len() or self.line2.len() == self.line4.len():
            return True
        else:
            return False

    def perimetr(self):
        return float(self.line1.len())+float(self.line2.len())+float(self.line3.len())+float(self.line4.len())

    def square(self):
        s = (self.line1.len()+self.line3.len() / 2) * math.sqrt( self.line3.len()**2 - ((self.line3.len() - self.line1.len())**2)/4)
        return s


