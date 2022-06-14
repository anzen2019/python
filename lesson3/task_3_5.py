"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
"мягкий"]
Например:
#>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы
сделать аргументы именованными?
"""
import random
def get_jokes(num_joke, n, adv, adj, repeats=True):
    max_num_joke = len(n) #длина массива до цикла, чтобы она не перезаписалась
    for i in range(num_joke):
        if num_joke > max_num_joke: #если хочется шуток больше, чем мы можем сделать
            print(f"Ошибка, введите число, не более {max_num_joke}")
            break
        else:
            if repeats==True: #если мы не против повторов в шутках
                print(random.choice(n), random.choice(adv), random.choice(adj))
            if repeats==False: #если хочется каждый раз уникальную шутку
                tmp_noun = random.choice(n)
                tmp_adv = random.choice(adv)
                tmp_adj = random.choice(adj)
                print(tmp_noun, tmp_adv, tmp_adj)
                n.remove(tmp_noun)
                adv.remove(tmp_adv)
                adj.remove(tmp_adj)
"""" Список массивов для шуток"""
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

""""Вывод действия функции"""
max_num_jokes = len(nouns)
numb = int(input(f'Сколько шуток желаете? Не больше  {max_num_jokes}: '))
get_jokes(numb, nouns, adverbs, adjectives, repeats=False)

