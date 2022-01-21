l=[1,2,'a','word',1.6,5,True]
for i in l:
    if type(i)==int:
        print(f'Элемент списка {i} -целого типа (int)')
    elif type(i)==float:
        print(f'Элемент списка {i} -вещественного типа (float)')
    elif type(i)==str:
        print(f'Элемент списка {i} имеет строковый тип данных (str)')
    elif type(i)==bool:
        print(f'Элемент списка {i}  тип данных Bool')