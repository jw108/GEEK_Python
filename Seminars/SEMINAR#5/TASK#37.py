# Введенные числа формирует в порядке возрастания:
def recursive_input2(size_n: int):
    x = input('please input: ')
    if size_n == 1:
        print(x, end=' ')
    else:
        recursive_input2(size_n - 1)
        print(x, end=' ')


n = int(input('Please input number: '))

recursive_input2(n)