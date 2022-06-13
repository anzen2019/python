#Задача 2
# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000
# (куб X - третья степень числа X):
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех
# чисел из этого
# списка, сумма цифр которых делится нацело на 7.
# c. * Решить задачу под пунктом b, не создавая новый список

# Пункт a
#Вывод кубов нечетных чисел
my_list = []
for i in range(1, 1001, 2): #после отладки кода заменить 21 на 1001
    my_list.append(i**3)
# print(my_list)
#Расчет суммы чисел, сумма цифр которых делится на 7
list_sum = 0 #счетчик
for num in my_list:
    tmp_num = num #запомнили число, чтобы над ним проводить операции
    len_num = len(str(num)) #расчет длины числа, для этого перевел в строку
    my_sum = 0 #сумма цифр числа
    for i in range(len_num):
        remains = tmp_num % 10  # поиск остатка
        my_sum += remains  # подсчет суммы цифр числа
        tmp_num = tmp_num // 10  # целое число от деления - что придет на выход на следующем цикле
    if my_sum % 7 == 0:
        list_sum += num
print(list_sum)
#Пункт b
#Прибавить 17 каждому элементу списка
my_list_seventeen = []
for num in my_list:
    num += 17
    my_list_seventeen.append(num)
# print(my_list_seventeen)
#Расчет суммы чисел, сумма цифр которых делится на 7
list_sum_seventeen = 0 #счетчик
for num in my_list_seventeen:
    tmp_num = num #запомнили число, чтобы над ним проводить операции
    len_num = len(str(num)) #расчет длины числа, для этого перевел в строку
    my_sum = 0 #сумма цифр числа
    for i in range(len_num):
        remains = tmp_num % 10  # поиск остатка
        my_sum += remains  # подсчет суммы цифр числа
        tmp_num = tmp_num // 10  # целое число от деления - что придет на выход на следующем цикле
    if my_sum % 7 == 0:
        list_sum_seventeen += num
print(list_sum_seventeen)
#
#Пункт с
for i, num in enumerate(my_list):
    num += 17
    my_list[i] = num
# print(my_list)
#Расчет суммы чисел, сумма цифр которых делится на 7
list_sum = 0 #счетчик
for num in my_list:
    tmp_num = num #запомнили число, чтобы над ним проводить операции
    len_num = len(str(num)) #расчет длины числа, для этого перевел в строку
    my_sum = 0 #сумма цифр числа
    for i in range(len_num):
        remains = tmp_num % 10  # поиск остатка
        my_sum += remains  # подсчет суммы цифр числа
        tmp_num = tmp_num // 10  # целое число от деления - что придет на выход на следующем цикле
    if my_sum % 7 == 0:
        list_sum += num
print(list_sum)








