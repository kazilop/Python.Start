
__author__ = 'Рыбка Артем Сергеевич'


# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

def zadanie1():
    fruits = ["яблоко", "банан", "киви", "арбуз"]
    index = 1
    for items in fruits:
        text = str(index) + "."+'{:>8}'.format(items)
        print(text)
        index = index +1
    return 0


# Задача-2:
# Даны два произвольные с писка.
# Удалите из первого списка элементы, присутствующие во втором списке.
def zadanie2():
    my_list1 = [1, 5, 12, 16, 44, 78, 47]
    my_list2 = [43, 6, 12, 77, 47, 89, 65, 12]

    for item1 in my_list1:
        for item2 in my_list2:
            if item1 == item2:
                my_list1.remove(item1)
                break

    print("Элементы, которых нет во 2 списке:")
    for items in my_list1:
        print(items)

    return 0


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
def zadanie3():
    old_list = [3, 7, 3, 8, 9, 5, 6, 8, 34, 74, 22, 15, 78]
    new_list =list()

    for items in old_list:
        if items %2 == 0:
            new_list.append(items/4)
        elif items %2 > 0:
            new_list.append(items * 2)
        else:
            print("неверное значение")

    print("Новый список выглядит так: ")
    for items in new_list:
        print(items)

    return 0


select = input("Введи номер задачи \n")

if select == "1":
    zadanie1()
elif select == "2":
    zadanie2()
elif select == "3":
    zadanie3()
else:
    print("Неправильный ввод")
