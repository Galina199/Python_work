### Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = int(input(Input n ))
a = [0]*n
a[0] = int(input(Input a[0] ))
d = int(input(Input d ))
print(a[0],end= )
for i in range(1,n):
    a[i]= a[i-1]+d
    print(a[i],end= )


#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#(т.е. не меньше заданного минимума и не больше заданного максимума)
#Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#Вывод: [1, 9, 13, 14, 19]'''

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_2 = []
max = 10
min = 6
# for i in range(len(lst_1)):
# if list_1[i] >= min and list_1[i] <= max:
# list_2.append(i)
# print(list_2)
# или
for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end=' ')