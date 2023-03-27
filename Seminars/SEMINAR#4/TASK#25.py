"""  
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n.

Пример ввода:
a a a b c a a d c d d

Пример вывода:
a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""

""" 
source = 'a a a b c a a d c d d'.split()
count_dict = {}


def transfer(source_list: list):
    # for idx, el in enumerate(source_list, start=1):
    for el in source_list:
        if el not in count_dict:
            count_dict[el] = 0
            yield el
            continue
        count_dict[el] += 1
        yield f'{el}_{count_dict[el]}'


[print(_, end=' ') for _ in transfer(source)]
 """
"""  
str1 = "a a a b c a a d c d d"


def twin_counter(str1):
    str1 = str1.split(" ")
    temp = []

    for i in range(len(str1)):
        counter = 0
        for j in str1[:i]:
            if str1[i] == j:
                counter += 1
        if counter > 0:
            counter = f'_{counter}'
        else:
            counter = ''

        temp.append(f"{str1[i]}{counter}")

    print(temp)


twin_counter(str1)
"""

s = input('Please input text: ').split()
d = {}

for i in s:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
    print(f"{i}", end="")
    if d[i] > 1:
        print(f"_{d[i]}", end=" ")
    else:
        print(' ', end="")


""" def using_dict(source: str) -> None:

    count_dict = {}
    stack = []
    for index in range(len(source)):
        el = source[index]
        if el.isalnum():
            count_dict[el] = source[:index].count(el)
            stack.append(el if not count_dict[el] else f'{el}_{count_dict[el]}')

    print('From using_dict\t->', ' '.join(stack))


def using_str(sequence: str):

    stack = []
    for index in range(len(sequence)):
        char = sequence[index]
        if not char.isalnum():
            continue
        counter = sequence[:index].count(char)
        stack.append(char if not counter else f'{char}_{counter}')
    print('From using_str\t->', ' '.join(stack)) 


def main() -> None:
    queue = 'a a a b c a a d c d d'
    using_str(queue)
    using_dict(queue)


if __name__ == '__main__':
    main()
"""

"""  

array = ("a a a b c a a d c d d").split()

counts = {}
for num in array:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

for num, count in counts.items():
    if count > 1:
        print(f"Число {num} повторяется {count} раз(а)")
        print(f"Число {num} повторяется {count} раз(а)")
"""