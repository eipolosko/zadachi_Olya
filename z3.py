# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
d={'Winter': [1,2,12],
   'Spring':[3,4,5],
   'Summer':[6,7,8],
   'Autumn':[9,10,11]}
print(d)
month=int(input('Введите номер месяца  '))
for key, value in d.items():
    for i in range(len(value)):
        if value[i] == month:
            print(key)
        else:
            key=None
if key==None:
    print('Вы ввели неправильный номер месяца')