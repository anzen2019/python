""""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
str, решить поставленную задачу? Функция должна возвращать результат числового типа,
например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
выведите курсы доллара и евро
"""
import requests
from datetime import datetime

def cur_rate(cur_code='', path ="http://www.cbr.ru/scripts/XML_daily.asp"):
    cur_code = cur_code.upper()
    result = requests.get(path)
    if result.ok:
        cur = result.text.split(cur_code)
        if len(cur) == 1:
            return None
        else:
            value = cur[1].split('</Value>')[0].split('<Value>')[1]
            value = float(value.replace(',', '.'))
            date = result.headers["Date"]
            date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()
            print(f'Курс {cur_code}: {value}, {date}')
    else:
        return None


print(cur_rate('USd'))
print(cur_rate('eUR'))

if __name__ == '__main__':
    # print(*currency_rates('USD'), sep=', ')
    print(cur_rate('USD'))
    print(cur_rate('eur'))
