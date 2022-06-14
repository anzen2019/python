# Задача 5
# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде
# <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки,
# как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп
# или 00 коп).
# a = 4.2
# print(int(a)) #выделить целую часть числа а
# print(a - int(a)) #два способа посчитать дробную часть..почему-то выходят в конце не 0
# print(a%1)
price_list = [57.8, 46.51, 97, 102.30, 12, 1024, 3.14, 42.02]
for price in range(len(price_list)):
    if type(price_list[price]) == float:
        head = int(price_list[price]) #рубли
        tail = round((price_list[price] % 1) * 100) #копейки
        if tail < 10:
            tail = '0{}'.format(tail)
    if type(price_list[price]) == int:
        head = price_list[price]
        tail = '00'
    print('{}руб {}коп'.format(head, tail))
# B. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что
# объект списка после сортировки остался тот же).
print(id(price_list))
price_list.sort() #сортировка по возрастанию
print((price_list))
print(id(price_list)) #тот же id, значит объект остался тот же

# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
import copy #строчка высвечивается серым, как будто является текстом
# почему-то не срабатывало через copy, deepcopy, поэтому делал через срез

price_decrease = price_list[:]
price_decrease.sort(reverse=True)
print(price_decrease)

# Несработавший метод:
# price_decrease = price_list.sort(reverse=True)
# print(price_decrease)

# D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по
# возрастанию, написав минимум кода?
(price_list.sort(reverse=True))
five_top_prise = (price_list[:5])
five_top_prise.sort()
print(five_top_prise)