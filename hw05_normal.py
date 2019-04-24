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

# Global v

PATH = list()
CURRENT_NUMB = int(0)
PATH.append(os.getcwd())


def menu():
    print('\x1b[1;33mГлавное меню \x1b[0m \n')
    print('\x1b[34m1 -Перейти в папку\x1b[0m')
    print('\x1b[34m2 -Просмотреть содержимое текущей папки\x1b[0m')
    print('\x1b[34m3 -Удалить папку\x1b[0m')
    print('\x1b[34m4 -Создать папку\x1b[0m \n')
    print('\x1b[34m5 -Текущий каталог\x1b[0m \n')
    print('\x1b[1;31m0 -Выход\x1b[0m \n')
    print('\x1b[36mВведи значение: \x1b[0m')

    return input()

def go_dir(name_dir, cur):
    if name_dir == ".." and cur != 0:
        os.chdir(PATH[cur-1])
        cur = cur - 1
    else:
        PATH.append(PATH[cur]+'\\'+str(name_dir))
        cur += 1
        os.chdir(PATH[cur])

    return cur


def make_dir(name):
    try:
        os.mkdir(name)
        return True
    except FileExistsError:
        print("Такая папка уже есть... \n")
        return False


def del_dir(name):
    if os.path.exists(os.path.abspath(os.curdir+'\\'+name)):

        if not os.listdir(os.path.abspath(os.curdir+'\\'+name)):
            os.rmdir(name)
            return True
        else:
            print("Папка не пустая")
            return False
    else:
        print("Такой папки нет")



answer = 1

while answer != 0:
    answer = menu()

    if answer == "1":
        next_dir = input("В какую папку идем ? (..) - подняться вверх: ")
        try:
           temp1 = go_dir(next_dir, CURRENT_NUMB)
           CURRENT_NUMB = temp1
        except FileNotFoundError:
            print("Такой папки нет")

    elif answer == "2":
        zadanie2()

    elif answer == "3":
        nameDir = input("Какую папку удаляем ? \n")
        if del_dir(nameDir):
            print("Успешно удалили ...")

    elif answer == "4":
        nameDir = input("Какую папку создаем ? \n")
        if make_dir(nameDir):
            print("Успешно создали ...")

    elif answer == "5":
        print(os.path.abspath(os.curdir))

    elif answer == "0":
        print('\x1b[1;31m Досвидания ... \x1b[0m \n')
        break

    else:
        print('\x1b[1;31m Такой команды нет .. \x1b[0m \n')







