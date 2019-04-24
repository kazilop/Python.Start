__author__ = 'Рыбка Артем Сергеевич'

import shutil
import os


def num_mkdir(name, numb):
    new_path = os.getcwd()
    i = 1
    dirname = list()
    while i < numb:
        temp_path = new_path + "\\" + str(name) + str(i)
        try:
            os.mkdir(temp_path)
            dirname.append(temp_path)
            i += 1
        except FileExistsError:
            print("Невозможно создать...")

    return dirname


def del_dir(dir_name):
    try:
        for name in dir_name:
            os.rmdir(name)
    except FileExistsError:
        print("Дириктории не существует")


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def zadanie1():

    name = input("Введи название дирикторий : ")
    numb = int(input("Введи кол-во :"))

    dir_name = num_mkdir(name, numb)
    print("Дириктории созданы \n\n")

    input("После ввода мы удалим эти дириктории")

    del_dir(dir_name)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def zadanie2():
    listdir = list()
    dirs = os.listdir()

    for z in dirs:
      #  if z[0]:
            listdir.append(z)

    # не нашел в инете как в регуляторных выражения обозначить точку
    print("Директории в текущей папке : \n")
    print(listdir)



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def zadanie3():
    print(__file__)
    shutil.copyfile(__file__, "newfile.txt")


if __name__ == '__main__':
    select = input("Введи номер задачи 1-3 \n")

    if select == "1":
        zadanie1()
    elif select == "2":
        zadanie2()
    elif select == "3":
        zadanie3()

    else:
        print("Неправильный ввод")
