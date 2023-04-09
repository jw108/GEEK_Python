"""  
Чтобы лучше разобраться в типах параметров функций Инна создала inspect_function(), которая в качестве аргумента принимает другую функцию (главное, не встроенную, built-in). 
В результате работы она выводит следующие данные: название анализируемой функции, наименование всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.). 
Попробуйте повторить результат девушки.
Разобраться с / и **kwargs
"""
import inspect

def inspect_function(func):
    sig = inspect.signature(func)
    print(f"Анализируемая функция: {func.__name__}")
    print("Параметры:")
    for name, param in sig.parameters.items():
        if param.kind == inspect.Parameter.POSITIONAL_ONLY:
            print(f"  {name}: Позиционный параметр без значения по умолчанию")
        elif param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
            if param.default is inspect.Parameter.empty:
                print(f"  {name}: Позиционный параметр без значения по умолчанию")
            else:
                print(f"  {name}: Позиционный параметр со значением по умолчанию {param.default}")
        elif param.kind == inspect.Parameter.VAR_POSITIONAL:
            print(f"  {name}: Переменное количество позиционных параметров")
        elif param.kind == inspect.Parameter.KEYWORD_ONLY:
            if param.default is inspect.Parameter.empty:
                print(f"  {name}: Ключевой параметр без значения по умолчанию")
            else:
                print(f"  {name}: Ключевой параметр со значением по умолчанию {param.default}")
        elif param.kind == inspect.Parameter.VAR_KEYWORD:
            print(f"  {name}: Словарь с дополнительными параметрами")

def my_func(a, b,/, c, d, *args, e, f,**kwargs):
    pass

inspect_function(my_func)

