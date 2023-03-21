"""  
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X
"""
from random import randint

n = int(input("Введите размер массива: "))
array = []
for i in range(n):
    array.append(randint(1, 30))
print(array)
    

counts = {}
for num in array:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

for num, count in counts.items():
    if count > 1:
        print(f"Число {num} повторяется {count} раз(а)")
