"""
Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0
"""
number = input('Введите число: ')
summ = 0
if number.isnumeric():
    number = int(number)
    if number < 100 or number > 999:
        print("Число не трёхзначное")
    else:
        while number > 0:
            summ += number % 10
            number = number // 10
        print(f"Сумма чисел трёхназного числа = {summ}")
else:
    print("Ввели не число")