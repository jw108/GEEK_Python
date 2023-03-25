def fib(arg):
    if arg in [0,1]:
        return 1
    return fib(arg-1)+fib(arg-2)

print(fib(0))