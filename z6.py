# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.


structura=[
(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
(2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
(3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

z=[]
klych=[]
dict_keys=structura[0][1].keys()
print(dict_keys)
for i in dict_keys:
    a=[]
    for j in range(len(structura)):
        znach=structura[j][1][i]
        a.append(znach)
    z.append(a)
print(z)
itog = dict(zip(dict_keys, z))
print(itog)


# {
# "название": ["компьютер", "принтер", "сканер"],
# "цена": [20000, 6000, 2000],
# "количество": [5, 2, 7],
# "ед": ["шт."]
# }
#