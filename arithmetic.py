"""
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий -
операция, которая должна быть произведена над ними. Если третий аргумент +, сложить
их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных
случаях вернуть строку "Неизвестная операция".
"""


def arithmetic(first_digit, second_digit, operand):
    try:
        final_result = r'print({} {} {})'.format(first_digit, operand, second_digit)
        exec(final_result)
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except SyntaxError:
        print('Введите корректные значения')
    except NameError:
        print('Недопустимый ввод')


a = input('Введите первое число:')
b = input('Введите второе число:')

c = input('Введите операцию:')

arithmetic(a, b, c)
