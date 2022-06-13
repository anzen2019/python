# 1. Реализовать вывод информации о промежутке времени в зависимости от его
# продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сеk
sec_per_min = 60
min_per_hour = 60
hour_per_day = 24
sec_per_hour = sec_per_min * min_per_hour
sec_per_day = sec_per_hour * hour_per_day
duration = int(input("Введите время в секундах: "))
if duration < 0: #расчет для секунд
    print('Ошибка, введите положительное значение')
elif duration < sec_per_min: #для минут
    print('Время: ', duration, 'cекунд')
elif sec_per_min <= duration < sec_per_hour:
    tmp_duration = duration
    dur_m = tmp_duration // sec_per_min
    dur_s = duration - dur_m * sec_per_min
    print('Время: ', dur_m, 'мин.,', dur_s ,'сек.')
elif sec_per_hour <= duration < sec_per_day:
    tmp_duration = duration
    dur_h = tmp_duration // sec_per_hour #количество часов
    dur_s = duration - dur_h * sec_per_hour #сколько секунд осталось после часов
    tmp_dur_s = dur_s #записали секунды для преобразований

    dur_m = tmp_dur_s // sec_per_min # количество минут
    dur_s = dur_s - dur_m * sec_per_min #количество секунд
    print('Время: ', dur_h, 'час.,', dur_m, 'мин.,', dur_s, 'сек.')
elif duration >= sec_per_day:
    tmp_duration = duration
    dur_d = tmp_duration // sec_per_day #дней
    tmp_duration = duration - dur_d * sec_per_day #сколько осталось секунд после дней
    dur_h = tmp_duration // sec_per_hour #количество дней
    dur_s = tmp_duration - dur_h * sec_per_hour  # сколько секунд осталось после часов
    tmp_duration = dur_s  # записали секунды для преобразований

    dur_m = tmp_duration // min_per_hour  #минут
    dur_s = tmp_duration - dur_m * sec_per_min  # количество секунд

    print('Время: ', dur_d, 'дн., ', dur_h, 'час., ', dur_m, 'мин.,', dur_s, 'сек.')
else:
    print('Ошибка')
