# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# my_list = [7, 5, 3, 3, 2]
# kol=0
# r=int(input('Введите новый рейтинг  '))
# for i in range(len(my_list)):
#     if r<=my_list[i]:
#         element = my_list[i]
#         ind_element = i
#         kol+=1
# if kol == 0:
#     my_list.insert(0, r)
#     print(my_list)
# else:
#     my_list.insert(ind_element+1,r)
#     print(my_list)

# 2 способ
my_list = [7, 5, 3, 3, 2]
r=int(input('Введите новый рейтинг  '))
my_list.append(r)
my_list.sort(reverse=True)
print(my_list)



