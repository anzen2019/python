"""
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в
исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""
"""
Вариант 1 - Решение в лоб
"""
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# src = [1, 2, 2, 3, 9, 9]
# res = []
# # src_new = frozenset(src)
# for i in range(len(src)):
#     if res.count(src[i]) == 1:
#         res.remove(src[i])
#     else:
#         res.append(src[i])
# print(res)


"""
Вариант 2 - Решение с использованием множества
Не получилось вывести числа в порядке появления в исходном массиве
"""
src_1 = [1, 2, 2, 3, 9, 9]
src_2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def uniq_numbers(your_list):
    excess = []
    res = []
    for i in range(len(your_list)):
        if res.count(your_list[i]) == 1: #определяем числа, которые потом удалить
            excess.append(your_list[i])
        else:
             res.append(your_list[i])
    excess = set(excess) #множество лишних чисел
    src_set = set(your_list)
    res = src_set - excess
    return res
print(uniq_numbers(src_1))
print(uniq_numbers(src_2))

