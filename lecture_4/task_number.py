lower_border = int(input('Введи нижнюю границу:'))
higher_border = int(input('Введи верхнюю границу:'))

area = list(range(lower_border, higher_border))

start = 0
end = len(area) - 1
mid = (start+end)//2

while start <= end:
    check = input(f'Твое число больше, меньше или равно {area[mid]}? [>,<,=]')
    if check == '>':
        start = mid + 1
    elif check == '<':
        end = mid - 1
    elif check == '=':
        print(f'Было загадано число {area[mid]}!')
        break
    elif check == 'exit':
        print('Главное не сдаваться!')
        break
    mid = (start+end)//2
    
if start > end:
    print('Подозреваю, что твоего числа нет в диапазоне')