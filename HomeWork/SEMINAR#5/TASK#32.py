"""  
Даны натуральные числа k и s. Определите, сколько существует k-значных натуральных чисел, сумма цифр которых равна s. 
Запись натурального числа не может начинаться с цифры 0.
В этой задаче можно использовать цикл для перебора всех цифр, стоящих на какой-либо позиции.
s<=k*9
"""

def recursion(len, sum, k, s):
    # Базовый случай
    if len == k:
        if sum == s:
            return 1
        else:
            return 0
    c = 1 if len == 0 else 0
    res = 0
    # Шаг рекурсии / рекурсивное условие
    for i in range(c, 10):
        res += recursion(len + 1, sum + i, k, s)
    return res

print(recursion(0, 0, 3, 15)) # вызов рекурсивной функции
