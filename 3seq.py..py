element_per = input('Введите элементы 1-го списка:').split(',')
spisok = list(element_per)
element_vtor = input('Введите элементы 1-го списка:').split(',')
spisok_vtor = list(element_vtor)
for i in spisok.copy():
    if i in spisok_vtor:
     spisok.remove(i)
print('Результат:', ','.join(spisok))