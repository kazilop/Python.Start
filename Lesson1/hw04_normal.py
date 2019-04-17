__author__ = 'Рыбка Артем Сергеевич'

import math
import random
import re
import os


# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

def zadanie1():
    line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
           'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
           'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
           'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
           'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
           'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
           'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
           'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
           'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
           'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT' \
           'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
           'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
           'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
           'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
           'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

    """ Способ без re"""
    s = list()
    len1 = 0
    item_index = 0
    text = ''

    for item in line:
        if item.islower():
            len1 = len1 + 1
            block_len = 0
            text = text + item

        elif item.isupper():
            block_len = len1

        if block_len > 0:
            s.append(text)
            text = ''
            len1 = 0

        item_index = item_index + 1

   # b = [i for i in line if i.islower()]

    print(s)
    print("*"*30)

    """ Второй способ с re"""

    def lower_search(text1):
        pattern = r"[a-z]{1,}"
        result = re.findall(pattern, text1, re.MULTILINE)
        return result

    my_result = lower_search(line)
    print(my_result)


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

def zadanie2():
    line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm' \
             'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV' \
             'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA' \
             'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV' \
             'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW' \
             'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
             'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR' \
             'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm' \
             'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn' \
             'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS' \
             'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf' \
             'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
             'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN' \
             'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ' \
             'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

    """ Способ с re """

    pattern = r"[a-z]{2}([A-Z]+)[A-Z]{2}"
    result = re.findall(pattern, line_2, re.MULTILINE)
    print(result)
    print("* " * 30)

    """ Способ без re"""

    li = line_2

    text = list()
    s = ""
    i = 2  # от 2 т.к. по условию слева должны быть минимум 2 символа

    while i < len(line_2) - 2:
        if li[i].isupper() and li[i+2].isupper() and li[i+1].isupper() and li[i-1].islower() and li[i-2].islower():
            while li[i].isupper() and li[i+2].isupper() and li[i+1].isupper():
                s = s + li[i]
                i = i + 1
            text.append(s)
            s = ""
        i = i + 1

    print(text)


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


def zadanie3():
    s = ""
    ss = ""
    name_file = "lesson4.txt"
    temp = list()
    temp2 = list()
    i = 0
    while i <= 25000:
        temp.append(random.randint(0, 9))
        s = s + str(temp[i])
        i = i + 1

    with open(name_file,'w', encoding='UTF-8') as file:
        file.write(s)

    with open(name_file,'r', encoding='UTF-8') as file:
        new_read = file.read()

    print("Значения из файла ")
    print(new_read)

    index = len(new_read) -1

    while index > 1:
        if new_read[index] == new_read[index-1]:
            ss = ss + new_read[index]
        else:
            if ss != '':
              temp2.append(ss)
              ss = ''
        index = index - 1

    max_len = 0
    for ii in temp2:
        if int(ii) > max_len:
            max_len = int(ii)


    print("Максимально длинное значение  ")
    print(max_len)





select = input("Введи номер задачи 1-3 \n")

if select == "1":
    zadanie1()
elif select == "2":
    zadanie2()
elif select == "3":
    zadanie3()
else:
    print("Неправильный ввод")
