# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

def input_num(message: str) -> int:
    input_error: bool = True
    while input_error:
        try:
            temp = int(input(message))
        except ValueError:
            print("Вы ввели не число!")
        else:
            input_error = False
            return temp


def input_list(message: str) -> list:
    temp_list = []
    for i in range(input_num('Please input size of ' + message + ': ')):
        temp_list.append(input_num(f'{i + 1} element of {message}: '))
    print('-' * 20)
    return temp_list


def n_minus_m(n_local: list, m_local: list) -> list:
    n_edit = []
    m_local = set(m_local)
    for i in n_local:
        if i in m_local:
            n_edit.append(i)
    return n_edit


n, m = [input_list(x) for x in ('list N', ' list M')]
print(n, m)
n_m = [i for i in n if i not in m]
print(*n_m)
print(*n_minus_m(n, m))