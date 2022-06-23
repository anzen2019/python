"""
2. * (вместо 1) Решить задачу генерации нечётных чисел
от 1 до n (включительно), не используя ключевое слово yield.
"""
odd_func = (num for num in range(1, 15 + 1, 2))
print(next(odd_func))
print(next(odd_func))
print(next(odd_func))
print(next(odd_func))
print(next(odd_func))
print(next(odd_func))
print(next(odd_func))
print(next(odd_func))
print(next(odd_func))




# nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
# print(next(nums_gen))
# print(next(nums_gen))