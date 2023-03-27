def Fib(n):
    if n in [1,2]:
        return 1
    return Fib(n-1) + Fib(n-2)
list_1 = [0]
for i in range(1,10):
    list_1.append(Fib(i))
print(list_1)

