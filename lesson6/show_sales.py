# не оптимизирована частичное открытие файла
def show_price(argv):
    with open('bakery.csv', 'r', encoding='UTF-8') as file:
        program, *args = argv  #как работает эта строчка?
        if len(args) == 0:  #ничего не было введено одно число - покажи весь файл
            answer = file.readlines()
            answer = ''.join(answer)
            print(answer)
        if len(args) == 1:
            nums = list(map(int, args))
            start_read = nums[0] - 1
            answer = file.readlines()[start_read : ]
            answer = ''.join(answer)
            print(answer)
        if len(args) == 2:
            print(*args)
            print(args[0], args[1])
            nums = list(map(int, args))
            start_read = nums[0] - 1
            finish_read = nums[1]
            answer = file.readlines()[start_read : finish_read]
            answer = ''.join(answer)
            print(answer)

if __name__ == '__main__':
    import sys
    (show_price(sys.argv))