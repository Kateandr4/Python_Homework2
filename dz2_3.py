#Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int

import random

num = int(input('Введите размер списка: '))
my_list = []

for i in range(1, num+1, 1):
     my_list.append(i)

print('Исходный список:')
print(*my_list, sep=', ')

my_list_fin = my_list[:]

for i in  range(len(my_list)):
    ran = random.randint(0, num-1)
    temp = my_list_fin[i]
    my_list_fin[i] = my_list_fin[ran]
    my_list_fin[ran] = temp

print('Перемешаный список:')
print(*my_list_fin, sep=', ')

