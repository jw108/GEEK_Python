"""  

"""

def find_num(tmp_list):
    count = 0
    for i in range(1, len(tmp_list) - 1):
        if tmp_list[i - 1] < tmp_list[i] > tmp_list[i + 1]:
            count += 1
    return count

list_1 = [1, 5, 1, 5, 1, 3, 2]
#list_1 = [1, 2, 3, 4, 5, 6]

print(find_num(list_1))