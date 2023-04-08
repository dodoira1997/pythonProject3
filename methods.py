#Методы списка
fruits = ['гранат', 'мандарин', 'яблоко', 'лимон', 'банан']
fruits.append('лайм')
print(fruits)
fruits.insert(2, 'апельсин')
print(fruits)
fruits.remove('банан')
print(fruits)
fruits.sort()
print(fruits)
#Методы словаря (dict)
toys = {'для мальчиков':'машинки',
        'для девочек':'куклы',
        'для самых маленьких' : 'погремушки'}
print(toys)
print(list(toys.keys()))
print(list(toys.values()))
print(list(toys.items()))
print(toys.clear())
print(toys.copy())
#Методы множеств (set)

# Методы строк (str)
pushkin = 'Я к вам пишу – чего же боле? Что я могу еще сказать?'
pushkin_upper = pushkin.upper()
print(pushkin_upper)
pushkin_replace = pushkin.replace('Что я могу еще сказать', 'Не знаю')
print(pushkin_replace)
pushkin_format = 'Татьяна писала: {}'.format(pushkin)
print(pushkin_format)
pushkin_find = pushkin.find('сказать')
print(pushkin_find)
pushkin_split = pushkin.split()
print(pushkin_split)