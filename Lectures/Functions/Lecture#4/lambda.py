data = '4 5 6 3 23 6 4  58 5 85 '
data = list(map(int,data.split()))
print(data)
""" 
!!! Данная функция это filter функция !!!
    def where(f,col):
    return [x for x in col if f(x)] 
"""
data = list(filter(lambda x: x%2 == 0,data)) 
print(data)
data = list(filter(lambda x: x%4 ==0,data))
print(data)
data = list(map(lambda x:(x,x**2),data))
print(data)
