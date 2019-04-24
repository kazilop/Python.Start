__author__ = 'Рыбка Артем Сергеевич'

from hw05_easy import zadanie2
import os

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Global

PATH = list()
PATH.append(os.getcwd())

def menu():
    print('\x1b[1;33mГлавное меню \x1b[0m \n')
    print('\x1b[34m1 -Перейти в папку\x1b[0m')
    print('\x1b[34m2 -Просмотреть содержимое текущей папки\x1b[0m')
    print('\x1b[34m3 -Удалить папку\x1b[0m')
    print('\x1b[34m4 -Создать папку\x1b[0m \n')
    print('\x1b[1;31m0 -Выход\x1b[0m \n')
    print('\x1b[36mВведи значение: \x1b[0m')

    return input()

def go_dir(name_dir):
    if name_dir == "..":
        pass
    else:
        pass


answer = 1

while answer != 0:
    answer = menu()

    if answer == "1":
        next_dir = input("В какую папку идем ? : ")
        try:
            go_dir(next_dir)
        except FileNotFoundError:
            print("Такой папки нет")

    elif answer == "2":
        zadanie2()

    elif answer == "3":
        pass

    elif answer == "4":
        pass

    elif answer == "0":
        print('\x1b[1;31m Досвидания ... \x1b[0m \n')
        break

    else:
        print('\x1b[1;31m Такой команды нет .. \x1b[0m \n')







