'''
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
если год високосный, и False иначе.
'''

def is_year_leap(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        print('Год високосный!')
    else:
        print('Год не високосный!')

y = int(input('Введите год:'))
is_year_leap(y)