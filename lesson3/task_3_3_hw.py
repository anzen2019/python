"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
содержащие имена, начинающиеся с соответствующей буквы. Например:
#>>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
"И": ["Иван", "Илья"],
"М": ["Мария"],
"П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется
сортировка по ключам? Можно ли использовать словарь в этом случае
"""
"""Способ 1 - сразу создать словарь
Не понял где можно применить оператор распаковки
"""
def thesaurus(name):
    peoples_name_alpha = {}
    for i in name:
        if i[0] not in peoples_name_alpha.keys():
            peoples_name_alpha.update({i[0]: [i]})
        else:
            peoples_name_alpha[i[0]] = peoples_name_alpha[i[0]] + [i]
    return peoples_name_alpha

peoples_name = ["Иван", "Мария", "Петр", "Илья", "Михаил"]
print(thesaurus(peoples_name))

""""Способ 2 - сначала создать массивы первых букв и имен
Не работает, тк видимо zip работает для массивов равной длины
Если массивы разной длины - обрезает до короткого
"""
# def thesaurus(name):
#     first_letter = []
#     names_list = []
#     for i in name:
#         names_list.append(i)
#         if i[0] not in first_letter:
#             first_letter.append(i[0])
#         # if i[0] in first_letter:
#     peoples_name_alpha = dict(zip(first_letter, names_list))
#     return peoples_name_alpha
