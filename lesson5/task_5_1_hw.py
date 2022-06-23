"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
yield, например:
#>>> odd_to_15 = odd_nums(15)
#>>> next(odd_to_15)
1
#>>> next(odd_to_15)
3
...
#>>> next(odd_to_15)
15
#>>> next(odd_to_15)
...StopIteration...
"""
def generate_odd(count):
    for x in range(1, count + 1, 2):
        if x <= count:
            yield x

odd_to_15 = generate_odd(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))



