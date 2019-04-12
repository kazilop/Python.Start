__author__ = 'Рыбка Артем Сергеевич'

import math
import random


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def zadanie1():
    def fibinacci(n,m):

        if n > 2:

            numb1 = 1
            numb2 = 1
            fib = list()
            i = 1

            while i <= m-2:
                summ = numb1 + numb2
                fib.append(summ)
                numb1 = numb2
                numb2 = summ
                i += 1
        else:
            return 1
        return fib[n-3:i]

    print(fibinacci(1, 15))



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def zadanie2():
    return 0



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def zadanie3():

    return 0


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def zadanie4():

    return 0




select = input("Введи номер задачи 1-4 \n")

if select == "1":
    zadanie1()
elif select == "2":
    zadanie2()
elif select == "3":
    zadanie3()
elif select == "4":
    zadanie4()
else:
    print("Неправильный ввод")
