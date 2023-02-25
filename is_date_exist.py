'''
Написать функцию date, принимающую 3 аргумента — день, месяц и год.
Вернуть True, если такая дата есть в нашем календаре, и False иначе.
'''
from datetime import datetime


def date(d):
    try:
        date1 = datetime.strptime(d, '%m/%d/%Y')
        return True
    except ValueError:
        return False


exact_date = input("Введите день: ") + '.' + input('Месяц: ') + '.' + input('Год в формате YYYY: ')

if date(exact_date) is True:
    print('Дата существует')
else:
    print('Даты не существует или вы ввели неверные значения, попробуйте еще раз')
