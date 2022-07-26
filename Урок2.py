# Урок 2. Знакомство с Python. Продолжение
# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: 
# - 6782 -> 23
# - 0,56 -> 11

# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# 3 - Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# 4 - Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# 5 - Реализуйте алгоритм перемешивания списка.


import random
import math

def incomeNumber(lowerBorder = False, upperBorder = False, lowerBorderNumber = 0, upperBorderNumber = 0, integerNumber = True, positiveOnly = True, excludeZero = False):

    PositiveNegative = 1
    N_incomeNumber = 0
    F_incomeNumber = 0

    while True:
        income_Number = input("Введите число в соответствии с условием:\n")
        if len(income_Number) > 0:
            if income_Number[0] == "-":
                if positiveOnly:
                    print("Введённое число не должно быть отрицательным. Повторите ввод.\n")
                    continue
                else:
                    PositiveNegative = -1
                    income_Number = income_Number[1:]

        # print(income_Number)

        if income_Number.isdigit():
            N_incomeNumber = int (income_Number)
            break

        elif integerNumber:
            print("Введённое число должно быть целым. Не допустимы посторонние знаки. Повторите ввод.\n")
            continue

        else:
            tch_incomeNumber = income_Number.find('.')
            zpt_incomeNumber = income_Number.find(',')
            rzdtl_incomeNumber = tch_incomeNumber if tch_incomeNumber > -1 else zpt_incomeNumber

            if rzdtl_incomeNumber > -1:
                if income_Number[:rzdtl_incomeNumber].isdigit() and income_Number[rzdtl_incomeNumber+1:].isdigit():
                    N_incomeNumber = int (income_Number[:rzdtl_incomeNumber])
                    F_incomeNumber = int (income_Number[rzdtl_incomeNumber+1:])
                    
                    if excludeZero and N_incomeNumber+F_incomeNumber == 0:
                        print("Введен 0. Введите положительное число. Повторите ввод.\n")
                        continue
                    break
                else:
                    print("Введено не число. Должно быть введено вещественное число. Повторите ввод.\n")
                    continue

            else:
                print("Введено не число. Должно быть введено вещественное число. Повторите ввод.\n")
                continue


    if integerNumber:
        return N_incomeNumber*PositiveNegative
    else:
        return float(N_incomeNumber+F_incomeNumber/(10**len(income_Number[rzdtl_incomeNumber+1:])))*PositiveNegative


# def natureNumber(borderNumber = 0, PositiveNumber = True):
#     PositiveNegative = 1
#     while True:
#         income_natureNumber = input("Введите натуральное число в соответствии с Задачей:\n")
#         if income_natureNumber[0] == "-":
#             if PositiveNumber:
#                 continue
#             else:
#                 PositiveNegative = -1
#         if income_natureNumber.isdigit():
#             if borderNumber > 0 and borderNumber >= int(income_natureNumber) or borderNumber <= 0 and int(income_natureNumber) > 0:
#                 break
#             else:
#                 print("Введённое число должно быть целым, натуральным и должно соответствовать условию.")
#         else:
#             print("\nВы ввели не натуральное число.")
#     return int(income_natureNumber)


# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def task1():
    print("1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.")

    while True:
        stroka_N_task1 = input("Введите вещественное число.\n")
        prototip_task1 = stroka_N_task1

        if prototip_task1[0] == '-':
            prototip_task1 = prototip_task1[1:]

        tch_task1 = prototip_task1.find('.')
        zpt_task1 = prototip_task1.find(',')
        rzdtl_task1 = tch_task1 if tch_task1 > -1 else zpt_task1

        if rzdtl_task1 > -1:
            prototip_task1 = prototip_task1[ : rzdtl_task1] + prototip_task1[rzdtl_task1 + 1 : ]

        if prototip_task1.isdigit():
            break

    sum_task1 = 0

    for each in prototip_task1:
        sum_task1 += int (each)

    print(sum_task1)


# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def task2():
    print("2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.")

    N_task2 = incomeNumber()
    Multi_task2 = 1
    outcome_task2 = "1"

    for i in range(2,N_task2+1):
        Multi_task2*=i
        outcome_task2 += (", " + str(Multi_task2))

    if N_task2 != 0:
        print(outcome_task2)


# 3 - Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму. (1 + 1/n)**n


def task3():
    print("3. Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.")

    N_task3 = incomeNumber()
    list_task3 = []
    sum_task3 = 0

    for i in range(1,N_task3+1):
        list_task3.append((1 + 1/i)**i)
        sum_task3 += list_task3[i-1]

    print(list_task3)
    print(sum_task3)


# 4 - Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.


def task4():
    print("4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.")
    print("Введите N.")
    N_task4 = incomeNumber()
    list_task4 = []
    
    for i in range(0,N_task4):
        print("Введите {}-й элемент списка:".format(i+1))
        list_task4.append(incomeNumber(True, True, -math.fabs(N_task4), math.fabs(N_task4), True, False))


    print("Ввод комбинаций - 2х позиций (от 1 до {} включительно) чисел 1го списка для умножения друг с другом".format(N_task4))
    print("Введите количество комбинаций:")
    Comb_task4 = incomeNumber()
    Multi_list_task4 = []
    num1_task4 = 0
    num2_task4 = 0

    for i in range(0,Comb_task4):
        print("Введите {}-ю комбинацию чисел:".format(i+1))
        while True:
            try:
                print("Введите 1ю позицию комбинации.")
                num1_task4 = incomeNumber(False, True, 0, math.fabs(N_task4), True, True, True)
                print("Введите 2ю позицию комбинации.")
                num2_task4 = incomeNumber(False, True, 0, math.fabs(N_task4), True, True, True)
                if num1_task4 < 1 or num2_task4 < 1:
                    continue
                break
            except:
                print("Введите 2 числа типа integer.")

        Multi_list_task4.append(list_task4[num1_task4-1]*list_task4[num2_task4-1])

    print(Multi_list_task4)


# 5 - Реализуйте алгоритм перемешивания списка.


def task5():
    print("5. Реализуйте алгоритм перемешивания списка. Введите число элементов в списке.")

    N_task5 = incomeNumber()
    list_task5 = []

    print("Введите список, разделяя элементы с помощью ENTER.")
    for i in range(0,N_task5):
        list_task5.append(input())

    random.shuffle(list_task5)

    print(list_task5)


while True:

    print("Выберите задание, введя соответствующее число:\n" +
    "1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.\n" +
    "2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.\n" +
    "3 - Задайте список из n чисел последовательности (1 + \\frac 1 n)**n и выведите на экран их сумму.\n" +
    "4 - Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.\n" +
    "5 - Реализуйте алгоритм перемешивания списка.\n" +
    "6 - Выход из программы.\n")

    tasks = incomeNumber(False, True, 0, 6, True, True, True)

    if tasks == 1:
        task1()
    elif tasks == 2:
        task2()
    elif tasks == 3:
        task3()
    elif tasks == 4:
        task4()
    elif tasks == 5:
        task5()
    else:
        print("Выход из программы")
        break