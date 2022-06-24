"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта,
а в другом — данные об их хобби. Известно, что при хранении данных используется принцип:
одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые
данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

file_users = open('user.csv', 'r', encoding='UTF-8')
file_hobby = open('hobby.csv', 'r', encoding='UTF-8')

data_users = file_users.read().splitlines()
data_hobby = file_hobby.read().splitlines()

data_names = [] #массив имен пользователей без запятых
for user in data_users:
    name = user.split(',')
    name = " ".join(name)
    data_names.append(name)

data_outlook = [] #массив хобби пользователей без запятых
for hobby in data_hobby:
    data_outlook.append(hobby) #тут не нужно разделять запятые

data = {} #Итоговый словарь с данными
"""Пользователей меньше, чем хобби"""
if len(data_names) < len(data_outlook):
    print("Ошибка код 1")

"""Пользователей и хобби - равное количество"""
if len(data_names) == len(data_outlook):
    data = dict(zip(data_names, data_outlook))

"""Пользователей больше, чем хобби"""
if len(data_names) > len(data_outlook):
    for i in range(len(data_names)):
        if i < len(data_outlook):#для тех, у кого есть сведения о хобби
            data.update({data_names[i]: data_outlook[i]})
        else:
            data.update({data_names[i]: None})
print(data)

file_users.close()
file_hobby.close()
