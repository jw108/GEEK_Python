"""  
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
dictionary = [{"V": "S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
unique = {''}
unique.clear()
for item in dictionary:
    print(item)
    for temp in item:
        unique.add(f'{item[temp]}')        
print(unique)

"""  
source = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005 "},
    {"V": "S009"},
    {"VIII": "S007"}
]


def unic_printer(list_data):
    result = set()
    for item in list_data:
        result.add(*item.values())
    print(result)


unic_printer(source)
"""