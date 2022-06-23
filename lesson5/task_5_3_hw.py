"""
3. Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в
списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние
кортежи в виде: (<tutor>, None), например:
('Станислав', None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
"""
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Анна', 'Артем'
]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

#Способ обрезает класс ученика
# tut_in_klass = {tutors[i]: klasses[i] for i in range(len(tutors))}
# print(tut_in_klass)
print(len(tutors))
print(len(klasses))

def gen_tut_in_klass(people, grade):
    for i in range(len(people)):
        if i >= len(grade):
            print(people[i], None)
            continue
        else:
            yield (people[i], grade[i])

tutors_list = gen_tut_in_klass(tutors, klasses)
print(next(tutors_list))
print(next(tutors_list))
print(next(tutors_list))
print(next(tutors_list))
print(next(tutors_list))
print(next(tutors_list))
print(next(tutors_list))
print(next(tutors_list))
print(next(tutors_list)) #Артём, None не получается сделать кортежем
