
__author__ = 'Рыбка Артем Сергеевич'


# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

def zadanie1():
    number = input("Введи число: \n")

    for i in number:
        print(i)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


def zadanie2():
    number_a = input("Введи число a: \n")
    number_b = input("Введи число b: \n")

    temp = number_a
    number_a = number_b
    number_b = temp

    print("Теперь a= " + number_a + " ,а число b = " + number_b)
    print("Теперь меняем их обратно без доп.переменной")

    number_a = int(number_a) + int(number_b)
    number_b = int(number_a) - int(number_b)
    number_a = int(number_a) - int(number_b)

    print("Теперь a= " + str(number_a) + " ,а число b = " + str(number_b))
    return


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

def zadanie3():

    age = input ("Введите ваш возраст: \n")
    if int(age) >= 18:
        print ("Доступ разрешен")
    else:
        print("Извините, пользование данным ресурсом только с 18 лет")


select = input("Введи номер задачи \n")

if select == "1":
    zadanie1()
elif select == "2":
    zadanie2()
elif select == "3":
    zadanie3()
else:
    print("Неправильный ввод")
