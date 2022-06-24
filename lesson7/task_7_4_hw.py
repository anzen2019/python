"""4. Написать скрипт, который выводит статистику для заданной папки
 в виде словаря, в котором ключи — верхняя граница размера файла
 (пусть будет кратна 10), а значения — общее количество файлов
 (в том числе и в подпапках), размер которых не превышает этой границы,
 но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat."""
import os
from collections import defaultdict
import django
folder = r'./'
# django_files = defaultdict(list)
#Массивы для файлов заданного диапазона
files_100 = []
files_1000 = []
files_10000 = []
files_100000 = []
for root, dirs, files in os.walk(folder):
    for file in files:
        adress = os.path.join(root, file)
        adress_size = os.stat(adress).st_size
        # print(adress, adress_size) #вывел пути всех файлов
        if adress_size < 10**2:
            files_100.append(adress)
        if 10**2 < adress_size < 10**3:
            files_1000.append(adress)
        if 10**3 < adress_size < 10**4:
            files_10000.append(adress)
        if 10**4 < adress_size < 10**5:
            files_100000.append(adress)

# Количество различных файлов
count_files = [len(files_100), len(files_1000), len(files_10000), len(files_100000)]

#задание геометрическое прогрессии для ключей словаря
file_size = []
size_first = 100
file_size.append(size_first)
size_prev = size_first
for i in range(1, 4):
    size_prev_cur = size_prev*10
    file_size.append(size_prev_cur)
    size_prev = size_prev_cur

answer = dict(zip(file_size, count_files))
print(answer)





