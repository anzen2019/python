"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает
объем ОЗУ компьютера.
"""
file = open('nginx_logs.txt', 'r')
data = []
for line in file:
    one_str = line.split(' ')
    data.append((one_str[0], one_str[5].replace('"', ''), one_str[6]))
print(data)
file.close()
