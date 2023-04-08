spisok = [int(i) for i in input('Введите элементы списка через запятую:').split(',')]
new = []
for i in spisok:
    if spisok.count(i) == 1:
        new.append(i)
print('Результат:', new, end='')
