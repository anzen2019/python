#Задача 2
""""
*Доработать предыдущую функцию в num_translate_adv(): реализовать
корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
должен быть с заглавной. Например:
#>>> num_translate_adv("One")
"Один"
#>>> num_translate_adv("two")
"два"
"""
def num_translate_adv(i, i_small):
    if i_small not in dict_translate.keys():
        print('None')
    elif i[0].isupper():#если заглавная буква большая
        return print(i, '-', dict_translate[i_small].capitalize())
    else:
        return print(i,'-' ,dict_translate[i_small])
dict_translate = {
    "zero": 'ноль',
    "one": 'один',
    "two": 'два',
    "three": 'три',
    "four": 'четыре',
    "five": 'пять',
    "six": 'семь',
    "seven": 'семь',
    "eight": 'восемь',
    "nine": 'девять',
    "ten": 'десять'
}

user_number = input('Enter number from 0 до 10: ')
user_number_small = user_number.lower() #привели число к нижн регистру
num_translate_adv(user_number, user_number_small)