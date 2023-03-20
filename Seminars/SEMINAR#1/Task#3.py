# В некоторой школе решили набрать три новых математических класса и оборудовать 
# кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, 
# которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

import math

n1 = int(input("Сколько учеников в 1 классе? "))
n2 = int(input("Сколько учеников в 2 классе? "))
n3 = int(input("Сколько учеников в 3 классе? "))

m1 = math.ceil(n1/2)
m2 = math.ceil(n2/2)
m3 = math.ceil(n3/2)

result = m1 + m2 + m3
print(f"Нужно {result} парта(-ы)")