'''
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
которому этот месяц принадлежит (зима, весна, лето или осень)
'''


def season(month):
    if month in (1, 2, 12):
        return 'Зима'
    elif month in (3, 4, 5):
        return 'Весна'
    elif month in (6, 7, 8):
        return 'Лето'
    else:
        return 'Осень'


m = int(input('Введите месяц: '))
if 0 < m < 13:
    print(season(m))
else:
    print('Введите корректное число')
