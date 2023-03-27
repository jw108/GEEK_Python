# *** (1)У вас есть массив чисел, составьте из них максимальное число. Например:
#       [61, 228, 9] -> 961228

import random

a = []
for x in range(random.randint(3, 6)):
    a.append(random.randint(1, 250))
print(a)

s = sorted(map(str, a), reverse=True)
print(s)
n = ''
for i in s:
    n = n + i
print('Искомое число: ' + n)