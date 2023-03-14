

"""
Вы пользуетесь общественным транспортом? Вероятно,
вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no
"""
number = input('Введите шестизначный номер билета : ')
if number.isnumeric():
    number = int(number)
    if number < 100000 or number > 999999:
        print("Число не шестизначное")
    else:
        firs_three_number = number // 1000
        second_three_number = number % 1000
        if firs_three_number // 100 + (firs_three_number // 10) % 10 + firs_three_number % 10 == second_three_number // 100 + (second_three_number // 10 ) % 10 + second_three_number % 10:
            print('Билет счастливый')
        else:
            print('Билет не счастливый')
else:
    print("Ввели не число")