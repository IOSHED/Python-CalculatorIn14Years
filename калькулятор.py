#калькулятор
import sys

print('ДОБРО ПОЖАЛОВАТЬ!')
bol = int(input('Чтобы войти в калькулятор нажмите "1", если хотите вычислить что-то по формуле нажмите "0": '))

if bol==1:
    colvo = 1
    while int(colvo <= 99):
        colvo=colvo+1
        a = float(input('Введите первое числo: '))
        s = float(input('Введите второе числo: '))
        why = input('Введите действие с клавиатуры: ')

        if why == '+' or why == 'плюс':
            c = a+s
            print('Ровно: ', c)
            continue
        elif why == '-' or why == 'минус':
            c = a-s
            print('Ровно: ', c)
            continue
        elif why == '*' or why == 'x' or why == 'умножить':
            c = a*s
            print('Ровно: ', c)
            continue
        elif why == '/' or why == 'делить':
            try:
                c = a/s
                print('Ровно: ', c)
            except ZeroDivisionError:
                print('У тебя "2" по математике? На ноль делить нельзя!')
            continue
        elif why == '//' or why == 'div':
            c = a//s
            print('Ровно: ', c)
            continue
        elif why == '%' or why == 'mod':
            c = a%s
            print('Ровно: ', c)
            continue
        elif why == '**' or why == 'возвести' or why == '^':
            c = a**s
            print('Ровно: ', c)
            continue
        elif why == 'корень из' or why == 'корень':
            c = a**(1/s)
            print('Ровно: ', c)
            continue
        else:
             print('Введено неизвестное действие')
             continue
else:
    colvo = 1
    while int(colvo <= 99):
        colvo = colvo + 1
        formylas = [1,2,3]
        print('1)Периметр ПРЯМОУГОЛЬНИКА по ширине, высоте: p=2(a+b)')
        print('2)Площадь ПРЯМОУГОЛЬНИКА по ширине, высоте: s=a*b')
        print('3)Площадь ПРЯМОУГОЛЬНИКА по диоганали и по известной стороны: s=a*(d^2-a^2)')
        f = input('Выбирите формулу(номер формулы): ')

        if f == '1':
            q = float(input('Введите ширину: '))
            w = float(input('Введите высоту: '))
            e = 2*(q+w)
            print('Периметр = ', e)
            payza = input('Продолжить(да,нет): ')
            if payza == 'да':
                continue
            elif payza == 'нет':
                sys.exit()
            else:
                print('Неверная команда!')
                continue
        elif f == '2':
            q = float(input('Введите ширину: '))
            w = float(input('Введите высоту: '))
            e = q*w
            print('Площадь = ', e)
            payza = input('Продолжить(да,нет): ')
            if payza == 'да':
                continue
            elif payza == 'нет':
                sys.exit()
            else:
                print('Неверная команда!')
                continue
        elif f == '3':
            q = float(input('Введите диоганаль: '))
            w = float(input('Введите известную сторону: '))
            e = w*(q**2-w**2)
            print('Площадь = ', e)
            payza = input('Продолжить(да,нет): ')
            if payza == 'да':
                continue
            elif payza == 'нет':
                sys.exit()
            else:
                print('Неверная команда!')
                continue