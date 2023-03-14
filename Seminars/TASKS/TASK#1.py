"""  
За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.
Input:
n = 700
m = 750
Output:
2
"""
n = int(input("Введите кол-во километров в первый день: "))
m = int(input("Маршрут пройденый во второй день: "))

countOfDay = (-(m//-n))
if countOfDay in (1,2,3,4):
    day = "день"
else:
    day = "дней"
print (f'Для того чтобы проехать {m} километров требуется {countOfDay} {day}')
